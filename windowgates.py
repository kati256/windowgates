#!/usr/bin/python3
'''
Author: kati256
Email: katithebizz (at) gmail.com

This is a script to auto generate ascii windows for whatever reason
one has.

Usage:
windowgates -f <filename>
This will take the contents of the file as the window contents and print
a window to stdout with the file's contents
'''

import sys

class WindowFrame:
    '''
    The purpose of this class is to hold the data used in generating the frames
    using these three methods it's easy to make different frames, which I might or
    might not do at some point.

    All methods except init (for obvious reasons) return the string piece
    of the frame.
    '''
    def __init__(self, name, width):
        self.name = name
        if width > 5 + len(name):
            self.width = width
        else:
            self.width = 5 + len(name)

    def body(self, line):
        '''
        @param line: the line to be used in the body.
        '''
        return '│ ' + line + ' │\n'

    def header(self):
        res = '┌' + '─' * (self.width + 2) + '┐\n'
        res += '│ {}'.format(self.name) + ' ' * (self.width - len(self.name) - 5)
        res += 'o o o │\n'
        res += '├' + '─' * (self.width + 2) + '┤\n'
        return res

    def footer(self):
        return '└' + '─' * (self.width + 2) + '┘\n'

def enframe(matrix, name):
    '''
    @param matrix: string array where all strings are of N length.
    @returns: string with the framed matrix within it.
    '''
    frame_height = len(matrix)
    if frame_height == 0:
        return ''
    frame_width = len(matrix[0])
    frame = WindowFrame(name, frame_width)
    result = ''
    result += frame.header()
    for i in range(frame_height):
        result += frame.body(matrix[i])
    result += frame.footer()
    return result

def makeWindow(contents, name):
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
    result = enframe(matrix, name)
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

    makeWindow(text, filename)

if __name__ == '__main__':
    main()
