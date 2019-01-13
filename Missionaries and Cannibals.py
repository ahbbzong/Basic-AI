import math

class Node():
	
	def __init__(self, cannibalLeft, missionaryLeft, boatSide, cannibalRight, missionaryRight):
            #initial each states for cannibal and missionary and the states of boats.
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boatSide = boatSide
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None
		#For the initial time, we at root, no parent of root.

	def goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
                    #Set up a state for the goal of the game.
			return True
		else:
			return False

	def valid(self):
		if (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight) and self.missionaryLeft >= 0 and self.missionaryRight >= 0 and self.cannibalLeft >= 0 and self.cannibalRight >= 0:
                    #Set up some states that can happen in the game. 
			return True
		else:
			return False

def operation(current_state):
	array = [];
	#An array to store new states.
	if current_state.boatSide == 'left':
		new_state = Node(current_state.cannibalLeft-2, current_state.missionaryLeft, 'right',current_state.cannibalRight+2, current_state.missionaryRight)
		# move two missinary from left to right
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft, current_state.missionaryLeft-2, 'right',current_state.cannibalRight, current_state.missionaryRight+2)
		# move two cannibals from left to right
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft - 1, current_state.missionaryLeft - 1, 'right',current_state.cannibalRight + 1, current_state.missionaryRight + 1)
		# move one cannibal and one missionary from left to right
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft, current_state.missionaryLeft - 1, 'right',current_state.cannibalRight, current_state.missionaryRight + 1)
		# move one missionary to the right.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft - 1, current_state.missionaryLeft, 'right',current_state.cannibalRight + 1, current_state.missionaryRight)
		# Move one cannibal to the right.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
	else:
		new_state = Node(current_state.cannibalLeft+2, current_state.missionaryLeft, 'left',current_state.cannibalRight-2, current_state.missionaryRight)
		# Move two missionarys from right to left.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft, current_state.missionaryLeft+2, 'left',current_state.cannibalRight, current_state.missionaryRight-2)
		#move two cannibals cross left.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft + 1, current_state.missionaryLeft + 1, 'left',current_state.cannibalRight - 1, current_state.missionaryRight - 1)
		#move one missionary and one cannibal from right to left.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft, current_state.missionaryLeft + 1, 'left',current_state.cannibalRight, current_state.missionaryRight - 1)
		#Move one missionary to left.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
		new_state = Node(current_state.cannibalLeft + 1, current_state.missionaryLeft, 'left',current_state.cannibalRight - 1, current_state.missionaryRight)
		#Move one cannibal to left.
		if new_state.valid():
			new_state.parent = current_state
			array.append(new_state)
			#Store the new state to array.
	return array

def BFS():
    #Do a Breath first search to find the result of the problem.
	initial_state = Node(3,3,'left',0,0)
	#Set up the start state. 
	white = list()
	grey = set()
	#Set up a list and a set. White means the node that haven't been visited yet.
	#Grey means the nodes that already been explored.
	white.append(initial_state)
	while white:
		state = white.pop(0)
		#Go through all the node until we find the goal
		if state.goal():
			return state
		grey.add(state)
		array = operation(state)
		for i in array:
			if (i not in grey) or (i not in white):
				white.append(i)
	return None

def main():
    solution = BFS()
    #Call the BFS to slove the problem
    route = []
    route.append(solution)
    parent = solution.parent
    while parent:
        route.append(parent)
        parent = parent.parent

    for i in range(len(route)):
        place = route[len(route) - i - 1]
        print ("step "+str(i+1)+"["+str(place.cannibalLeft) + "," + str(place.missionaryLeft) + "," + str(place.cannibalRight) + "," + str(place.missionaryRight) +","+ place.boatSide + "]")
        # Print the result out. 

if __name__ == "__main__":
        #run under main
    main()
