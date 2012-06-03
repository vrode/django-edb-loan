# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Owner( User ):
    pass
    
class Person( User ):
    pass

class Article( models.Model ):
    name        = models.CharField( max_length = 80, unique = True );
    description = models.TextField( default = "" );

class Entity( models.Model ):
    article     = models.ForeignKey( Article );
    # code        = models.ForeignKey( Code );
    condition   = models.DecimalField( 
        max_digits = 5, 
        decimal_places = 4, 
        default = "1.0"
    );
    
class Code( models.Model ):
    FAMILY = (
        ('QR', 'qr'),
        ('BAR', 'barcode'),
    );
    code    = models.CharField( max_length = 80, unique = True );
    entity  = models.ForeignKey( Entity );
    family  = models.CharField( max_length = 10 , choices = FAMILY )
    
    
class Loan( models.Model ):
    entity          = models.ForeignKey( Entity, unique = True );
    fromPerson      = models.ForeignKey( User, related_name = "+" );
    toPerson        = models.ForeignKey( User, related_name = "+" );
    society         = models.TextField();
    location        = models.TextField();
    event           = models.TextField();
    # timeOrdered     = models.DateField();
    timeFetched     = models.DateField();
    timeExpired     = models.DateField();
    # timeReturned    = models.DateField();
    
class ArchivedLoan( models.Model ):
    entity          = models.ForeignKey( Entity, unique = True );
    fromPerson      = models.ForeignKey( User, related_name = "+" );
    toPerson        = models.ForeignKey( User, related_name = "+" );
    society         = models.TextField();
    location        = models.TextField();
    event           = models.TextField();
    # timeOrdered     = models.DateField();
    timeFetched     = models.DateField();
    timeExpired     = models.DateField();
    # timeReturned    = models.DateField();    
    