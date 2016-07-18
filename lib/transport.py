from lib.debug import debug


class PymonTransport():
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        # Register a listener
        debug("Adding listener")
        self.listeners.append(listener)

    def add_listeners(self, listeners):
        # Register a list of listeners
        debug("Adding listeners")
        self.listeners.extend(listeners)
    
    def remove_listener(self, listener):
        # Remove a listener from the list
        debug("Removing listener")
        self.listeners.remove(listener)
    
    def get_listeners(self):
        # Get all registered listeners
        return self.listeners
    
    def emit(self, msg):
        # Send a message to all listeners
        # TODO: rename as broadcast?
        debug("Received message: %s" % msg)
        for listener in self.listeners:
            listener.handle_msg(msg)


# Create a static instance of PymonTransport
transport = PymonTransport()
