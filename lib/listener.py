import os
import subprocess
from lib.debug import *

class PymonListener():
    def __init__(self, prog="python", app_args=""):
        self.prog = prog
        self.app_args = app_args
        self.proc = None
        self.start()

    def get_app(self):
        return self.prog

    def start(self):
        if self.proc != None:
            warn("Already running %s %s" % (self.prog, self.app_args))
            return
        
        debug("Starting %s %s" % (self.prog, self.app_args))

        self.proc = subprocess.Popen([self.prog, self.app_args])

    def stop(self):
        if self.proc == None:
            warn("No process running for %s" % self.prog)
            return

        debug("Stopping %s %s" % (self.prog, self.app_args))
        self.proc.terminate()
        self.proc = None

    def restart(self):
        if self.proc != None:
            self.stop()
        self.start()

    def handle_msg(self, msg):
        debug(msg)
        if msg == "restart":
            self.restart()
        elif msg == "stop":
            self.stop()
        elif msg == "start":
            self.start()
        else:
            warn("Unknown command: %s" % msg)
