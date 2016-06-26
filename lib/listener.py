import os
import subprocess
from lib.debug import *


class PymonListener():
    def __init__(self, prog="python", app_args=""):
        # Initialize instance variables
        self.prog = prog
        self.app_args = app_args
        self.proc = None

        # Start the application
        self.start()

    def get_app(self):
        return self.prog

    def start(self):
        # Check if there is already a running application
        if self.proc != None:
            warn("Already running %s %s" % (self.prog, self.app_args))
            return
        
        # Start the application
        # TODO: Need to listen for application terminating early/itself
        debug("Starting %s %s" % (self.prog, self.app_args))
        self.proc = subprocess.Popen([self.prog, self.app_args])

    def stop(self):
        # Check if there is a running application
        if self.proc == None:
            warn("No process running for %s" % self.prog)
            return

        # Terminate the application
        debug("Stopping %s %s" % (self.prog, self.app_args))
        self.proc.terminate()
        self.proc = None

    def restart(self):
        # Restart the application
        if self.proc != None:
            self.stop()
        self.start()

    def handle_msg(self, msg):
        debug(msg)

        # Determine the message nature
        # TODO: Create message constants
        if msg == "restart":
            self.restart()
        elif msg == "stop":
            self.stop()
        elif msg == "start":
            self.start()
        else:
            warn("Unknown command: %s" % msg)
