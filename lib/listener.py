import os
import subprocess
from lib.debug import *


class PymonListener():
    def __init__(self, prog="python", app_args=""):
        # Initialize instance variables
        self.prog = prog
        self.app_args = app_args
        self.proc = None

    def get_app(self):
        return self.prog

    def start(self, capture_out=False):
        # Check if there is already a running application
        if self.proc != None:
            warn("Already running %s %s" % (self.prog, self.app_args))
            return
        
        # Start the application
        # TODO: Need to listen for application terminating early/itself
        colour_print(GREEN_COLOUR, "[pymon] Starting '%s %s'" % (self.prog, self.app_args))
        if capture_out:
            self.proc = subprocess.Popen([self.prog, self.app_args], stdout=subprocess.PIPE)
        else:
            self.proc = subprocess.Popen([self.prog, self.app_args])

    def stop(self):
        # Check if there is a running application
        if self.proc == None or self.proc.poll() != None:
            warn("No process running for %s" % self.prog)
            self.proc = None
            return

        # Terminate the application
        debug("Stopping %s %s" % (self.prog, self.app_args))
        self.proc.terminate()
        self.proc = None

    def restart(self, capture=False):
        # Restart the application
        colour_print(GREEN_COLOUR, "[pymon] Restarting")
        if self.proc != None:
            self.stop()
        self.start(capture)
    
    def ping(self):
        print "Ping"
        self.proc.poll()
        if self.proc.returncode != None:
            colour_print(GREEN_COLOUR, "[pymon] '%s %s' has terminated" % (self.prog, self.app_args))
            self.proc = None

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
        elif msg == "ping":
            self.ping()
        else:
            warn("Unknown command: %s" % msg)
