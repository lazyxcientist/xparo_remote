
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
    
import json
import threading

xparo_website = '127.0.0.1:8000'

class Xparo(websocket.WebSocketApp):
    def __init__(self, *args, **kwargs):
        super(Xparo, self).__init__(*args, **kwargs)



class Remote():
    def __init__(self):
        self.websocket_connected = False
        self.email = None
        self.robot = None
        self.callback = None

    def connect(self,email,password,robot):
        sd = '''

    connencting to ...
    ██╗░░██╗██████╗░░█████╗░██████╗░░█████╗░
    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
    ░╚███╔╝░██████╔╝███████║██████╔╝██║░░██║
    ░██╔██╗░██╔═══╝░██╔══██║██╔══██╗██║░░██║
    ██╔╝╚██╗██║░░░░░██║░░██║██║░░██║╚█████╔╝
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░


        █▀▀█ █▀▀ █▀▄▀█ █▀▀█ ▀▀█▀▀ █▀▀ 
        █▄▄▀ █▀▀ █░▀░█ █░░█ ░░█░░ █▀▀ 
        ▀░▀▀ ▀▀▀ ▀░░░▀ ▀▀▀▀ ░░▀░░ ▀▀▀

    website: https://xplauncher.me/
    github:  https://github.com/lazyxcientist/xparo_remote
    email:   xpassistantpersonal@gmail.com
        '''
        print(sd)
        if not self.websocket_connected:
            socket_server='ws://'+xparo_website+'/ws/remote/'+str(email)+'/'+str(password)+'/'+str(robot)+'/'
            self.ws = Xparo(socket_server,
                            on_message=self.on_ws_message,
                            on_error=self.on_ws_error,
                            on_open=self.on_ws_open,
                            on_close=self.on_ws_close,)
            self.email = email
            self.robot = robot
            self.websocket_connected = True
            threading.Thread(target=self.ws.run_forever).start()
        else:
            print("already connected to xparo remote")
           

    def send_websocket_message(self,message):
        try:
            self.ws.send(json.dumps({"robot_id":self.robot,"type":"command","data":message}))
        except Exception as e:
            print(e)

    def on_ws_message(self, ws, message):
        if self.callback:
            self.callback(message)
        else:
            print(ws,message)

    def on_ws_error(self, ws, error):
        print(error)

    # def ws_connection(self, dt, **kwargs):
    #     print("connecting to websocket")
    #     threading.Thread(target=self.ws.run_forever).start()


    def on_ws_open(self, ws):
        self.websocket_connected = True
        sd = '''
        \\\\Connection Sussessfull//
           \\\\X.P.A.R.O remote//
            \\\\is 🄻🄸🅅🄴 now//
        
        '''
        print(sd)


    def on_ws_close(self, ws):
        self.websocket_connected = False
        sd = '''

        
         xparo remote is
    █▀▀ █── █▀▀█ █▀▀ █▀▀ █▀▀▄ 
    █── █── █──█ ▀▀█ █▀▀ █──█ 
    ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀─


        '''
        print("retry again !!!")






if __name__ == "__main__":

    
    remote = Remote()
    remote.connect("xparo_remote","123456789","robot_id")
    def callback(message):
        print(message)
    remote.callback = callback


    remote.send_websocket_message("hello")