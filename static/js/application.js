
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/showall');

    //receive messages from server with websocket and show it on client
    socket.on('newfiles', function(msg) {
        console.log("Received files" + msg);
        payload_string = '';
        titlepayload = 'Payload data:'
        titleanswer = 'Response data:'
        payload_string = payload_string + '<br><br><p>' + titlepayload +'</p><p>' + JSON.stringify(msg.payload_j) + '</p><p>' + titleanswer + '</p><p>' + JSON.stringify(msg.answer_j) + '</p>'
        $('#log').html(payload_string);
    });
    socket.on('newerrorfiles', function(msg) {
        console.log("Received files" + msg);
        error_string = '';
        titleerror = 'Error message:'
        error_string = error_string + '<br><br><p>' + titleerror + '</p><p>' + JSON.stringify(msg.newerror) + '</p>'
        $('#log').html(error_string);
    });

});