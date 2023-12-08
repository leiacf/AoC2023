class Node:

    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):

        string = "Name: {} Children: [".format(self.name)
        for child in self.children:
            string+= str(child.name)
            if len(self.children) > 1:
                string+=", "
        string += "]"
        
        return string