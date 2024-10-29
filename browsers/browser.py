from abc import ABC, abstractmethod
from websockets.sync.client import ClientConnection

class Browser(ABC):

    ws_autoclose_delay: int

    ws_endpoint: str
    ws: ClientConnection

    def __init__(self, browser_id: str = None, autoclose_timeout: int = 100, port: int = 9222, host: str = '127.0.0.1'):
        self.ws_autoclose_delay = autoclose_timeout
        self.initializeConnection(browser_id, port, host)
        # TODO - rethink autoclose and method proxying wrt. Python
    
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