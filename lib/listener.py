import os
import subprocess
from lib.debug import *

class PymonListener():
    def __init__(self, app):
        self.start()

    def start(self):
        debug("Starting")
        pass

    def stop(self):
        debug("Stopping")
        pass

    def restart(self):
        self.stop()
        self.start()
        pass

    def handle_msg(self, msg):
        debug(msg)
        pass
