$(document).ready(function(){
	var altura=$("section.cont").offset().top;
	$(window).on('scroll',function(){
         if($(window).scrollTop()>altura){
         	$("nav.menu").addClass("menu-fixo");
         }
         else{$("nav.menu").removeClass("menu-fixo");}
	});


});