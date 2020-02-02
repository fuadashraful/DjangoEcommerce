$(document).ready(function(){

 $('.add-to-bag').click(function(){
    
    var ID= $(this).attr("data-id");
    console.log(ID);
 });

//  Elevate zoom

$(".productImg").elevateZoom({
   zoomType	: "inner",
   cursor: "crosshair"
 });
// End elevalte zoom
    
});