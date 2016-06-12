/**
 * Custom Project functions
 */

// +++ device detection +++++++++++++++++++++++++++++++++++++++


jQuery(document).ready(function($) {

	function logIt(label, value){
		console.log(label +": "+value);
	}

  // +++ device detection +++++++++++++++++++++++++++++++++++++++
  var iPhone = false;
  if(
    (navigator.userAgent.match(/iPhone/i))
    || (navigator.userAgent.match(/iPod/i))
    || (navigator.userAgent.match(/Opera Mini/i))
    || (navigator.userAgent.match(/Opera Mobi/i))
    || (navigator.userAgent.match(/Fennec/i))
    || (navigator.userAgent.match(/android/i))
  ){
     iPhone = true;
  }
  if(!iPhone){
    
  }else{
    
  }

  $(".header-close").click(function(){
    //logIt("Clicked?","!");
    $(this).parent().toggleClass("collapsed");
    //$(".toggleSometing").fadeToggle("slow");
  });

  $(".bs-callout-info .close").click(function(){
    $(this).parent().css("display","none");
  });
   
  
  // Toggle something
  $(".toggle-sidebar").click(function(){
    //if($(".navbar-brand").hasClass("collapse-sidebar")){
      //$(this).toggleClass("open");
      //$(".toggleSometing").fadeToggle("slow");
    //}
  });


});