import inspect
import sys
from lib.settings import get_settings


# Formatting constants
BOLD            = "\033[1m"
END             = "\033[0m"
WARN_COLOUR     = "\033[93m"
FAIL_COLOUR     = "\033[91m"
RED_COLOUR      = "\033[31m"
GREEN_COLOUR    = "\033[32m"
YELLOW_COLOUR   = "\033[33m"
BLUE_COLOUR     = "\033[34m"


def is_debug():
    # Check if debugging is enabled
    debugging = get_settings()["debug"]

    return debugging


def force_debug(enable=True):
    # Override default debug settings
    debugging = enable


def debug(msg):
    if is_debug():
        # Print message with caller information
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        print "%s: %s" % (caller, msg)


def warn(msg):
    if is_debug():
        # Print message with caller information in WARN_COLOUR
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        msg = "%s%s%s" % (WARN_COLOUR, msg, END)
        
        print "%s: %s" % (caller, msg)


def wtf(msg, trace=False):
    if is_debug():
        # Print message with caller information in FAIL_COLOUR then exit
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        msg = "%s%s%s" % (FAIL_COLOUR, msg, END)
        
        print "%s: %s" % (caller, msg)
        
        if trace:
            # Print entire stack trace
            print "Stack trace:"
            for level in inspect.stack()[1:]:
                print "\t%s:%s:%d:%s" % (level[0], level[1], level[2], level[3])

        # Exit with error code 1
        sys.exit(1)

def colour_print(colour, msg):
    print_msg = "%s%s%s" % (colour, msg, END)
    print(print_msg)
