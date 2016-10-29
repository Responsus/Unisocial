$ (document).ready(function() {

	$('div#container').load('/professor/ads');

 
   	$('.item').click(function() {
      var page = $(this).attr("href");	
     $('div#container').load('/professor/' + page);
     return false;
      });
});
