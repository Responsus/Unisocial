$(document).ready(function(){
   
   $(window).scroll(function(){
      var barra=$(window).scrollTop();
      var position=barra*0.20;
      $('body').css({
         'background-position':'0 -' +position+ 'px'
      });
   });
});