from random import randrange

def check_primo(x):
    counter = 0
    for i in range(1,x+1):
        if x % i == 0: counter+=1
    return counter==2 
       
def check_multi(num):
    return num % 5 ==0

for i in range(100):
    n = randrange(10, 200)
    if check_multi(n):
        print(" [", n ,"]", end='')
    if check_primo(n):
        print(" #", n,"#", end='')


