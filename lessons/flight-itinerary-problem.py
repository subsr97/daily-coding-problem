"""
The flight itinerary problem is as follows:

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, 
and a starting airport, compute the person's itinerary. 

If no such itinerary exists, return null. All flights must be used in the itinerary.

For example, given the following list of flights:
    HNL ➔ AKL
    YUL ➔ ORD
    ORD ➔ SFO
    SFO ➔ HNL

and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL. 

"""

def getItinerary(flights, currentItinerary):
    if not flights:
        return currentItinerary
    
    lastStop = currentItinerary[-1]

    for i, (source, dest) in enumerate(flights):
        flightsMinusCurrent = flights[:i] + flights[i+1:]
        currentItinerary.append(dest)

        if source == lastStop:
            return getItinerary(flightsMinusCurrent, currentItinerary)
        
        currentItinerary.pop()

    return None

if __name__ == "__main__":
    flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
    source = "YUL"

    print(" -> ".join(getItinerary(flights, [source])))