import random
class Diffusion_model:
    def __init__(self,pollution,number_of_dye_drops,diffusion_coefficient):
        self.diffusion_coefficient=diffusion_coefficient
        self.width=30
        self.height=20
        self.field=[[0]*self.width for i in range(self.height)]
        
        total_polluted_cells=int(self.height*self.width*pollution/100)
        while number_of_dye_drops>0:
            temp_y=random.randrange(1,self.height-1)
            temp_x=random.randrange(1,self.width-1)
            self.field[temp_y][temp_x]=191
            number_of_dye_drops-=1
        filling_count=0
        while filling_count<total_polluted_cells:
            temp_y=random.randrange(0,self.height)
            temp_x=random.randrange(0,self.width)
            if self.field[temp_y][temp_x]=='x' or int(self.field[temp_y][temp_x])>0:
                continue
            else:
                self.field[temp_y][temp_x]='x'
                filling_count+=1
        
    def update(self):
        for y in range(1,self.height-1):
            for x in range(1,self.width-1):
                if self.field[y][x]!='x':                   
                    for i in range(y-1,y+2):
                        for j in range(x-1,x+2):
                            if i==y and j==x:
                                continue
                            else:
                                if self.field[i][j]!='x':
                                    if int(self.field[i][j])<int(self.field[y][x]):
                                        delta=(self.field[y][x]-self.field[i][j])*self.diffusion_coefficient
                                        self.field[i][j]+=delta
                                        self.field[y][x]-=delta
                                        