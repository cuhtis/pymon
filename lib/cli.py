import sys

def parse_cli(argv):
    if len(argv) <= 1:
        print "usage: python %s app.py <args>" % argv[0]
        sys.exit(0)

    cli = dict()

    cli["execp"] = "python"
    cli["app_args"] = ' '.join(argv[1:])
    cli["path"] = '.'
    cli["regexes"] = ['.*[.]py']
    cli["ignores"] = ['.*[.]pyc']
    
    return cli 
