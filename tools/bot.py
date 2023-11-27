class Bot():

    def __init__(self, instructions):

        self.number = int(instructions[0].split(" ")[1])
        self.lowdirection = instructions[1]
        self.highdirection = instructions[2]
        self.low = -1
        self.high = -1

    def __str__(self):

        return "Bot number: {} ! Gives low to {} and high to {} ! Contains chips: {} and {}".format(self.number, self.lowdirection, self.highdirection, self.low, self.high)

    def getChip(self, chip):
        
        if self.low == -1:
            self.low = chip

        elif self.high == -1:
            self.high = chip

        else:
            exit("Error: Bot can only have two chips")

        if self.high < self.low:
            temp = self.high
            self.high = self.low
            self.low = temp

    def hasChips(self):
        return (self.low != -1 and self.high != -1)
    
    def removeChip(self, chip):

        if self.high == chip:
            self.high = -1

        elif self.low == chip:
            self.low = -1

        else:
            exit("Error: Bot does not have that chip!")

    def followRules(self, bots, search1, search2):

        return -1
