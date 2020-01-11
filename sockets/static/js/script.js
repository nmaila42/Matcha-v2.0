var socket = io();
const messages = document.getElementById("messages");
const message = document.getElementById("message-box");
const sendbtn = document.getElementById("send");
var sender = "mosima";

socket.on('connect', function() {
    socket.emit('connection-event', {data: 'I\'m connected!'}, function(x){sender = x});
});

window.onbeforeunload = closeConnection

function closeConnection(){
    socket.emit('disconnection-event', sender , function(x){console.log(x)});
}

socket.on('update-online-users', function(x) {
    console.log(x);
});

sendbtn.addEventListener('click', function(e){ sendMessage(message.value)});

function sendMessage(msg){
    console.log(msg);
    socket.emit('new-message', {from: sender,
                                message: msg
                                });
}

socket.on('message-recieved', function(msg){
    var newMessage = "<div class='message'> <span class='sender'>"+msg.from+"</span>  <span class='message'>"+msg.message+"</span> </div>";
    divMessage = document.createElement('div');
    msgSender = document.createElement('span');
    msgText = document.createElement('span');
    
    messages
    messages.appendChild(divMessage);
    
    divMessage.appendChild(msgSender);
    divMessage.appendChild(msgText);
    
    msgSender.innerHTML = msg['from'];
    msgText.innerHTML = msg['message'];

    console.log(msg);
})