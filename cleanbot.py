#posr, posc, board
#find all "d" spots on board, clean them. 

def next_move(posr, posc, board):
	
	#find all dirty spots
	#naive, find closest, go straight there. 
	#not that naive, let's implement. 

	#find closest dirty spot
	#search outwards for "d"
	#reconstruct path


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)