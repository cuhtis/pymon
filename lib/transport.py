from lib.debug import debug

class PymonTransport():
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        debug("Adding listener")
        self.listeners.append(listener)
    
    def get_listeners(self):
        return self.listeners
    
    def emit(self, msg):
        debug("Received message: %s" % msg)
        for listener in self.listeners:
            listener.handle_msg(msg)
