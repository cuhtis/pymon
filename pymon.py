#!/usr/bin/env python

import sys
from watchdog.observers import Observer
from lib.cli import parse_cli
from lib.watch import PymonEventHandler
from lib.listener import PymonListener
from lib.transport import PymonTransport
from lib.debug import *

def run():
    cli = parse_cli()

    event_handler = PymonEventHandler(
            cli["regexes"], 
            cli["ignores"], 
            True, False)

    observer = Observer()
    observer.schedule(event_handler, cli["path"], recursive=True)
    observer.start()

    transport = PymonTransport()

    listener = PymonListener(cli["execp"], cli["app_args"])
    transport.add_listener(listener)

    try:
        while True:
            user_input = raw_input("")
            if user_input == "rs":
                transport.emit("restart")
            elif user_input == "stop":
                raise Exception
    except (KeyboardInterrupt, Exception) as e:
        transport.emit("stop")
        observer.stop()
        observer.join()

if __name__ == "__main__":
    run()
else:
    warn("Non-CLI usage has not been supported yet")
    sys.exit(0)
