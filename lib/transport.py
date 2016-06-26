from lib.debug import debug

class Transport():
    def __init__(self):
        self.listeners = []

    def addListener(self, listener):
        debug("Adding listener")
        listeners.append(listener)
    
    def getListeners(self):
        return self.listeners
    
    def emit(self, msg):
        debug("Received message: %s" % msg)
