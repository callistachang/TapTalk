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

  $("#left-menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("left-toggled");
  });

  $("#right-menu-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("right-toggled");
  });

$(function(){
  $('#isTaptalkOn').click(function() {
    $(".comments").toggle(this.checked);
    
    if (this.checked == false) {
      $(".articleSection").removeClass("col-10");
      $(".articleSection").addClass("col-12");

    } else {
      $(".articleSection").removeClass("col-12");
      $(".articleSection").addClass("col-10");
    }
  });
})