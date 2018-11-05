import flask
import time

app = flask.Flask(__name__)

GameList = {}
@app.route('/games', methods=['GET', 'POST'])
def app_server():
    if flask.request.method == 'GET':
        timestamp = time.time()

        for timerecord in iter(GameList.items()):
            timediff = timestamp-timerecord
            if timediff > 30:
                del GameList[timediff]
            else:
                pass
        for key_ip in GameList.keys():
            return_value = str(key_ip) + "\n"
        
        return return_value
    
    if flask.request.method == 'POST':
        client_ip = flask.request.environ.get('HTTP_X_REAL_IP', flask.request.remote_addr)
        timestamp = time.time()

        for timerecord in iter(GameList.items):
            timediff = timestamp-timerecord
            if timediff > 30:
                del GameList[timediff]
            else:
                pass
        
        GameList.update({client_ip:time})
        return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)