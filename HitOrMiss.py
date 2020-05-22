import random
import operator as op
from functools import reduce
import matplotlib.pyplot as plt

def hitOrMiss(shots, hit_shots, hit, miss):
    comb_perc = combination(shots, hit_shots)
    hit_perc  = (hit)**(hit_shots)
    miss_perc = (miss)**(shots - hit_shots)

    calc = comb_perc * hit_perc * miss_perc
    return calc
    
def combination(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer / denom       

def pie_chart(sample):
    labels = 'Hit', 'Miss'
    hit = sample * 100
    miss = 100 - hit 
    sizes = [hit, miss]
    if hit > miss:
        explode = (0.1, 0)
    elif hit < miss:
        explode = (0, 0.1)
    else:
        explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig("hit_or_miss.png")


if __name__ == "__main__":
    result = hitOrMiss(shots=3, hit_shots=3, hit=0.6, miss=0.4)
    pie_chart(result1)

    with open('hitormiss.txt', 'w+') as f:
       f.write(str(result))    
    
