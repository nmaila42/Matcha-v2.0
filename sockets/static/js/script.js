var socket = io();
const messages = document.getElementById("messages");
const message = document.getElementById("message-box");
const to = document.getElementById("to");
const sendbtn = document.getElementById("send");
var sender = "mosima";
var recievedAction = 'message-recieved'

socket.on('connect', function() {
    socket.emit('connection-event', {data: 'I\'m connected!'}, function(x){sender = x; console.log(sender);recievedAction = 'message-recieved-' + sender;});
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


// function setCookie(cookieName, cookieValue, exdays) {
//     var d = new Date();
//     d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
//     var expires = "expires="+d.toUTCString();
//     document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
//   }
  
//   function getCookie(cookieName) {
//     var name = cookieName + "=";
//     var ca = document.cookie.split(';');
//     for(var i = 0; i < ca.length; i++) {
//       var c = ca[i];
//       while (c.charAt(0) == ' ') {
//         c = c.substring(1);
//       }
//       if (c.indexOf(name) == 0) {
//         return c.substring(name.length, c.length);
//       }
//     }
//     return "";
//   }
  
//   function checkCookie() {
    
//     var user = getCookie("username");

//     while (user == "" || user == null) {
//       user = prompt("Please enter your name:", "");
//       if (user != "" && user != null) {
//         setCookie("username", user, 365);
//         break;
//       }
//     }
//   }