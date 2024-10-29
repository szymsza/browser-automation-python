from .browser import Browser
from websockets.sync.client import connect
from time import sleep

class Chromium(Browser):
    session_id: int

    def initializeConnection(self, browserId, port, host):
        self.ws_endpoint = f'ws://{host}:{port}/devtools/browser/{browserId}'

        self.ws = connect(self.ws_endpoint)
        
        target_response = self.send({
            'method': 'Target.getTargets',
        })

        page_target = list(filter(lambda info: (info['type'] == 'page'), target_response['result']['targetInfos']))[0]['targetId']

        session = self.send({
            'method': 'Target.attachToTarget',
            'params': {
                'targetId': page_target,
                'flatten': True
            }
        })

        self.session_id = session['params']['sessionId']

    def closeConnection(self):
        pass

    def navigate(self, url):
        self.send({
            'sessionId': self.session_id,
            'method': 'Page.navigate',
            'params': {
                'url': url
            }
        })
        sleep(0.01)

    def click(self, x, y):
        self.send({
            'sessionId': self.session_id,
            'method': 'Input.dispatchMouseEvent',
            'params': {
                'x': x,
                'y': y,
                'type': 'mousePressed',
                'clickCount': 1,
                'button': 'left'
            }
        })

        self.send({
            'sessionId': self.session_id,
            'method': 'Input.dispatchMouseEvent',
            'params': {
                'x': x,
                'y': y,
                'type': 'mouseReleased',
                'button': 'left'
            }
        })