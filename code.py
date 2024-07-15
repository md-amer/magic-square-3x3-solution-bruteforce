import itertools
import time

t1=time.time()

poss = []

def gen_poss():
    global poss
    poss = list(itertools.permutations([1,2,3,4,5,6,7,8,9]))

    for i in range(len(poss)):
        poss[i]=list(poss[i])

#Sums

#Rows
r1=[]
r2=[]
r3=[]

#Columns
c1=[]
c2=[]
c3=[]

#Diagonals
#Top-left to bottom-right
d1=[]

#Top-right to bottom-left
d2=[]

def cal_r1(grid):
    return grid[0]+grid[1]+grid[2]

def cal_r2(grid):
    return grid[3]+grid[4]+grid[5]

def cal_r3(grid):
    return grid[6]+grid[7]+grid[8]

def cal_c1(grid):
    return grid[0]+grid[3]+grid[6]

def cal_c2(grid):
    return grid[1]+grid[4]+grid[7]

def cal_c3(grid):
    return grid[2]+grid[5]+grid[8]

def cal_d1(grid):
    return grid[0]+grid[4]+grid[8]

def cal_d2(grid):
    return grid[2]+grid[4]+grid[6]

def cal_all():
    for i in range(len(poss)):
        r1.append(cal_r1(poss[i]))
        r2.append(cal_r2(poss[i]))
        r3.append(cal_r3(poss[i]))
        c1.append(cal_c1(poss[i]))
        c2.append(cal_c2(poss[i]))
        c3.append(cal_c3(poss[i]))
        d1.append(cal_d1(poss[i]))
        d2.append(cal_d2(poss[i]))              

correct=[]
sums=[]

def check_correct(i):
    if r1[i]==r2[i]==r3[i]==c1[i]==c2[i]==c3[i]==d1[i]==d2[i]:
        return True
    else:
        return False

def check_add_all():
    for i in range(len(poss)):
        if check_correct(i):
            correct.append(poss[i])
            sums.append(r1[i])

def save_correct():
    file=open("correct.txt","w")
    for i in correct:
        file.write(str(i)+'\n')
    file.close()

def save_data():
    save_correct()

gen_poss()
cal_all()
check_add_all()
save_data()

t2=time.time()
dur=t2-t1
print(dur)

print(len(poss))
