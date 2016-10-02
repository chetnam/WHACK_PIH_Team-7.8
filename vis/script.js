//Code for Selecting Location (currently using continents)
var locationTags = [ "North America", "Europe", "Asia", "South America", "Antartica", "Africa", "Australia" ];
$( "#autocomplete-locations" ).autocomplete({
  source: function( request, response ) {
          var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
          response( $.grep( locationTags, function( item ){
              return matcher.test( item );
          }) );
      }
});

//Code for Selecting Drugs
$( "#files" ).selectmenu();

//Code for setting priority
$( "#radioButtons" ).buttonset();
