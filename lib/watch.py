from watchdog.events import PatternMatchingEventHandler, FileSystemEvent

class PymonEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        print "Change detected"
