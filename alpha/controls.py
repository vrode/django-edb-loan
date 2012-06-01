from models import Article, Entity, Loan
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoanManager:

    def __init__( self, entity_prefix = "Entity" ):
        self.entity_prefix = entity_prefix;
    
    def check( self, request ):
        
        # Integers
        entities = extract_entity_keys( request );
        fromPerson = request.POST['fromPerson'];
        toPerson = request.POST['toPerson'];
        # Strings
        location = request.POST['location'];
        society = request.POST['society'];
        event = request.POST['event'];
        # Times
        timeFetched = request.POST['timeFetched'];
        timeExpired = request.POST['timeExpired'];
    
    def extract_entity_keys( request ):
        # retain the elements that start with the prefix
        entities = [ 
            x for x in request.POST if x.startswith( self.entity_prefix ) 
        ];
        # strip the prefix
        entities = map( lambda x: x.replace( "Entity", ""), entities );
        
        return entities;  

    def check_entities( self, entities ):
        # Check if every entity exists
        # Check that every entity is available
        # Check each entities' condition (fit, need of repair)    
        return True;
        
    def check_owner( self, key, password = "" ):
        # Check if exists
        try:
            User.objects.get( username = key );
        except ObjectDoesNotExist:
            return False;
        
        # Check if has rights
        # Check if password is correct    
        return True;
    
    def check_user( self, key ):
        # Check if exists
        try:
            User.objects.get( username = key );
        except ObjectDoesNotExist:
            return False;
                
        # Check if not blacklisted    
        return True;
    
    def check_dates( self, fetched, expired ):
        # Check that dates are consequent        
        # Check that period does not overlap with other reservations/loans    
        return True;
    
    def check_purpose( self ):
        # Check if society exists
            # Check user/society-correspondence
        # Check if event exists
        # Check if location is approved for use of equipment
        # Calculate point scores and compare with conflicts/loan requirements    
        return True;
        
        