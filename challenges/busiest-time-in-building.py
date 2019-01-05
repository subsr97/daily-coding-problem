"""
#171
Amazon

You are given a list of data entries that represent entries and exits of groups of people into a building. 

An entry looks like this:
{"timestamp": 1526579928, count: 3, "type": "enter"}
This means 3 people entered the building.

An exit looks like this:
{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

Test case generated using: https://gist.github.com/subsr97/013f0ec962ebc2f30f26e2ea73c2a4f7
Entry Count: 10
Entries:
[
    {'timestamp': 1546711314, 'count': 1, 'type': 'enter'}, 
    {'timestamp': 1546711379, 'count': 3, 'type': 'enter'}, 
    {'timestamp': 1546711496, 'count': 1, 'type': 'exit'}, 
    {'timestamp': 1546711578, 'count': 1, 'type': 'exit'}, 
    {'timestamp': 1546711673, 'count': 3, 'type': 'enter'}, 
    {'timestamp': 1546711755, 'count': 5, 'type': 'enter'}, 
    {'timestamp': 1546711764, 'count': 5, 'type': 'exit'}, 
    {'timestamp': 1546711778, 'count': 3, 'type': 'exit'}, 
    {'timestamp': 1546711799, 'count': 3, 'type': 'enter'}, 
    {'timestamp': 1546711851, 'count': 5, 'type': 'exit'}
]
People List: [0, 1, 4, 3, 2, 5, 10, 5, 2, 5, 0]
Answer: (1546711755, 1546711764)
"""

def busiestTime(entries):
    currentPopulation = 0
    maxPopulation = 0
    previousTimestamp = 0
    currentTimestamp = 0
    maxPopulationTimestamp = (0, 0)

    for entry in entries:
    
        previousTimestamp = currentTimestamp
        currentTimestamp = entry["timestamp"]

        if currentPopulation > maxPopulation:
            maxPopulation = currentPopulation
            maxPopulationTimestamp = (previousTimestamp, currentTimestamp)
        
        if entry ["type"] == "enter":
            currentPopulation += entry["count"]
        else:
            currentPopulation -= entry["count"]
        

    
    return maxPopulationTimestamp
        

def main():
    entries = [
        {'timestamp': 1546711314, 'count': 1, 'type': 'enter'}, 
        {'timestamp': 1546711379, 'count': 3, 'type': 'enter'}, 
        {'timestamp': 1546711496, 'count': 1, 'type': 'exit'}, 
        {'timestamp': 1546711578, 'count': 1, 'type': 'exit'}, 
        {'timestamp': 1546711673, 'count': 3, 'type': 'enter'}, 
        {'timestamp': 1546711755, 'count': 5, 'type': 'enter'}, 
        {'timestamp': 1546711764, 'count': 5, 'type': 'exit'}, 
        {'timestamp': 1546711778, 'count': 3, 'type': 'exit'}, 
        {'timestamp': 1546711799, 'count': 3, 'type': 'enter'}, 
        {'timestamp': 1546711851, 'count': 5, 'type': 'exit'}
    ]

    print(busiestTime(entries))

if __name__ == "__main__":
    main()