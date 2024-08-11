$(document).ready(function () {
    
    // display the message on screen while chating with it
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        console.log("DisplayMessage called with:", message);
        $(".siri-msg").text(message);
        $(".siri-msg").textillate('start');
    }

    // display the main interface again after completion of chat
    eel.expose(ShowInterface)
    function ShowInterface() {
        $("#interface").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }
});