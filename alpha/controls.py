from models import Article, Entity, Loan
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class Terms:

    def __init__( self, request ):

        def extract_entity_keys( request ):
            # retain the elements that start with the prefix
            entities = [ 
                x for x in request.POST if x.startswith( self.entity_prefix ) 
            ];
            # strip the prefix
            entities = map( lambda x: x.replace( "Entity", ""), entities );
            return entities;     
    
        # Integers
        self.entities       = extract_entity_keys( request );
        self.fromPerson     = request.POST['fromPerson'];
        self.toPerson       = request.POST['toPerson'];
        # Strings
        self.location       = request.POST['location'];
        self.society        = request.POST['society'];
        self.event          = request.POST['event'];
        # Times
        self.timeFetched    = request.POST['timeFetched'];
        self.timeExpired    = request.POST['timeExpired'];

    def entities_exist( self ):
        pass;
    
    def entities_are_in_store( self ):
        pass;
    
    def owner_exists( self ):
        pass;
    
    def owner_has_rights( self ):
        pass;
    
    def owner_has_correct_password( self ):
        pass;
    
    def user_exists( self ):
        pass;
    
    def user_is_not_blacklisted( self ):
        pass;

    def dates_are_consequent( self ):
        pass;
    
  


class Contract:
    
    def check_entities( self, entities ):
        # Check if every entity exists
        # Check that every entity is available
        # Check each entities' condition (fit, need of repair)    
    def check_owner( self, key, password = "" ):
        # Check if exists        
        # Check if has rights
        # Check if password is correct    
    def check_user( self, key ):
        # Check if exists
        # Check if not blacklisted    
    def check_dates( self, fetched, expired ):
        # Check that dates are consequent        
        # Check that period does not overlap with other reservations/loans    
    def check_purpose( self ):
        # Check if society exists
            # Check user/society-correspondence
        # Check if event exists
        # Check if location is approved for use of equipment
        # Calculate point scores and compare with conflicts/loan requirements