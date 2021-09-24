from node import Node

explored_node_list = []
visited_node_list = []

goal_state = [0, 1, 2,
              3, 4, 5,
              6, 7, 8]
goal_node = Node(goal_state, None, depth=0)


goal_is_found = False

def ai_search_dfs(start_node):
    explored_node_list.append(start_node)
    visit(start_node)


def visit(node):
    global goal_is_found
    if goal_is_found:
        return

    print(node)
    visited_node_list.append(node)

    # your code:
    #############your code ################

    # @{node} here is the current node we are handling.
    # in order to clarify, we give it a nickname
    current = node
    if goal_node.equals(current): 
        goal_is_found = True
    for neighbor in current.neighbors():
        if node_is_not_explored(neighbor) & node_is_not_visited(neighbor):
            explored_node_list.append(neighbor)
            visit(neighbor)


    #######################################


def node_is_not_explored(node):
    for explored_node in explored_node_list:
        if node.equals(explored_node):
            return False
    return True

def node_is_not_visited(node):
    for visited_node in visited_node_list:
        if node.equals(visited_node):
            return False
    return True


def main():
    start_state = [1, 4, 2,
                   3, 7, 5,
                   6, 0, 8]
    start_node = Node(start_state, None, depth=0)

    ai_search_dfs(start_node)

    print("visit list:")
    for node in visited_node_list:
        print(node)
        print()

    print("explore list:")
    for node in explored_node_list:
        print(node)
        print()

if __name__ == "__main__":
    main()


