import _thread
import socket
import client

class thread():
    def __init__(self):
        self.reset()

    def stop(self):
        self._stop = True
        client.processOrder(self.addr, int(self.port), '')

    def stopped(self):
        return self._stop

    def reset(self):
        self._stop = False
        self._done = False
        self.addr = self.port = 0

    def finished(self):
        return self._done

    def run(self, fun, addr, port, n):
        self.addr = addr
        self.port = port
        _thread.start_new_thread(fun, (addr, port, self, n))

