from functools import reduce

class Card():
    def __init__(self, spaces=None, marked=None) -> None:
        # Represent spaces on the card
        if spaces:
            self.spaces = spaces
        else:
            self.spaces = [
                [0] * 5,
                [0] * 5,
                [0] * 5,
                [0] * 5,
                [0] * 5,
            ]
        # Mask to represent spaces marked on the card
        if marked:
            self.marked = marked
        else:
            self.marked = [
                [False] * 5,
                [False] * 5,
                [False] * 5,
                [False] * 5,
                [False] * 5,
            ]

    def check_vert(self):
        for row in self.marked:
            if reduce(lambda a, b: a and b, row):
                return True
        return False

    def check_horiz(self):
        for i in range(5):
            col = [self.marked[x][i] for x in range(5)]
            if reduce(lambda a, b: a and b, col):
                return True
        return False

    def sum_unmarked(self):
        sum = 0
        for i, line in enumerate(self.spaces):
            for j, item in enumerate(line):
                if not self.marked[i][j]:
                    sum+=item
        return sum

    def check_win(self):
        horiz = self.check_horiz()
        vert = self.check_vert()
        return horiz or vert
    
    def call(self, num):
        for i, line in enumerate(self.spaces):
            for j, item in enumerate(line):
                if item == num:
                    self.marked[i][j] = True
        if self.check_win():
            return self.sum_unmarked() * num
    
    def __str__(self) -> str:
        repr = str(self.spaces)
        return repr

    def __repr__(self) -> str:
        repr = str(self.spaces)
        return repr
    

f = open("input", "r")
calls_str = f.readline().strip().split(",")
calls = [int(x) for x in calls_str]
print(calls)
f.readline()

cards = []
temp = []
for line in f:
    if line.isspace():
        cards = cards + [Card(temp)]
        temp = []
    else:
        str_list = line.strip().split()
        row = [int(x) for x in str_list]
        temp = temp + [row]
# Make sure to take care of last card
cards = cards + [Card(temp)]

for i, card in enumerate(cards):
    for j, call in enumerate(calls):
        result = card.call(call)
        if result:
            print(f"Card {i} won after {j} calls with score {result}")
            break
