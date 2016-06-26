import inspect
import sys
import os


# Check if debugging is enabled
# TODO: Add option to use config file to enable debugging
if "PYMON_DEBUG" in os.environ and os.environ["PYMON_DEBUG"] != "0":
    debugging = True
else:
    debugging = False


# Formatting constants
BOLD        = "\033[1m"
END         = "\033[0m"
WARN_COLOUR = "\033[93m"
FAIL_COLOUR = "\033[91m"


def is_debug():
    # Get debugging setting
    return debugging


def force_debug(enable=True):
    # Override default debug settings
    debugging = enable


def debug(msg):
    if debugging:
        # Print message with caller information
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        print "%s: %s" % (caller, msg)


def warn(msg):
    if debugging:
        # Print message with caller information in WARN_COLOUR
        stack = inspect.stack()[1]
        caller = "%s%s:%d:%s%s" % (BOLD, stack[1], stack[2], stack[3], END)
        msg = "%s%s%s" % (WARN_COLOUR, msg, END)
        
        print "%s: %s" % (caller, msg)


def wtf(msg, trace=False):
    if debugging:
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
