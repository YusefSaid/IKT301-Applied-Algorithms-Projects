import extract_dataset
import path_cost
import Greedy
import dynamic_programming
import Dijkstra


def main():
    norwegian_cities = extract_dataset.open_file()
    A, city_list = path_cost.find_path_costs(norwegian_cities)
    #Dijkstra.solve_with_dijkstra(A, city_list)
    #Greedy.greedy_algorithm(A, city_list)
    P = [[0 for i in range(len(A))] for j in range(len(A))]
    dynamic_programming.dynamic_programming_solution(A, len(A), None, P, city_list)
    # returns adjacency matrix
    # tsp(A, 0)


if __name__ == "__main__":
    main()
