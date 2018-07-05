#!/usr/bin/env python3

import argparse
from os import walk
from os import path
from sys import exit

def dir_is_subdir(curdir, dirs):
    for d in dirs:
        if d in curdir:
            return True
    return False

parser = argparse.ArgumentParser(description='PHP4 Constructor Detector')
parser.add_argument('-r', '-R', '--recursive', action='store_true', help='Recursively scan directory')
parser.add_argument('-i', '--ignore', help='Directories to ignore')
parser.add_argument('dir', help='Directory to scan')

args = parser.parse_args()

if not path.isdir(args.dir):
    print('%s is not a valid directory' % args.dir)
    exit()

args.ignore = args.ignore.strip(' \t\n\r\\/').split(',') if args.ignore else []

files_using_php4_constructors = []

for (dirpath, dirnames, filenames) in walk(args.dir):
    if dir_is_subdir(dirpath, args.ignore):
        continue
    print('\nScanning directory: %s' % dirpath)
    for fl in filenames:
        if not '.php' in fl:
            continue
        try:
            with open(dirpath + '\\' + fl) as f:
                class_name = ''
                for line in f:
                    l = line.strip()
                    if l.startswith('class '):
                        class_name = l.replace('class ', '')
                        class_name = class_name[:class_name.find(' ')]
                    elif class_name and l.startswith('function '):
                        function_name = l.replace('function ', '')
                        function_name = function_name[:function_name.find('(')]
                        if function_name == class_name:
                            files_using_php4_constructors.append(dirpath + '\\' + fl)
        except FileNotFoundError:
            print('Could not find file %s. Skipping...' % (dirpath + '\\' + fl))
        except UnicodeDecodeError:
            continue
    if not args.recursive:
        break

print('\n\nFiles using PHP4 constructors')
print('-----------------------------')

if not files_using_php4_constructors:
    print('None')
else:
    for f in set(files_using_php4_constructors):
        print(f)