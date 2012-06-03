$( function() {

    /* */

    $( ".article" ).mouseover( function() {
        $( ".article" ).css( "background-color", "" );
    } );
    
    $( ".article" ).mouseout( function() {
        $( ".article" ).css( "background-color", "" );
    } ); 

    /* return.html */
    
    var instruction = "Les av koden";
    
    $( "#candidate" ).val( instruction );
    
    $( "#candidate" ).focus( function() {
        $( "#candidate" ).val( "" );
    });
    
    $( "#candidate" ).focusout( function() {
        $( "#candidate" ).val( instruction );
    });    
    
    $( "#candidate" ).keypress( function(event) {
        if ( event.which == 13 ) { /* 13 is 'enter' */
        
            var contents = $( "#batch" ).val();
            var candidate = $( "#candidate" ).val();
            
            if ( contents != "" ) {
                $( "#batch" ).val( contents + "\n" + candidate + ";" );
            } else {
                $( "#batch" ).val( candidate + ";" );
            }
            
            /* scroll down the batch textarea */
            var batch = $( "#batch" );
            batch.scrollTop(
                batch[0].scrollHeight - batch.height()
            );            
            
            /* clean out the candidate field */
            $( "#candidate" ).val( "" );
        }
    } );     
    
    
}); 