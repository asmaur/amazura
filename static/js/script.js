$(document).ready(function(){
    
    //console.log("hello world");
    
    
    /*START MENU JS*/
			$('a.page-scroll').on('click', function(e){
				var anchor = $(this);
				$('html, body').stop().animate({
					scrollTop: $(anchor.attr('href')).offset().top - 50
				}, 1500);
				e.preventDefault();
			});		

			$(window).scroll(function() {
			  if ($(this).scrollTop() > 100) {
				$('.menu-top').addClass('menu-change');
                  $('#topcontrol').show();
			  } else {
				$('.menu-top').removeClass('menu-change');
                  $('#topcontrol').hide();
			  }
			});
			
					
		/*END MENU JS*/ 
   /* 
    $('.owl-carousel').owlCarousel({
            loop:true,
            margin:10,
            nav:true,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:3
                },
                1000:{
                    items:5
                }
            }
        }); */

    
});