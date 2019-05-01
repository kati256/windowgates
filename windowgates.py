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

def enframe(matrix):
    '''
    @param matrix: string array where all strings are of N length.
    @returns: string with the framed matrix within it.
    '''
    frame_height = len(matrix)
    if frame_height == 0:
        return ''
    frame_width = len(matrix[0])
    result = ''
    result += '+' + '-' * frame_width + '+\n'
    for i in range(frame_height):
        result += '|' + matrix[i] + '|\n'
    result += '+' + '-' * frame_width + '+\n'
    return result

def makeWindow(contents):
    '''
    @param contents: string with the full content of the window.
    '''
    matrix = contents.split('\n')
    width = 0
    height = len(matrix)
    for line in matrix:
        width = max(width, len(line))
    for i, line in enumerate(matrix):
        matrix[i] += ' '*(width-len(line))
    result = enframe(matrix)
    print(result)

def main():
    args = sys.argv
    if len(args) < 3 or args[1] != '-f':
        print('Please give an input file with -f <filename>')
        sys.exit(-1)

    filename = ' '.join(args[2:])
    try:
        inputFile = open(filename, 'r')
        text = inputFile.read()
        inputFile.close()
    except IOError as e:
        print('Error: Failed to open file {}. {}'.format(filename, e))
        sys.exit(-1)
    except Exception as e:
        print('Error: Unknown error {}'.format(e))
        sys.exit(-1)

    makeWindow(text)

if __name__ == '__main__':
    main()
