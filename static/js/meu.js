$ (document).ready(function() {

	$('div#container').load('/aluno/primeiro');

 
   	$('div#nav a').click(function() {
      var page = $(this).attr("href");	
     $('div#container').load('/aluno/'+ page);
     return false;
      });
});