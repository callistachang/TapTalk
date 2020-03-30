/*Wait for all the components to be loaded before applying the script*/
$(document).ready
(
    function ()
    {
        //Functions for the sidebar menu
        //Opens the side bar menu by setting shifiting it into view of the webpage
        $("#openHamburgerMenuButton").click(
            function()
            {
                openSideMenu();
            }
        );

        //Close the side bar menu by setting shifiting it into view of the webpage
        $("#closeHamburgerMenuButton").click(
            function ()
            {
                closeSideMenu();
            }
        );

        $("#OpenExpertButton").click
        (
            function ()
            {
                openExpertCommentsPanel();
            }
        );

        $("#OpenUserButton").click
        (
            function ()
            {
                openUserCommentsPanel();
            }
        );

        $("#transparentEffectExpert").click
        (
            function ()
            {
                closeExpertCommentsPanel();
            }
        );

        $("#transparentEffectUser").click
        (
            function ()
            {
                closeUserCommentsPanel();
            }
        );
    }
);

function openSideMenu()
{
    $("#mySidepanel").css("left", "0px");
}

function closeSideMenu()
{
    $("#mySidepanel").css("left", "-350px");
}

function openExpertCommentsPanel() {
    $("#expertCommentsPanelWrapper").css("left", "0px");
    $("#transparentEffectExpert").css("left", "350px");
}

function closeExpertCommentsPanel() {
    $("#expertCommentsPanelWrapper").css("left", "-350px");
    $("#transparentEffectExpert").css("left", "-300px");
}

function openUserCommentsPanel() {
    $("#userCommentsPanelWrapper").css("right", "0px");
    $("#transparentEffectUser").css("right", "350px");
}

function closeUserCommentsPanel() {
    $("#userCommentsPanelWrapper").css("right", "-350px");
    $("#transparentEffectUser").css("right", "-300px");
}