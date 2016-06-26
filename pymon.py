#!/usr/bin/env python

import sys
from watchdog.observers import Observer
from lib.cli import parseCli
from lib.watch import PymonEventHandler

def run():
    cli = parseCli(sys.argv)

    event_handler = PymonEventHandler(
            cli["regexes"], 
            cli["ignores"], 
            True, False)

    observer = Observer()
    observer.schedule(event_handler, cli["path"], recursive=True)
    observer.start()

    try:
        while True:
            user_input = raw_input("")
            if user_input == "rs":
                print "Restarting"
            elif user_input == "stop":
                raise Exception
    except (KeyboardInterrupt, Exception) as e:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    run()
else:
    print "Non-CLI usage has not been supported yet"
    sys.exit(0)
