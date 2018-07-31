"""
#15
Facebook

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

"""

import random
from datetime import datetime

class Stream:

    def __init__(self):
        self.pseudoStream = [random.randint(-10000, 10000)]*10000000+[None]

    def nextSample(self):
        return random.choice(self.pseudoStream)

def selectSample():

    sampleCount = 1

    stream = Stream()

    selectedSample = stream.nextSample()
    maxProbability = random.random()

    while True:
        currentSample = stream.nextSample()
        
        if currentSample == None:
            print("Received", sampleCount, "samples.")
            return selectedSample

        sampleCount += 1

        currentProbability = random.random()

        if currentProbability > maxProbability:
            selectedSample = currentSample
            maxProbability = currentProbability
        

if __name__ == "__main__":
    
    startTime = datetime.now()

    print("Chosen sample:", selectSample() )

    stopTime = datetime.now()

    print("Time elapsed: ", stopTime-startTime)