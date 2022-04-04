$(document).ready(function() {

    function open_model(model_class_name) {
        $("." + model_class_name).show()
        $("." + model_class_name).addClass("show")
    }

    if (is_notification != "0") {
        open_model("myModal")
    }

    $(document).on('click', ".hide-notification", function(e) {
        // debugger;
        let url = this.dataset.target;
        let model_id = this.closest("div.show").id
        $.ajax({
            type: 'POST',
            url: url,
            success: function(response) {
                if (response["status"] == 200) {
                    let count = parseInt($(".notification-count").text()) - 1
                    $(".notification-count").text(count)
                    $("#" + model_id).hide();
                }
            },
        })
    })

    $(document).on('click', ".hide-all-notification", function(e) {
        $(".myModal").hide();
        $(".SocketModel").hide();
    })


    const notificationSocket = new WebSocket(
        'ws://' +
        window.location.host +
        '/ws/notification/' +
        roomName +
        '/'
    );
    console.log(notificationSocket)

    notificationSocket.onmessage = function(e) {

        const data = JSON.parse(JSON.parse(e.data)['notification']);
        let test = $("#socket_model").clone().appendTo(".container");
        let notification_id = data[0]['pk']
        let user_id = data[0]['fields']['user']
        test[0].id = "model_" + notification_id
        test[0].classList.add("myModel", test[0].id)


        $("." + test[0].id + " .notification-title").text(data[0]['fields']['title'])
        $("." + test[0].id + " .notification-types").text(data[0]['fields']['types'])
        $("." + test[0].id + " .notification-text").text(data[0]['fields']['text'])
        $("." + test[0].id + " .hide-notification").attr(
            "data-target", `/notification/hide/${notification_id}/`
        )

        $("." + test[0].id + " .close").attr("id", notification_id)
        $("." + test[0].id).show()
        $("." + test[0].id).addClass("show")

        let count = parseInt($(".notification-count").text()) + 1

        $(".notification-count").text(count)
    };

    notificationSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
});
