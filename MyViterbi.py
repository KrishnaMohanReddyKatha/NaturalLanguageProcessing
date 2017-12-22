""" Author: Krishna Mohan Reddy Katha
    Implementation of Viterbi Algorithm for the given HMM model
    NLP Fall 2017"""

stateNames = {0:'HOT',1:'COLD'}

def Viterbi(input,stateProb,initialProb,obsProb):
    obsLength = len(input)
    numOfStates = len(initialProb)
    probMatrix = [[0 for x in range(obsLength)] for y in range(numOfStates)]
    backTrackMatrix = [[0 for x in range(obsLength)] for y in range(numOfStates)]

    for i in range(numOfStates):
        probMatrix[i][0] = initialProb[i]*obsProb[i][int(input[0])-1]
        backTrackMatrix[i][0] = 0
    for ob in range(1,obsLength):
        for i in range(numOfStates):
            calculatedValues = [(probMatrix[j][ob-1]*stateProb[j][i]*obsProb[i][int(input[ob])-1],j) for j in range(numOfStates)]
            maxCalculatedValues = max(calculatedValues)
            probMatrix[i][ob] = maxCalculatedValues[0]
            backTrackMatrix[i][ob] = maxCalculatedValues[1]
    result = max((probMatrix[i][obsLength - 1], i) for i in range(numOfStates))
    probability = result[0]
    backPtr = result[1]
    result = []

    for ob in range(obsLength-1,-1,-1) :
        result.insert(0,stateNames[backPtr])
        backPtr = backTrackMatrix[backPtr][ob]
    return probability,result

input = raw_input("enter the input sequence : ")
stateProb = [[0.7 ,0.3],[0.4,0.6]]
initialProb = [0.8,0.2]
obsProb = [[0.2,0.4,0.4],[0.5,0.4,0.1]]

print "probability and weather sequence is : "
print Viterbi(input,stateProb,initialProb,obsProb)