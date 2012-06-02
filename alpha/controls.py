from django.contrib.auth.models import User
from models import Article, Entity, Loan
    


class ArticleOrder:
    
    def __init__( self, request, prefix = "Article" ):
        self.request = request;
        self.prefix = prefix;
    
    def get_article_keys( self ):
        return [ 
            x.replace( self.prefix, "" ) for x in self.request.POST
            if x.startswith( self.prefix )
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
            entities = Entity.objects.filter( article = article );
            if len( entities ) >= 1:
                catalogue.append(
                    EntityOffer( article, entities )
                );
            else:
                catalogue.append(
                    EntityOffer( article, None )
                );
        
        # Remove the entities that are on loan
        
        return catalogue;
    
    def get_entity_order( self ):
        order = [];
        catalogue = self.get_entity_catalogue();
        for offer in catalogue:
            if len( offer ) > 1:
                from random import choice;
                order.append( 
                    # chooses the entity randomly
                    EntityOffer( offer.article, [ choice( offer.entities) ] )
                );
            else:
                order.append(
                    EntityOffer( offer.article, [ offer.entities[0] ] )
                );
        return order;
                
        
class EntityOffer:
    def __init__( self, article, entities ):
        self.article = article;
        self.entities = entities; # must be a sequence
    
    def __len__( self ):
        return len( self.entities );
        
        
        
        
        
        
        
        
        
        
            