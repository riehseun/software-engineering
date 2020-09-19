# python3
import sys


def compute_min_refills(distance, tank, stops):
    """
	Solves classical Car fueling problem using greedy algorithm

    Args:
    distance -- total distance to travel
    tank -- distance that the car can travel w/o fueling
    stops -- array representing the location of gas stations

    Returns:
    num_refills -- the mimimum number of refills required
    """

    num_refills = 0
    current_refill = 0

    all_stops = []
    all_stops.append(0)
    for stop in stops:
    	all_stops.append(stop)
    all_stops.append(distance)

    num_stops = len(all_stops)

    while current_refill < num_stops:
    	last_refill = current_refill

    	while (current_refill < num_stops and all_stops[current_refill+1] - all_stops[last_refill] <= tank):
    		current_refill += 1
    		if current_refill == num_stops-1:
    			return num_refills

    	if current_refill == last_refill:
    		return -1
    	if current_refill < num_stops:
    		num_refills += 1

    return num_refills


print(compute_min_refills(950, 400, [200, 375, 550, 750]))
print(compute_min_refills(10, 3, [1, 2, 5, 9]))