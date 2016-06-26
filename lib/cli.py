import sys

def parseCli(argv):
    if len(argv) <= 1:
        print "usage: python %s app.py <args>" % argv[0]
        sys.exit(0)

    cli = dict()

    cli["app"] = sys.argv[1]
    cli["app_args"] = sys.argv[2:]
    cli["path"] = '.'
    cli["regexes"] = ['.*[.]py']
    cli["ignores"] = None
    
    return cli 
