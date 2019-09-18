from functools import reduce
import numpy as np

def prob(po, pc, pco):
    probs = []
    for i in range(pc.shape[0]):
        probs.append([(1 - pco[i]) / (1 - pc[i]), pco[i]/pc[i], 1])
    probs = np.array(probs)
    print(probs)

    active = np.zeros(pc.shape[0]).astype('uint8')

    names = np.array(["-", "+", "?"])

    for i in range(3 ** pc.shape[0]):
        #Get Probabilities
        px = po
        for i in range(active.shape[0]):
            px = px * probs[i][active[i]]
        print(names[active], ":\t", round(px*100, 2), "%")

        #Increment Active
        active[0] = active[0] + 1
        for i in range(1, active.shape[0]):
            if active[i-1] == 3:
                active[i-1] = 0
                active[i] = active[i] + 1



print("How many conditions?")
num = int(input())

print("P(outcome) = ", end = '')
rpo = float(input())
rpc = []
rpco = []



for i in range(num):
    print("P(condition "+str(i+1)+") = ", end = '')
    rpc.append(float(input()))

    print("P(condition "+str(i+1)+" | outcome) = ", end = '')
    rpco.append(float(input()))

rpoc = prob(np.array(rpo), np.array(rpc), np.array(rpco))
