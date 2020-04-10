$(document).ready
(
    function ()
    {
        $(".toggleTapTalk").click
            (
            function()
            {
                toggleOverlay();
            }
            );
    }
);



var isOverlay = false;

function toggleOverlay()
{
    if (!isOverlay)
    {
        isOverlay = true;
        $(".tutorialOverlay").css("display", "block");
    }

    else
    {
        isOverlay = false;
        $(".tutorialOverlay").css("display", "none");
    }
}