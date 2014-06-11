urlstr = location.href.substring(36)

$("#NAVBAR-COLL li a").each( function( index ) {
  if(urlstr == $( this ).attr("href")) $( this ).attr("class", "active");
});