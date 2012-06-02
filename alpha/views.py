﻿# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response;
from django.template import RequestContext, Template;
from django.core.context_processors import csrf;
from django.views.decorators.csrf import csrf_protect;

from models import Article, Entity, Loan;
from django.contrib.auth.models import User;

from controls import ArticleOrder, ArticleManager;


def column_width_percentage( columns ):
    return ( 96.0 / len(columns) ) if ( len(columns) < 3 ) else 30
    
    
def console( request ):

    manager = ArticleManager();
    
    return render_to_response( "clean.html", {
            'title': 'listing',
            'collection': map( 
                lambda e: ( e.article.name, len( e.entities ) ), 
                manager.get_entity_catalogue() 
            ),
            'content': "Fuck off"
        }
    );    
    
def process_loan( request ):
    order = ArticleOrder( request );
    
    for entity in order.get_flat_entity_order():
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
        
        loan.save();
        
        
         
    return render_to_response( "contract.html", {
            'title': 'Contract',
            'required': order.get_article_order().values(),
            'missing': order.get_missing_article_keys(),
            'acquired': order.get_flat_entity_order(),
        }
    );


def return_loan( request ):
    return render_to_response( "return.html", {} );
    
def process_return( request ):
    return render_to_response( "return.html", {} );    
    
def temporary_loan( request ):
    
    article_choices = extract_article_keys( request );
    
    columns = (
        [ "POST" ] + request.POST.items(),
        [ "GET" ] + request.GET.items(),
        [ "Loan Order" ] + \
            map( 
                lambda x: ( x, Article.objects.get(pk=x).name ), 
                article_choices
            ),
    );
    
    return render_to_response( 'generic.html', {
        'columnWidthPercentage': column_width_percentage( columns ),
        'columns': columns,
    });
    
@csrf_protect
def loan( request ):
    articles = Article.objects.all();
    manager = ArticleManager();
    
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
    