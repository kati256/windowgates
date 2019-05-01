#!/usr/bin/python3
'''
This is a script to auto generate ascii windows for whatever reason
one has.

Usage:
windowgates -f <filename>
This will take the contents of the file as the window contents and print
a window to stdout with the file's contents
'''

import sys

def main():
    args = sys.argv
    if len(args) < 3 or args[1] != '-f':
        print('Please give an input file with -f <filename>')
        sys.exit(-1)

    filename = ' '.join(args[2:])
    try:
        inputFile = open(filename, 'r')
        text = inputFile.read()
    except IOError as e:
        print('Error: Failed to open file {}. {}'.format(filename, e))
        sys.exit(-1)
    except e:
        print('Error: Unknown error {}'.format(e))
        sys.exit(-1)
    finally:
        inputFile.close()

    print(text)

if __name__ == '__main__':
    main()
