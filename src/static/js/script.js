(function ($) {
    "use strict";

    //preloader
    $(window).bind("load", function () { // makes sure the whole site is loaded
        $("#status").fadeOut(); // will first fade out the loading animation
        $("#preloader").delay(450).fadeOut("slow"); // will fade out the white DIV that covers the website.
    });

	//Page scrolling
    $('.for-sticky .navigation').onePageNav({
        filter: ':not(.external)',
        scrollThreshold: 0.25,
        scrollOffset: 92
    });
    //sticky navigation
    $(".for-sticky").sticky({
        topSpacing: 0,
        className: 'shrink'
    });
    
	
    //change logo on scroll
    
    $(window).scroll(function() {
    if ($(document).scrollTop() > 1) {
        $('.logo').addClass('change-logo');
        $('.logo').addClass('vcenter');
    }
    else {
        $('.logo').removeClass('change-logo');
        $('.logo').addClass('vcenter');

    }
    });
    



	//create menu for tablet/mobile
	$(".menu-box .navigation").clone(false).find("ul,li").removeAttr("id").remove(".sub-menu").appendTo($(".mobile-menu"));
	$(".mobile-menu .sub-menu").remove();
	$('.mobile-menu').on('show.bs.collapse', function () {
		$('body').on('click', function () {
			$('.mobile-menu').collapse('hide');
		})
	})
	
	//toggle menu
	$('.menu-btn').on('click', function () {
		$('.mobile-menu').collapse({
			toggle: false
		});
	})
	//menu for tablet/mobile scrolling
	$('.mobile-menu a').bind('click', function (event) {
		var $anchor = $(this);
	
		$('html, body').stop().animate({
			scrollTop: $($anchor.attr('href')).offset().top -92
		}, 800, 'linear');
		event.preventDefault();
	});

    //slider homepage setting
    $(".home-slider").owlCarousel({
        navigation: false, // Hide next and prev buttons
        slideSpeed: 300,
        autoplay: true,
		autoHeight: true,
        pagination: true,
        paginationSpeed: 300,
        singleItem: true,
        transitionStyle: "fade"
    });


    //slider team setting
    $(".team-slider").owlCarousel({
        navigation: false, // Hide next and prev buttons
        slideSpeed: 300,
        autoplay: true,
		autoHeight: true,
        pagination: true,
        paginationSpeed: 300,
        singleItem: true,
        mouseDrag: false,
        stopOnHover: true,
        transitionStyle: "fade"
    });
	
    // script prettyphoto
    $(document).ready(function () {
        $("a[data-rel^='prettyPhoto']").prettyPhoto({
            hook: 'data-rel',
            deeplinking: false
        });
    });


    // Video responsive
    $("body").fitVids();

    $(".port-hov").hover(function() {
            //console.log("bok");
            $(this).css('opacity', 1);
            },
            function() {
                $(this).css('opacity', 0);
            //console.log("ajd bok");

           }
        );    

    //replace the data-background into background image
    /*
    $(".img-bg").each(function () {
        var imG = $(this).data('background');
        $(this).css('background-image', "url('" + imG + "') "

        );
    });
    */

    //move to hash after loading
    $(window).bind("load", function () {
        if (window.location.hash) {
            $('html, body').stop().animate({
                scrollTop: $(window.location.hash).offset().top - 93
            }, 300, 'linear');
        }
    });

    //portfolio ajax setting
    $(document).ready(function () {
        $('.port-ajax').click(function () {
			
            var toLoad = $(this).attr('data-link') + ' .worksajax > *';
            $('.worksajax').slideUp('slow', loadContent);

            function loadContent() {
                $('.worksajax').load(toLoad, '', showNewContent)
            }

            function showNewContent() {
                $.getScript("js/portfolio.js");
                $('.worksajax').slideDown('slow');
            }
            return false;
        });

        if ($(document).scrollTop() > 1) {
                    $('.logo').addClass('change-logo');
                    $('.logo').addClass('vcenter');
                    $('.sticky-wrapper').addClass('shrink');
        }

        function popNavBar(){
            setTimeout(function(){
                if ($(document).scrollTop() < 1) {
                    $('.logo').addClass('change-logo');
                    $('.logo').addClass('vcenter');
                    $('.sticky-wrapper').addClass('shrink');
                }
            },3000)
            setTimeout(function(){
                if ($(document).scrollTop() < 1) {
                        $('.logo').removeClass('change-logo');
                        $('.logo').removeClass('vcenter');
                        $('.sticky-wrapper').removeClass('shrink');
                }
            },6000)

        }
        //6000
        popNavBar();

        var hover_show;
        var index = 0;
        var duration = 3000; 
        
        function loopProjects() {
            $('.port-hov').each(function(index,item) {
                index = index + 1;
                setTimeout(function(){
                    $(item).mouseenter();},duration);
                
                duration = duration + 3000;
                
                setTimeout(function(){
                    if (!$(item).is(":hover")){
                        $(item).mouseleave();}},duration);
            });
        }
        
        //loopProjects();
        setInterval(loopProjects, index * 4000);
        //console.log(index * 4000);
        //console.log(duration);
    });


    //isotope setting(portfolio)
    /*
    var $container = $('.portfolio-body');
    $container.imagesLoaded(function () {
        $container.isotope();
    });

    // filter items when filter link is clicked
    $('.port-filter a').click(function () {
        var selector = $(this).attr('data-filter');
        $container.isotope({
            itemSelector: '.port-item',
            filter: selector
        });
        return false;
    });
    //adding active state to portfolio filtr
    $(".port-filter a").click(function (e) {
        $(".port-filter a").removeClass("active");
        $(this).addClass("active");
    });
	/*
	//background ticker
    $('.big-ticker:has(>div:eq(1))').list_ticker({
        speed: 5000,
        effect: 'fade'
    });
    */
	//add class on touch device
	if (Modernizr.touch) {
			$('body').addClass('no-para');
			
	}
})(jQuery);