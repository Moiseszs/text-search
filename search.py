import sys
import re
from modules import locate
from modules import _file_ as f

# def find_only_one(file, word):

#     with open(file) as f:
#         lines = f.readlines()
#         found = False
#         counter = 1

#         for line in lines:
#             if re.search(r'\b' + word + r'\b', line):
#                 word.strip()
#                 print("Found ", word, "in", "{", line.strip(), "}", counter)
#                 found = True

#             counter = counter + 1

#         if not found:
#             print("Could not find")

#     # DEPRECATED




def help():
    print("Commands: ")
    print('   -o   Search one string \n   -e   Search for one exactly string')


     

def main():
    args = sys.argv
    file_target = _file_.get_file(args)

    if(args[1] == '-o'):
        if(args[2] == '-e'):
          locate.search_one_exact(file_target,args[3])  
        else:
            locate.search_one_generic(file_target, args[2])

    elif(args[1] == '-h'):
        help()

    elif(args[1] == '-m'):
        elements = _file_.get_elements(args)
        locate.search_many_generic(file_target, elements)

    elif(args[1] == '-b'):
        file = _file_.get_file(args)
        print(file)

main()