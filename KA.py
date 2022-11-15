import random
class Cell_auto:
    def __init__(self,height,width,life):
        self.height = height
        self.width = width
        self.field_0 = [[0]*self.width for i in range(self.height)]
        self.life_num = self.height * self.width * life

    def Initialize(self):
        while self.life_num > 0:
            self.x = random.randrange(1,self.width-1)
            self.y = random.randrange(1,self.height-1)
            if self.field_0[self.y][self.x] == 1:
                continue
            else:
                self.field_0[self.y][self.x] = 1
                self.life_num -= 1

    def Copy_Field(self):
        self.bufer_field = [[0]*self.width for i in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                self.bufer_field[y][x]=self.field_0[y][x]

    def Update(self):
        for y in range(1,self.height-1):
            for x in range(1,self.width-1):
                life = 0
                for i in range(y-1,y+2): 
                    for j in range(x-1,x+2):
                        if y == i and x == j:
                            continue
                        elif self.field_0[i][j] == 1:
                            life += 1
                if life == 3:
                    self.bufer_field[y][x] = 1
                elif life < 2 or life > 3:
                    self.bufer_field[y][x] = 0
        for y in range(self.height):
            for x in range(self.width):
                self.field_0[y][x] = self.bufer_field[y][x]
    
def Print(ca):
    for y in range(ca.height):
        for x in range(ca.width):
            print(ca.field_0[y][x], end=' ')
        print()
    print()

def main():
    ca = Cell_auto(10,10,0.15)
    ca.Initialize()
    while True:
        Print(ca)
        ca.Copy_Field()
        ca.Update()
        input()
main()
                    


