import time

coinValues = [1,2,5,10,20,50,100,200]

#give back 0p : 1 solution 0p -> ways[0] = 1
#give back 1p : 1 soulution 1p -> ways[1] = 1
#give back 2p: 2 solutions 1p(ways[1]) + 2p -> ways[2] = 2

possibilities = [0]*(200+1)
possibilities[0] = 1 #i can split 0p only one way

for i in range(len(coinValues)):
    for j in range(coinValues[i],201):
        print(i,j)
        possibilities[j] += possibilities[j-coinValues[i]]

print(possibilities[200])
