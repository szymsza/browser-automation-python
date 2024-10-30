from abc import ABC, abstractmethod
from websockets.sync.client import connect, ClientConnection
import json

class Browser(ABC):

    request_id: int = 0
    ws_timeout: int
    ws: ClientConnection

    def __init__(self, browser_id: str = None, port: int = 9222, host: str = '127.0.0.1', autoclose_timeout: float = 0.1):
        self.ws_timeout = autoclose_timeout
        self.ws = connect(self.get_ws_endpoint(host, port, browser_id), close_timeout=autoclose_timeout)
        self.initialize_connection(browser_id, port, host)

    def req_id(self) -> int:
        self.request_id += 1
        return self.request_id
    
    def send(self, data: dict) -> dict:
        data['id'] = self.req_id()

        print(data)

        self.ws.send(json.dumps(data))

        result = None

        while (result == None or ('method' in result and result['method'] != data['method']) or ('id' in result and result['id'] != data['id'])):
            result = json.loads(self.ws.recv(self.ws_timeout))
            print(result)

            if ('type' in result and result['type'] == 'error'):
                raise Exception(f'Received browser error: {result}')

        return result

    # --- BROWSER-SPECIFIC METHODS ---
    @abstractmethod
    def get_ws_endpoint(self, host: str, port: int, browser_id: str):
        pass

    @abstractmethod
    def initialize_connection(self, _browserId, _port, _host):
        pass

    @abstractmethod
    def close_connection(self, ):
        pass

    @abstractmethod
    def navigate(self, _url):
        pass

    @abstractmethod
    def click(self, _x, _y):
        pass