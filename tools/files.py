def input_as_string(filename):

    f = open(filename, "r")

    return f.read()

def input_as_list(filename):

    f = open(filename, "r")

    return f.read().split("\n")
