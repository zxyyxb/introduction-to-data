from collections import deque

def is_valid_state(state):
    F, W, G, C = state
    # 如果狼和羊在一起，而农夫不在，狼会吃羊
    if W == G and F != W:
        return False
    # 如果羊和菜在一起，而农夫不在，羊会吃菜
    if G == C and F != G:
        return False
    return True

def get_next_states(state):
    F, W, G, C = state
    # 所有可能的移动方式
    moves = [W, G, C, F]
    next_states = []

    for move in moves:
        if F == move:  # 如果农夫和要移动的物品在同一边
            new_state = tuple([1 - F if x == F or x == move else x for x in state])
            if is_valid_state(new_state):
                next_states.append(new_state)

    return next_states

def farmer_river_problem():
    start = (0, 0, 0, 0)  # 所有物品都在河的这一边
    end = (1, 1, 1, 1)   # 所有物品都需要到达河的另一边

    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()
        if state == end:
            return path + [end]

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None

solution = farmer_river_problem()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found!")
