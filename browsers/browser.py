from abc import ABC, abstractmethod
from websockets.sync.client import ClientConnection
import json

class Browser(ABC):

    request_id: int = 0

    ws_timeout: int

    ws_endpoint: str
    ws: ClientConnection

    def __init__(self, browser_id: str = None, autoclose_timeout: float = 0.1, port: int = 9222, host: str = '127.0.0.1'):
        self.ws_timeout = autoclose_timeout
        self.initializeConnection(browser_id, port, host)
    
    def req_id(self) -> int:
        self.request_id += 1
        return self.request_id
    
    def send(self, data: dict) -> dict:
        data['id'] = self.req_id()
        self.ws.send(json.dumps(data))
        return json.loads(self.ws.recv(self.ws_timeout))

    # --- BROWSER-SPECIFIC METHODS ---
    # Initialize the browser connection
    @abstractmethod
    def initializeConnection(self, _browserId, _port, _host):
        pass

    @abstractmethod
    def closeConnection(self, ):
        pass

    @abstractmethod
    def navigate(self, _url):
        pass

    @abstractmethod
    def click(self, _x, _y):
        pass