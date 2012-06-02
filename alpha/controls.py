from django.contrib.auth.models import User
from models import Article, Entity, Loan
    
class ArticleRequirement:
    def __init__( self, article_key, quantity, article_key_prefix = "Article" ):
        
        self.article_key = \
            article_key.replace( article_key_prefix, "" );
        
        try:
            self.quantity = int( quantity );
        except ValueError:
            self.quantity = 0;
        
        self.article = self.get_article();
    
        
    def __len__( self ):
        return self.quantity;
    
    def __str__( self ):
        return "%d: %s" % (self.quantity, self.article );
    
    def get_article( self ):
        candidates = Article.objects.filter( pk = self.article_key );
        if len( candidates ) == 1:
            return candidates[0];
        else:
            return None;
        
    def get_entity_offer( self ):
        if self.article is None:
            return None;
        else:
            return EntityOffer( self.article, self.quantity );
        
        

class ArticleOrder:
    def __init__( self, request, prefix = "Article" ):
        self.request = request;
        self.prefix = prefix;
    
    def get_requirements( self ):
        """
        Extracts all, even zero quantity articles.
        """
        result = [];
        for (key, quantity) in self.request.POST.items():
            if key.startswith( self.prefix ):
                result.append(
                    ArticleRequirement( key, quantity )
                );
        return result;        
    
    def get_missing_articles( self ):
        result = [];
        for r in self.get_requirements():
            if r.article is None:
                result.append( r );
        return result;
    
    def get_article_order( self ):
        result = [];
        for r in self.get_requirements():
            if r.quantity > 0 and r.article is not None:
                result.append( r );        
        return result;
        
    def get_entity_order( self ):
        result = [];
        article_order = self.get_article_order();
        for r in article_order:
            offer = r.get_entity_offer();
            result.append( offer );
        return result;
        
    def get_flat_entity_order( self ):
        result = [];
        for offer in self.get_entity_order():
            for entity in offer.select():
                result.append( entity );
        return result;
        
    
class ArticleManager:
    MAX_ENTITY_COUNT = 99;
    
    def __init__( self ):
        pass;
    
    def get_entities( self, article ):
        return Entities.objects.filter( article = article );
    
    def get_available_entities( self, article ):
        result = [];
        for e in self.get_entities( article ):
            existing_loans = Loan.objects.filter( entity = e );
            if len( existing_loans ) == 0:
                result.append( e );
        return result;
    
    def get_entity_catalogue( self ):
        catalogue = [];
        articles = Article.objects.all();
        for article in articles:
            catalogue.append( 
                EntityOffer( article, 
                    quantity = ArticleManager.MAX_ENTITY_COUNT 
                ) 
            );
        return catalogue;
            

        
class EntityOffer:
    def __init__( self, article, quantity = 1 ):
        self.article = article;
        self.quantity = quantity;
        
        candidates = \
            Entity.objects.filter( article = article );
    
        if len( candidates ) > 0:
            self.entities = candidates;
        else:
            self.entities = None;
        
    def __len__( self ):
        return len( self.entities );
        
    def __str__( self ):
        return "%d: Candidates: %d Selected: id=%s" % \
            ( self.quantity, 
              len(self.entities),  
              map ( lambda e: e.pk, self.select() ) );        
        
    def select( self ):
        """
        Chooses a number of available entity from the list of existing.
        Excludes the entities that are currently on loan, but does not
        check their date.
        """
        from random import choice, sample;
        candidates = [];
         
        # check if available (not on loan) depends on time-consistant loan table
        available_entities = [];
        for e in self.entities:
            existing_loans = Loan.objects.filter( entity = e );
            if len( existing_loans ) == 0:
                available_entities.append( e );

        # random choice from the available
        if len( available_entities ) > 0:
            if len( available_entities ) > self.quantity:
                # there are enough available entities to fulfill the order
                candidates = sample( available_entities, self.quantity );
            else:
                # there are not enough available entities to fulfill the order
                candidates = available_entities; # max out the offer
        
        return candidates;
    
        
        
        
        
        
        
        
        
        
            