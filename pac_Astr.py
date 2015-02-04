import heapq as hq

def Astar(pac, food, r, c):
	#node implemented as (x, y)
	#sorted list with (priority, node)
	#priority = dist_traveled (inc by 1) + manhattan_dist(node, food)
	#f(node)

	#push starting position and initial cost
	fronter = [(pac, 0)]
	hq.heapify(frontier)

	while not frontier.empty():
		#take first thing from priority queue, 
		if pac == food:
			return#reconstruct this path



def manhattan_dist(node, food):
    r1,c1 = node
    r2,c2 = food
    return (abs(r1-r2) + abs(c1-c2))


if __name__ == "__main__":
	print manhattan_dist((35,35),(35,1))