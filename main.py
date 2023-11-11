import sys
import os
import data
from heapq import heapify, heappush, heappop


def clear_screen():
    os.system('cls')


def shortest_path(graph, starting_point, hospitals):
    infinite = sys.maxsize
    start_point_neighbour = []
    neighbour_check = True
    node_data = {}
    total_nodes = 0
    for key, value in graph.items():
        node_data[key] = {'cost': infinite, 'pred': []}
        total_nodes += 1

    node_data[starting_point]['cost'] = 0
    visited = []
    temp = starting_point
    for i in range(total_nodes - 1):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap, (node_data[j]['cost'], j))

        heapify(min_heap)
        if neighbour_check:
            start_point_neighbour = min_heap
            neighbour_check = False

        if len(min_heap) != 0:
            temp = min_heap[0][1]
        # else:
        #     temp = start_point_neighbour[0][1]
        #     start_point_neighbour.pop(0)
        #     heapify(start_point_neighbour)

    # for node in node_data.keys():
    #     print(node, node_data[node]["pred"], node_data[node]["cost"])

    near_hospitals = []
    for key in node_data:
        if key in hospitals:
            near_hospitals.append(key)

    max_time = sys.maxsize

    for hospital in near_hospitals:
        if node_data[hospital]['cost'] < max_time:
            closest = hospital
            max_time = node_data[hospital]['cost']

    max_time_2 = sys.maxsize

    for hospital in near_hospitals:
        if node_data[hospital]['cost'] > max_time and node_data[hospital]['cost'] < max_time_2:
            second_closest = hospital
            max_time_2 = node_data[hospital]['cost']

    clear_screen()
    print("The route for closest hospital to your location is:  " +
          str(node_data[closest]['pred'] + [closest]))
    print("Total time to travel: " + str(node_data[closest]['cost']) + " mins")
    print("\n ------------------------------------------------------------------------------------------- \n")
    print("The route for second closest hospital to your location is:  " +
          str(node_data[second_closest]['pred'] + [second_closest]))
    print("Total time to travel: " +
          str(node_data[second_closest]['cost']) + " mins")


if __name__ == "__main__":

    area_option = [dt for dt in data.graph.keys()]

    for i in range(len(area_option)):
        print(f"{i+1}: {area_option[i]}")

    index = int(input("Enter the index no. of the area to select: "))

    shortest_path(data.graph, area_option[index-1], data.hospitals)
