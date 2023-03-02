from search import *
# YOUR CODE GOES HERE
class WolfGoatCabbage(Problem):

  def __init__(self, initial=('F','G','W','C'), goal=()):
    #initializes WolfGoatCabbage inheriting from Problem with initial state and goal specified
    super().__init__(initial, goal)

  def goal_test(self, state):
    #returns true or false if given state is the goal state
    return state == self.goal
  
  def result(self, state, action):
    result_state = list(state)
    #for each item in given action, change state to reflect changes requested
    for item in action:
      #because not existing in state means it is on the other side of the river state observes, we remove to indicate the item has moved to the side we are not observing or adding to indicate the item has moved to the side we are observing
      result_state.remove(item) if item in state else result_state.append(item)
    result_state = tuple(result_state)
    #returns the new state after actions are taken
    return result_state

  def actions(self, state):
    possible_actions = ()
    sorted_state = tuple(sorted(state))
    #check what the current states are and select the possible actions allowed
    if sorted_state == ('C', 'F', 'G', 'W'):
      possible_actions = ({'F', 'G'},)
    elif sorted_state == ('C', 'F', 'G') or sorted_state == ('W',):
      possible_actions = ({'C', 'F'}, {'F', 'G'})
    elif sorted_state == ('C', 'F', 'W') or sorted_state == ('G',):
      possible_actions = ({'C', 'F'}, {'F', 'W'}, {'F'})
    elif sorted_state == ('C', 'G', 'W') or sorted_state == ('F',):
      possible_actions = ({'F'},)
    elif sorted_state == ('F', 'G', 'W') or sorted_state == ('C',):
      possible_actions = ({'F', 'G'}, {'F', 'W'})
    elif sorted_state == ('F', 'G') or sorted_state == ('C', 'W'):
      possible_actions = ({'F', 'G'}, {'F'})
    return possible_actions

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)