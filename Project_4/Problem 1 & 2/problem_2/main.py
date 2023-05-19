import extract_dataset
import path_cost
import prims_algorithm
import kruskals_algorithm


def print_tree(tree, city_list):
    for i in range(len(tree)):
        for j in range(len(tree)):
            if tree[i][j] == None:
                tree[i][j] = '-'
    for i in range(len(city_list)):
        print(f"{tree[i]} - {city_list[i]}")
    print('')


def main():
    norwegian_cities = extract_dataset.open_file()
    A, city_list = path_cost.find_path_costs(norwegian_cities)

    print("Prims's Algorithm:")
    tree = prims_algorithm.prim(A)
    print_tree(tree, city_list)

    tree = kruskals_algorithm.kruskal(A)
    print("Kruskal's Algorithm:")
    print_tree(tree, city_list)


if __name__ == '__main__':
    main()
