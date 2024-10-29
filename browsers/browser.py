from abc import ABC, abstractmethod
from websockets.sync.client import connect, ClientConnection

class Browser(ABC):

    ws_autoclose_delay: int
    ws: ClientConnection

    def __init__(self, browser_id: str = None, autoclose_timeout: int = 100, port: int = 9222, host: str = '127.0.0.1'):
        self.ws_autoclose_delay = autoclose_timeout

        # TODO - rethink autoclose and method proxying wrt. Python
    
    # --- BROWSER-SPECIFIC METHODS ---
    # Initialize the browser connection
    @abstractmethod
    def initializeConnection(_browserId, _port, _host):
        pass

    @abstractmethod
    def closeConnection():
        pass

    @abstractmethod
    def navigate(_url):
        pass

    @abstractmethod
    def click(_x, _y):
        pass