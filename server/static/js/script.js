//Code for Selecting Location (currently using continents)
var locationTags = [ "North America", "Europe", "Asia", "South America", "Antartica", "Africa", "Australia" ];
$( "#location" ).autocomplete({
  source: function( request, response ) {
    var matcher = new RegExp( "^" + $.ui.location.escapeRegex( request.term ), "i" );
    response( $.grep( locationTags, function( item ){
      return matcher.test( item );
    }) );
  }
});

//Code for Selecting Drugs
$( "#item" ).selectmenu();

//Code for setting priority
$( "#radioButtons" ).buttonset();
