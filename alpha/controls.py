from django.contrib.auth.models import User
from models import Article, Entity, Loan
    
MAX_ENTITY_COUNT = 99;
    
class ArticleManager:
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
                EntityOffer( article, quantity = MAX_ENTITY_COUNT ) 
            );
        return catalogue;
            
            


class ArticleOrder:
    
    def __init__( self, request, prefix = "Article" ):
        self.request = request;
        self.prefix = prefix;
    
    def get_article_keys( self ):
        return [ 
            x.replace( self.prefix, "" ) for x in self.request.POST
            if x.startswith( self.prefix )
        ];
    
    def get_missing_article_keys( self ):
        """
        Missing article keys often suggest
        1. an attempt of cross-site scripting
        2. an unsyncronized deletion of an object in the database
        """
        return [ a
            for a in self.get_article_order().items()
            if a[1] == None
        ];
    
    def get_article_order( self ):
        """ 
        Takes in article keys from the request and finds
        the corresponding object in the database.
        For each object that does not correspond to a database
        object, puts a None into a missing pk-index position 
        """
        result = {};
        article_keys = self.get_article_keys();
        for article_key in article_keys:
            article = Article.objects.filter( pk = article_key );
            if len( article ) == 1:
                result[article_key] = article[0];
            else:
                result[article_key] = None;
        
        return result;
    
    def get_article_names( self ):
        return [ 
            a.name 
            for a in self.get_article_order().values() 
            if a != None 
        ];
    
    def get_article_objects( self ):
        return [
            o
            for o in self.get_article_order().values()
            if o != None
        ];
        
    def get_entity_catalogue( self ):
        """
        This function collects all entities that correspond to
        a particular article, then finds those that are available
        for loan.
        """
        
        # Find the existing entities
        catalogue = []
        for article in self.get_article_objects():
            catalogue.append( EntityOffer( article ) )
        
        # Remove the entities that are on loan
        
        return catalogue;
    
    def get_entity_order( self ):
        order = [];
        catalogue = self.get_entity_catalogue();
        for offer in catalogue:
            order.append(
                ( offer.article, offer.select() )
            );
            
        return order;
    
    def get_flat_entity_order( self ):
        order = [];
        catalogue = self.get_entity_catalogue();
        for offer in catalogue:
            for entity in offer.select():
                order.append( entity );
        return order;

    def get_loan( self ):
        pass;
        
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
        
    def select( self, quantity = 1 ):
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
            if len( available_entities ) > quantity:
                # there are enough available entities to fulfill the order
                candidates = sample( available_entities, quantity );
            else:
                # there are not enough available entities to fulfill the order
                candidates = available_entities; # max out the offer
        
        return candidates;
    
        
        
        
        
        
        
        
        
        
            