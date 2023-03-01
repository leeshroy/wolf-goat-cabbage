from search import *
# YOUR CODE GOES HERE
class WolfGoatCabbage(Problem):
  
  def __init__(self, initial=('F','G','W','C'), goal=()):
    super().__init__(initial, goal)

  def goal_test(self, state):
    return state == self.goal
  
  def result(self, state, action):
    for passenger in action:
      if passenger in state:
        state.remove(passenger)
      else:
        state.add(passenger)
    return state

  def actions(self, state):
    possible_actions = []
    sorted_state = sorted(state)
    if sorted_state == ('C', 'F', 'G', 'W'):
      possible_actions = [('F', 'G')]
    elif sorted_state == ('C', 'F', 'G') or sorted_state == ('W'):
      possible_actions = [('C', 'F'), ('F', 'G')]
    elif sorted_state == ('C', 'F', 'W') or sorted_state == ('G'):
      possible_actions = [('C', 'F'), ('F', 'W')]
    elif sorted_state == ('C', 'G', 'W') or sorted_state == ('F'):
      possible_actions = [('F')]
    elif sorted_state == ('F', 'G', 'W') or sorted_state == ('C'):
      possible_actions = [('F', 'G'), ('F', 'W')]
    elif sorted_state == ('F', 'G') or sorted_state == ('C', 'W'):
      possible_actions = [('F', 'G'), ('F')]
    return possible_actions

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)