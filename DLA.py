import random

class Cell_auto:
    def __init__(self, height, width, life):
        self.height = height
        self.width = width
        self.field_0 = [[0] * self.width for i in range(self.height)]
        self.life_num = life

    def Initialize(self):
        while self.life_num > 0:
            self.x = random.randint(1, self.width - 1)
            self.y = random.randint(1, self.height - 1)
            if self.field_0[self.y][self.x] == 1:
                continue
            else:
                self.field_0[self.y][self.x] = 1
                self.life_num -= 1

    def Copy_Field(self):
        self.bufer_field = [[0] * self.width for i in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                self.bufer_field[y][x] = self.field_0[y][x]

    def Update(self):
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                life = 0
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
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

class DLA(Cell_auto):
    def Place_particle(self):
        self.x = random.randint(1, self.width - 1)
        self.y = random.randint(1, self.height - 1)
        while self.field_0[self.y][self.x] == 2:
            self.x = random.randint(1, self.width - 1)
            self.y = random.randint(1, self.height - 1)
        self.field_0[self.y][self.x] = 1

    def Update(self):
        center_counter = 1
        moving = True
        moving_x = 0
        moving_y = 0
        while moving:
            while (self.x - 1 < 0) or (self.x + 1 > self.width-1) or (self.y - 1 < 0) or (self.y + 1 > self.height-1):
                self.field_0[self.y][self.x] = 0
                self.Place_particle()
            if self.field_0[self.y][self.x+1] == 2 or self.field_0[self.y-1][self.x] == 2 or self.field_0[self.y][self.x-1] == 2 or self.field_0[self.y+1][self.x] == 2:
                self.field_0[self.y][self.x] = 2
                center_counter += 1
                self.Place_particle()
            direction = random.randint(0,1)
            if direction == 0:
                moving_x = random.randint(-1,1)
            else:
                moving_y = random.randint(-1,1)
            while (self.x + moving_x < 0) or (self.x + moving_x > self.width-1) or (self.y + moving_y < 0) or (self.y + moving_y > self.height-1):
                self.field_0[self.y][self.x] = 0
                self.Place_particle()
            self.field_0[self.y][self.x] = 0
            self.x += moving_x
            self.y += moving_y
            self.field_0[self.y][self.x] = 1
            current_porosity = (center_counter / (self.width * self.height)) * 100
            if current_porosity >= self.life_num:
                moving = False
            self.Print()

    def Initialize(self):
        self.field_0[int(self.height/2)][int(self.width/2)] = 2
        self.Place_particle()
        self.Print()

    def Print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.field_0[y][x], end=' ')
            print()
        print()
        input()

def main():
    ca = DLA(7, 7, 50)
    ca.Initialize()
    ca.Update()
    print('Цель достигнута')
main()