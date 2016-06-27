# Pymon

Created by Curtis Li

Pymon is a Python port of Nodemon. It monitors the file system at a given path/directory, and restarts an application whenever changes are detected.

## Features

* Manual restarting of applications by typing `rs` or `restart` in command-line interface
* Automatic restarting of applications whenever changes in the file system are detected
* Able to custom specify a directory/path to monitor
* Able to use regex to filter and match which files/directories to monitor
* Use a configuration file or environment variables to preset your settings

## Basic Usage

To run an application, run:
```
./pymon.py app.py [args ...]
```
or
```
python pymon.py app.py [args ...]
```

To restart an application, type:
```
rs
```
or
```
restart
```

To stop an application, type:
```
stop
```
or
```
<Ctrl+C>
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

* Add support for use as a library
* Add support for multiple apps/processes
* Be installable as a pip library/module

## Dependencies

* Watchdog
