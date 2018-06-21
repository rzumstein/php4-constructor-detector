#!/usr/bin/env python3

import sys
from os import walk

try:
    print('Scanning directory: %s' % sys.argv[1])
except IndexError:
    sys.exit('You must provide a directory to search')

files_using_php4_constructors = []

for (dirpath, dirnames, filenames) in walk(sys.argv[1]):
    print('Scanning directory: %s' % dirpath)
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
                        if (function_name == class_name):
                            files_using_php4_constructors.append(dirpath + '\\' + fl)
        except FileNotFoundError:
            print('Could not find file %s. Skipping...' % (dirpath + '\\' + fl))
        except UnicodeDecodeError:
            continue

print('\n\nFiles using PHP4 constructors')
print('-----------------------------')

for f in set(files_using_php4_constructors):
    print(f)
