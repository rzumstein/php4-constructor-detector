# PHP4 Constructor Detector

## Description

Finds PHP classes that use the PHP4 constructor style that is now deprecated in PHP5 when using namespaces, and completely deprecated in PHP7.  Useful for checking if your codebase uses PHP4 constructors when upgrading PHP.

## Use

Clone this repo; or download either `pcd.py` or `pcd.js`.  Run the script by providing a directory to scan for PHP files, e.g.:

To run using Python:

```bash
python3 pcd.py /path/to/src/
```

To run using Node:

```bash
node pcd.js /path/to/src/
```

## Supported Platforms

- Windows
- OS X
- Linux

## Todo

- Allow ignoring (sub)directories
- Allow non-recursive scanning
- Add option to automatically fix php4 constructors
- Show how many violations each file has as opposed to just showing the filename
- Add sanity checking to ensure the user actually passes in a directory as an argument

----

Thanks to: [Matt Meisberger](https://github.com/matthewdaniel) for providing the Node version of this script