import modules._file_ as f

def search_one_generic(file, word):
    lines = f.open_file(file)
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
    lines = f.open_file(file)
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