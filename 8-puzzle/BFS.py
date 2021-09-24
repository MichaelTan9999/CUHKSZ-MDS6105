from collections import deque
from node import Node


frontier_node_queue = deque()
explored_node_list = []
visited_node_list = []

def ai_search_bfs(start_node, goal_node):

    frontier_node_queue.appendleft(start_node)
    explored_node_list.append(start_node)

    while frontier_node_queue:
        # visit
        ##############  your code ############

        current = frontier_node_queue.popleft()

        isVisited = False
        for visited_node in visited_node_list:
            if current.equals(visited_node):
                isVisited = True
        if isVisited == False:
            visited_node_list.append(current)

        # if node_is_not_explored(current):
        #     visited_node_list.append(current)
        if find_the_goal(current, goal_node):
            # print(current)
            break
        # put the current node's neighbors in the frontier queue

        ######################################

        # explore
        ##############  your code ###########
        for neighbor in current.neighbors():
            # isExplored = False
            # for explored_node in explored_node_list:
            #     if neighbor.equals(explored_node):
            #         isExplored = True
            
            # if isExplored == False:
            if node_is_not_explored(neighbor):
                frontier_node_queue.append(neighbor)
                explored_node_list.append(neighbor)


        #####################################
        


def node_is_not_explored(node):
    for explored_node in explored_node_list:
        if node.equals(explored_node):
            return False
    return True

def find_the_goal(node, goal_node):
    return node.equals(goal_node)

def main():
    start_state = [3,1,2,
                   4,0,5,
                   6,7,8]
    start_node = Node(start_state, None, depth = 0)

    goal_state = [0,1,2,
                  3,4,5,
                  6,7,8]
    goal_node = Node(goal_state, None, depth = 0)

    ai_search_bfs(start_node, goal_node)

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


