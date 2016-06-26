#!/usr/bin/env python

import sys
from watchdog.observers import Observer
from lib.cli import parse_cli
from lib.watch import PymonEventHandler
from lib.listener import PymonListener
from lib.transport import transport
from lib.debug import *


def run():
    # Parse command-line arguments
    cli = parse_cli()

    # Create an event handler for file system changes
    event_handler = PymonEventHandler(
            cli["regexes"], 
            cli["ignores"], 
            True, False)

    # Create a file system observer
    observer = Observer()
    observer.schedule(
            event_handler, 
            cli["path"], 
            recursive=True)
    observer.start()

    # Create and register a listener for the user's application
    listener = PymonListener(
            cli["prog"], 
            cli["app_args"])
    transport.add_listener(listener)

    try:
        # Loop for user input
        while True:
            user_input = raw_input("")

            if user_input == "rs" or user_input == "restart":
                transport.emit("restart")
            elif user_input == "stop":
                raise Exception

    except (KeyboardInterrupt, Exception) as e:
        # Terminate all applications and exit
        transport.emit("stop")
        observer.stop()
        observer.join()


if __name__ == "__main__":
    run()
else:
    warn("Non-CLI usage has not been supported yet")
    sys.exit(0)
