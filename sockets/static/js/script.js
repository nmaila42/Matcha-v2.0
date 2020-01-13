var socket = io();
const messages = document.getElementById("messages");
const message = document.getElementById("message-box");
const to = document.getElementById("to");
const sendbtn = document.getElementById("send");
const online = document.getElementById("online-users");

var sender = "";

socket.on('connect', function() {
    socket.emit('connection-event', 
    {data: 'I\'m connected!'}, 
    function(x){
        sender = x;
        console.log(sender);
    })
})

window.onbeforeunload = closeConnection

function closeConnection(){
    socket.emit('disconnection-event', sender , function(x){console.log(x)});
}

socket.on('update-online-users', function(users) {
    console.log('updating...');
    users.forEach(user => {
        console.log(user);
        tag = document.createElement("p");
        tag.innerHTML = user;
        tag.id = user;
        tag.addEventListener("click", usernameClicked)
        online.appendChild(tag);
    });
});

function usernameClicked(e){
    console.log(e.target.id);
    inline.removeChild(document.getElementById(e.target.id))
}

sendbtn.addEventListener('click', function(e){ sendMessage(message.value)});

function sendMessage(msg){
    console.log(msg);
    console.log(recievedAction);
    socket.emit('new-message', {from: sender,
                                to: to.value,
                                message: msg
                                });
}


socket.on('message-recieved', function(msg){
    var newMessage = "<div class='message'> <span class='sender'>"+msg.from+"</span>  <span class='message'>"+msg.message+"</span> </div>";
    divMessage = document.createElement('div');
    msgSender = document.createElement('span');
    msgText = document.createElement('span');
    

    messages.appendChild(divMessage);
    
    divMessage.appendChild(msgSender);
    divMessage.appendChild(msgText);
    
    msgSender.innerHTML = msg['from'];
    msgText.innerHTML = msg['message'];

    console.log(msg);
})
