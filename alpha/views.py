# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response;
from django.template import RequestContext, Template;
from django.core.context_processors import csrf;
from django.views.decorators.csrf import csrf_protect;

from models import Article, Entity, Loan;
from django.contrib.auth.models import User;

from controls import Order, LoanManager;


def column_width_percentage( columns ):
    return ( 96.0 / len(columns) ) if ( len(columns) < 3 ) else 30
    
    
def console( request ):
    
    order = Order( request );
    
    return render_to_response( "clean.html", {
            'title': 'listing',
            'collection': order.get_article_requirements(),
            'content': "Empty"
        }
    );    
    
def process_loan( request ):
    order = Order( request );
    
    missing = map( lambda a: a,
        order.get_missing_articles()
    );
    required = map( lambda a: a,
        order.get_article_order()
    );
    acquired = map( lambda e: e,
        order.get_entity_order()
    );
    
    listing = order.get_flat_entity_order();
    insufficient = order.get_insufficient_offers();
    
    for entity in listing:
        loan = Loan(
            entity          = entity,
            fromPerson      = User.objects.get( username = "ils" ),
            toPerson        = User.objects.get( username = "ils" ),
            society         = "none",
            event           = "none",
            location        = "none",
            timeFetched     = request.POST['timeFetched'],
            timeExpired     = request.POST['timeExpired']
        );
        
        #loan.save();
        
    return render_to_response( "contract.html", {
            'title': "Contract",
            'columns': (
                (   "Ønskede",
                    map( lambda e: ("%d %s" % (e.quantity, e.article.name)), required )
                ),
                (   "Manglende",
                    map( lambda e: e,       missing )
                ),
                (   "Manglende antall",
                    map( lambda e: e,       insufficient )
                ),                
                (   "Bekreftede",
                    map( lambda e: e, acquired )
                ),
                (   "Alle",
                    map( lambda e: e.article.name, listing )
                ),                
            )
        }
    );

    
    # return render_to_response( "contract.html", {
            # 'title': 'Contract',
            # 'missing': missing,
            # 'required': required,
            # 'acquired': acquired,
            # 'listing': listing,
            # 'insufficient': insufficient,
        # }
    # );


def return_loan( request ):
    return render_to_response( "return.html", {} );
    
def process_return( request ):
    return render_to_response( "return.html", {} );
    
@csrf_protect
def loan( request ):
    articles = Article.objects.all();
    manager = LoanManager();
    
    return render_to_response( 'loan.html', {
            'title': "Loan",
            'articles': articles,
            'articleCatalogue': manager.get_entity_catalogue(),
            'articlePrefix': "Article",
        },
        context_instance = RequestContext( request )
    )  

    
def welcome( request ):
    
    columns = (
        ( "Lån", 
            ( "Registrer Utlån", "/loan/" ), 
            ( "Tilbakelevering", False ),
            ( "Lagerstatus", False ),
        ),
        ( "Artikkel", 
            ( "Legg til en artikkel", False ), 
            ( "Søk i artikkeldatabasen", False ), 
            ( "List tilgjengelige artikler", False ), 
            ( "Varetellingsliste", False ), 
            ( "Skaderapport", False ), 
        ),
        ( "Person", 
            ( "Legg til en person", False ), 
            ( "Finn en person", False ),
            ( "List alle personene", False ),
            ( "Svart liste", False ),
        ),        
        ( "Arkiv", 
            ( "Statistikk", False ),
        ),
        ( "Testing",
            ( "Populér testdata", "/populate/" ),
            ( "Konsoll og logg", "/console/" ),
        ),
    );
    
    return render_to_response( 'welcome.html', {
            'title': "Welcome",
            'columnWidthPercentage': column_width_percentage( columns ),
            'columns': columns,
        } 
    )    
    
def populate( request ):

    Article.objects.all().delete()
    Entity.objects.all().delete()
    Loan.objects.all().delete()

    articles = (
        ( Article( name = "Aktiv Høytaler" ) ),
        ( Article( name = "DJ Flight Newmark" ) ),
        ( Article( name = "DJ Flight Pioneer" ) ),
        ( Article( name = "Platespiller" ) ),
        ( Article( name = "Mikser Blå" ) ),
        ( Article( name = "Mikser Grå" ) ),
        ( Article( name = "Mikrofon SM 57" ) ),
        ( Article( name = "DJ Boks" ) ),
        ( Article( name = "Mikrofonstativ" ) ),
        ( Article( name = "XLR Kabel" ) ),
        ( Article( name = "Strømkabel" ) ),
        ( Article( name = "Phonokabel" ) ),
        ( Article( name = "Phono-minijack kabel" ) ),
        ( Article( name = "Prosjektor Grå" ) ),
        ( Article( name = "Prosjektor Svart" ) ),
        ( Article( name = "VGA (skjerm) kabel" ) ),
    )

    from random import randint # generates random number of copies of articles
    
    for a in articles:
        a.save();
        for copy in range( randint( 1,4 ) ):
            e = Entity( article = a );
            e.save();
    
    columns = ( "Done",
        ( "Database", "The database is populated with test data." ),
    );
    
    return render_to_response( 'generic.html', {
        'columnWidthPercentage': column_width_percentage( columns ),
        'columns': columns
    } );  
    