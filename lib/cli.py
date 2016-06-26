import sys
import argparse
import textwrap
import ConfigParser

def parse_cli():
    config = ConfigParser.ConfigParser()
    config.read('settings.cfg')

    parser = argparse.ArgumentParser(sys.argv[0],
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                    Pymon %s
                    --------------------------------
                    Created by Curtis Li
                    ''' % config.get("pymon", "version")))

    parser.add_argument("-v", "--version", 
            action="version", 
            version=config.get("pymon", "version"))
    parser.add_argument("-r", "-R", "--recursive", 
            action="store_true",
            help="recursively monitor directories (Default)")
    parser.add_argument("--no-recursive",
            action="store_false",
            help="do not recursively monitor directories")
    parser.add_argument("--exec",
            action="store",
            metavar="PROG",
            default="python",
            help="program to execute application (Default: %s)" % config.get("pymon", "prog"))
    parser.add_argument("--match",
            action="append",
            metavar="REGEX",
            help="regex to match monitored files (Default: .py)")
    parser.add_argument("--ignore",
            action="append",
            metavar="REGEX",
            help="regex to filter monitored files (Default: .pyc)")
    parser.add_argument("args", 
            nargs=argparse.REMAINDER)

    args = parser.parse_args()
    
    cli = dict()

    cli["prog"] = "python"
    cli["app_args"] = ' '.join(sys.argv[1:])
    cli["path"] = '.'
    cli["regexes"] = ['.*[.]py']
    cli["ignores"] = ['.*[.]pyc']
    
    return cli 
