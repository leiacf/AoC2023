class Module:

    def __init__(self, name, typ, outputs):
        self.name = name
        self.type = typ
        self.outputs = [outputs]
        self.inputs = []

    def __str__(self):

        out = f"{self.name} | {self.type} | "
        for i in self.inputs:
            out += i.name + " "

        out += "| "

        if self.outputs != [None]:
            for o in self.outputs:
                out += o.name + " "

        out += "|"

        return out
    
    def setInput(self, module):
        self.inputs.append(module)

    def get(self, pulse, fro):
        return pulse, self.outputs        

class Flip(Module):

    def __init__(self, name, typ, outputs):
        Module.__init__(self, name, typ, outputs)
        self.state = 0

    def get(self, pulse, fro):
        return self.flip(pulse)

    def flip(self, pulse):

        if pulse == 1:
            return None, None
        
        else:

            if self.state == 0:
                self.state = 1
                return 1, self.outputs
            elif self.state == 1:
                self.state = 0
                return 0, self.outputs
        
class Con(Module):

    def __init__(self, name, typ, outputs):
        Module.__init__(self, name, typ, outputs)
        self.recent = {}

    def get(self, pulse, fro):

        self.updateInput(fro, pulse)

        if all(val == 1 for val in self.recent.values()):
            return 0, self.outputs
        else:
            return 1, self.outputs

    def updateInput(self, module, pulse):
        self.recent[module] = pulse

    def initInputs(self):
        for input in self.inputs:
            self.recent[input] = 0