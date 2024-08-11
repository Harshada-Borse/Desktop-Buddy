$(document).ready(function () {
    console.log("Document ready!");

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    // --Siri Wave--
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 950,
        height: 200,
        style: "ios9",
        amplitude: "1.5",
        speed: "0.30",
        autostart: true
    });

    // siri message animation
    $('.siri-msg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeInUp",
            sync: true,
        },
    });

    // mic button click event
    $('#micBtn').click(function (e) {  // jqClick
        console.log("Mic button clicked");
        eel.playStartSound(); // Call the Python function
        $('#interface').attr('hidden', true);  
        $('#siriwave').attr('hidden', false);
        eel.allComands()(function(response) {
            console.log("Response from Python:", response);
        });
    });
});
