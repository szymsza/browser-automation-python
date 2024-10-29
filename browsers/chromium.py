from .browser import Browser
from websockets.sync.client import connect

class Chromium(Browser):
    def initializeConnection(self, browserId, port, host):
        self.ws_endpoint = f'ws://{host}:{port}/devtools/browser/{browserId}'

        self.ws = connect(self.ws_endpoint)

        print(self.ws)
        self.ws.send("Hello world!")
        print("2")
        message = self.ws.recv()
        print(f"Received: {message}")

        pass

    def closeConnection(self):
        pass

    def navigate(self, url):
        pass

    def click(self, x, y):
        pass