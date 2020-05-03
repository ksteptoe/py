# -*- coding: utf-8 -*-
"""
helloworld
:param sys.argv[1:]
:returns: True
:raises: Null

"""
import sys


def main(argv):
    print('hello world')
    print('Yello Brick')

    try:
        if __name__ == "__main__":
            main(sys.argv[1:])
    except SystemExit:
        pass