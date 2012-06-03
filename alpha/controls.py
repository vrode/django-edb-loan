from django.contrib.auth.models import User
from models import *
from sys import maxint



class ReturnOrder:
    def __init__( self, request, batch_separator = ";\n" ):
        self.batch = request.POST['batch'].split( batch_separator );
        self.batch = [c.replace( ";", "") for c in self.batch];
        
    def get_code_order( self ):
        result = [];
        for code in self.batch:
            candidates = Code.objects.filter( code = code );
            if len( candidates ) == 1:
                result.append( 
                    ( code, candidates[0].entity )
                );
            elif len( candidates ) == 0:
                result.append( 
                    ( code, None )
                );
            else:
                pass; # exception: non-unique code occured
        return result;
        
    def get_loan_order( self ):
        result = [];
        for ( code, entity ) in self.get_code_order():
            candidates = Loan.objects.filter( entity = entity );
            # [?] what if database contains multiple corrupted loans?
            if len( candidates ) >= 1:
                for loan in candidates:
                    result.append( 
                        ( entity, loan )
                    );
            else:
                result.append( 
                    ( entity, None )
                );
        return result;
                
    def execute_return( self ):
        print self.get_loan_order()[0];
        for ( entity, loan ) in self.get_loan_order():
            if loan != None:
                archived = ArchivedLoan(
                    entity = loan.entity,
                    fromPerson = loan.fromPerson,
                    toPerson = loan.toPerson,
                    society = loan.society,
                    location = loan.location,
                    event = loan.event,
                    timeFetched = loan.timeFetched,
                    timeExpired = loan.timeExpired
                );
                archived.save();
                loan.delete();
            


class LoanManager:
    def get_entity_catalogue( self ):
        result = [];
        for a in Article.objects.all():
            result.append(
                EntityOffer( a, quantity = maxint )
            );
        return result;
        
        
            
  
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
        
        

class Order:
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
        
    def get_insufficient_offers( self ):
        result = [];
        for offer in self.get_entity_order():
            if not offer.sufficient():
                result.append( offer );
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
        return "%d: Candidates: %d Selected: id=%s %s" % \
            ( self.quantity, 
              len(self.entities),  
              map ( lambda e: e.pk, self.select() ),
              self.sufficient()
              );        
        
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
    
    def sufficient( self ):
        """
        Tells whether the number of available entities is sufficient,
        to satisfy the quantity requirements of the order.
        """
    
        return ( self.quantity <= len( self.entities ) );
        
        
        
        
        
        
        
        
            