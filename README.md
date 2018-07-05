# PHP4 Constructor Detector

## Description

Finds PHP classes that use the PHP4 constructor style that is now deprecated in PHP5 when using namespaces, and completely deprecated in PHP7.  Useful for checking if your codebase uses PHP4 constructors when upgrading PHP.

## Use

Clone this repo or download `pcd.py`.  Run the script by providing a directory to scan for PHP files, e.g.:

```bash
python3 pcd.py /path/to/src/
```

To run recursively:

```bash
python3 pcd.py -r /path/to/src/
```

To ignore subdirectories, pass them to `--ignore` as a comma-separated list:

```bash
python3 pcd.py -r -i /path/to/src/subdir1,/path/to/src/subdir2 /path/to/source
```

## Supported Platforms

- Windows
- OS X
- Linux