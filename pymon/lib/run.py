import sys
from watchdog.observers import Observer
from lib.settings import parse_settings
from lib.watch import PymonEventHandler
from lib.listener import PymonListener
from lib.transport import transport
from lib.debug import *


def run():
    # Create and read all the settings
    settings = parse_settings(sys.argv[1:])
    debug(settings)

    colour_print(BLUE_COLOUR, "[pymon] Pymon %s" % settings["version"])
    colour_print(BLUE_COLOUR, "[pymon] Watching %s" % settings["path"])

    # Create an event handler for file system changes
    event_handler = PymonEventHandler(
            settings["regexes"], 
            settings["ignores"], 
            True, False)

    # Create a file system observer
    observer = Observer()
    observer.schedule(
            event_handler, 
            settings["path"], 
            recursive=True)
    observer.start()

    # Create and register a listener for the user's application
    listener = PymonListener(
            settings["prog"], 
            settings["app_args"])
    transport.add_listener(listener)
    listener.start()

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
