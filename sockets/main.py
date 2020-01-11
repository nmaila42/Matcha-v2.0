from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

online_users = []

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('json')
def handle_json(json):
    print('received json on handle json: ' + str(json))


@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('new-message')
def handle_new_message(message):
    print('received message: ' + str(message))
    socketio.emit('message-recieved', message)



@socketio.on('connection-event')
def handle_connection_event(json):
    user = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    online_users.append(user)
    print('received json on handle custom event: ' + str(json))
    update_online_users()
    return user


@socketio.on('disconnection-event')
def handle_disconnection_event(name):
    
    online_users.remove(name)
    print('received json on handle custom event: ' + name)
    update_online_users()
    return name + ' has left'

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json on handle custom event: ' + str(json))

def update_online_users():
    socketio.emit('update-online-users', online_users)

if __name__ == '__main__':
    socketio.run(app, debug=True)
