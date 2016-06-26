import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEvent

class PymonEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        print "Change detected"

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print "usage: %s app.py <args>" % sys.argv[0]
        sys.exit(0)

    app = sys.argv[1]
    path = '.'
    regexes = ['.*[.]py']
    ignores = None

    event_handler = PymonEventHandler(regexes, ignores, True, False)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

