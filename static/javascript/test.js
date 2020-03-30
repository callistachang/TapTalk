$(document).ready
(
    function ()
    {
        $("#redirectExpert").click
            (
            function ()
            {
                window.open("https://www.linkedin.com/in/jian-hao-toh-3767661a4/");
                return false;
            }
            );
    }
);





$(function(){
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    $(window).resize(function(e) {
      if($(window).width()<=768){
        $("#wrapper").removeClass("toggled");
      }else{
        $("#wrapper").addClass("toggled");
      }
    });
  });


$('#isTaptalkOn').click(function() {
    $("#taptalkOn").toggle(this.checked);
});