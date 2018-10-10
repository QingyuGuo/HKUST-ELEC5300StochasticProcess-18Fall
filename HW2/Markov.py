import numpy as np

'''
Write a program (with any language) to generate a sequence from t = 1 to 200. 
Assume the generator generates 1 at t = 0. 
The state transition probabilities of the Markov process are given below.
p(1 | 1) = 0.7 p(-1|1) = 0.3
p(1| -1) = 0.6 p(-1|-1) = 0.4
(a) Print out your sequence 
(a) Suppose we randomly select a time between t = 1 and 200. What is the probability that we find X(t) = 1? 
(b) Let R(s) represents the auto-correlation function of this discrete-time random sequence. Compute R(1) and R(2) 
(note that the sequence represents a power-type signal).
'''

#define states
states = [1, -1]
#define transition sequence
transitionName = [['11', '1-1'], ['-11', '-1-1']]
#define transition matrix
transitionMatrix = [[0.7, 0.3], [0.6, 0.4]]
#define start state
stateStart = 1
#define state list
stateList = [stateStart]
stateDictionary = {1: 0, -1: 0}

# A function that implements the Markov model
def markovModel(days):
    global stateStart
    global stateList
    stateCurrent = stateStart
    countDays = 1
    for t in range(days):
        for i in range(len(states)):
            if stateCurrent == states[i]:
                change = np.random.choice(transitionName[i], replace=True, p=transitionMatrix[i])
                for j in range(len(states)):
                    if change == transitionName[i][j]:
                        stateCurrent = states[j]
                        stateList.append(stateCurrent)
                        # print('t = ', str(countDays)+':')
                        # print(stateList)
                        #this line is used to debug
                        # print(countDays, ':', change, '\n', stateList, len(stateList))
                        break
                break
        countDays += 1
    return countDays - 1


num = markovModel(200)
#to see whether the function goes well
# print(num)

# print(stateList)
# print(len

#to print out the sequence from t=1
sequenceList = stateList[1:]

for element in sequenceList:
    stateDictionary[element] = stateDictionary.get(element, 0) + 1


posFrequency = stateDictionary[1] / (stateDictionary[1] + stateDictionary[-1])
negFrequency = stateDictionary[-1] / (stateDictionary[1] + stateDictionary[-1])

#calculate R(i)
def calculate_R(list, i):
    temp_cal_r = 0
    for t in range(i, len(list)):
        temp_cal_r += list[t] * list[t - i]
    return temp_cal_r/(len(list) - i)


print(sequenceList)
print(stateDictionary)
print('p(1)=', posFrequency, 'p(-1)=', negFrequency)
print('R(1)=', calculate_R(sequenceList, 1))
print('R(2)=', calculate_R(sequenceList, 2))