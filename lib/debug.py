import inspect
import sys
import os

if "PYMON_DEBUG" in os.environ and os.environ["PYMON_DEBUG"] != "0":
    debugging = True
else:
    debugging = False

BOLD        = "\033[1m"
END         = "\033[0m"
WARN_COLOUR = "\033[93m"
FAIL_COLOUR = "\033[91m"

def is_debug():
    return debugging

def force_debug(enable=True):
    debugging = enable

def debug(msg):
    if debugging:
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        print "%s: %s" % (caller, msg)

def warn(msg):
    if debugging:
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        msg = "%s%s%s" % (WARN_COLOUR, msg, END)
        
        print "%s: %s" % (caller, msg)

def wtf(msg, trace=False):
    if debugging:
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        msg = "%s%s%s" % (FAIL_COLOUR, msg, END)
        
        print "%s: %s" % (caller, msg)
        
        if trace:
            print "Stack trace:"
            for level in inspect.stack()[1:]:
                print "\t%s:%s:%d:%s" % (level[0], level[1], level[2], level[3])

        sys.exit(1)
