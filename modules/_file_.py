import sys


def get_elements(args):
    elements = []

    for arg in args[2: args.index("-f")]:
        elements.append(arg)

    return elements


def get_file(args):
    sys.tracebacklimit = 0

    file = ''

    if '-f' in args:
        file = args[args.index('-f')+1]

    else:
        raise Exception("Not found")

    try:
        opn = open(file)
    except IOError:
        raise Exception("None")

    return file
    

def open_file(file):
    lines = []

    with open(file) as f:
        lines = f.readlines()

    return lines