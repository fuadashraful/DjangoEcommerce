

/******Carousal Jqeury ******/
$(document).ready(function(){



    $('.carousal-slide').slick({
        dots:true,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: true,
        focusOnSelect: true,
    });



$(".slick-prev").html("<i class='fa fa-arrow-left'></i>");
$(".slick-next").html("<i class='fa fa-arrow-right'></i>");


 });