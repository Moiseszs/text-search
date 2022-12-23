import sys
import re

def find_only_one(file, word):

    with open(file) as f:
        lines = f.readlines()
        found = False
        counter = 1

        for line in lines:
            if re.search(r'\b' + word + r'\b', line):
                word.strip()
                print("Found ", word, "in", "{", line.strip(), "}", counter)
                found = True

            counter = counter + 1

        if not found:
            print("Could not find")

    # DEPRECATED


                
def open_file(file):
    lines = []

    with open(file) as f:
        lines = f.readlines()

    return lines


def search_one_generic(file, word):
    lines = open_file(file)
    found = False
    counter = 1

    for line in lines:
        if word in line:
            print("Found ", word, "in", "{", line.strip(), "}", counter)
            found = True
    counter = counter +  1

    if not found:
        print("not found")



def search_one_exact(file, word):
    lines = open_file(file)
    found = False
    counter = 1

    for line in lines:
        if re.search(r'\b' + word + r'\b', line):
            print("Found ", word, "in", "{", line.strip(), "}", counter)
            found = True
        counter = counter +  1

    if not found:
        print("not found")


def search_many_generic(file,word):
    pass



def help():
    print("Commands: ")
    print('   -o   Search one string \n   -e   Search for one exactly string')


def get_elements(args):
    elements = []

    for arg in args[2: args.index("-f")]:
        elements.append(arg)

    return elements

def main():
    args = sys.argv

    if(args[1] == '-o'):
        if(args[2] == '-e'):
          search_one_exact(args[5],args[3])  
        else:
            search_one_generic(args[3], args[2])

    elif(args[1] == '-h'):
        help()

    elif(args[1] == '-m'):
        elements = get_elements(args)
        search_many_generic(file, elements)

main()