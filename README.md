# Pymon

Created by Curtis Li

Pymon is a Python port of Nodemon. It monitors the file system at a given path/directory, and restarts an application whenever changes are detected.

## Features

* Manual restarting of applications by typing `rs` in command-line interface
* Custom providing of a directory/path to monitor
* Use regex to filter and match which files/directories to monitor

## Basic Usage

```
./pymon.py app.py [args ...]
```
or
```
python pymon.py app.py [args ...]
```

## Advanced Usage

##### Help
```
./pymon.py --help
```

##### Version
```
./pymon.py --version
```

##### Verbose/Debug mode
```
./pymon.py --debug
```

##### Regex matching

To only monitor certain files:
```
./pymon.py --match ".*[.]py"
```

To ignore monitoring certain files:
```
./pymon.py --ignore ".*[.]pyc"
```

To use multiple regexes:
```
./pymon.py --match ".*[.]py" --match ".*[.]cfg" --ignore ".*[.]pyc"
```

## TODO

* Improve CLI interface
* Add support for directory ignores
* Add support for use as a library
* Add support for multiple apps/processes
* Be installable as a pip library/module

## Dependencies

* Watchdog
