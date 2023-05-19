def dynamic_programming_solution(A, n, path, P, city_list):
    D = [[[None for i in range(n + 1)] for j in range(n)] for k in range(n)]
    P = [[[None for i in range(n + 1)] for j in range(n)] for k in range(n)]

    for i in range(1, n):
        D[i][0][i + 1] = A[i][0]

    for k in range(1, n):
        subsets = create_subsets(1, k, n, [], '')
        if len(subsets) == 1:
            subset = subsets[0].split(', ')
            del subset[-1]
            break

        for j in range(len(subsets)):
            subset = subsets[j].split(', ')
            del subset[-1]
            if k in subset:
                continue

            for i in range(1, n):
                min_cost = float("inf")
                if str(i + 1) in subset:
                    continue
                for l in range(len(subset)):

                    if len(subset) <= 1:
                        new_cost = A[i][int(subset[l]) - 1] + D[int(subset[l]) - 1][k - 1][int(subset[l])]
                    else:
                        new_cost = A[i][int(subset[l]) - 1] + D[int(subset[l]) - 1][k - 1][
                            int(subset[l + 1]) if (l == 0) else int(subset[0])]

                    if min_cost >= new_cost:
                        min_cost = new_cost
                        D[i][k][int(subset[0])] = min_cost
                        P[i][k][int(subset[0])] = int(subset[l])

    for l in range(len(subset)):
        new_cost = A[0][int(subset[l]) - 1] + D[int(subset[l]) - 1][k - 1][
            int(subset[l + 1]) if (l == 0) else int(subset[0])]
        if min_cost >= new_cost:
            min_cost = new_cost
            D[0][k][int(subset[0])] = min_cost
            P[0][k][int(subset[0])] = int(subset[l])
    print_solution(P, k, A, city_list)


def print_solution(P, k, A, city_list):
    nodes = [i for i in range(2, k + 2)]
    node_from = None
    node = 1

    cost = 0
    all_cost = []

    print('Optimal tour:', end='')
    for i in range(k):
        node = P[node - 1][k - i][nodes[0]]

        if node_from is None:
            print(city_list[0], end='-')

            node_from = 1

        print(city_list[node - 1], end='-')
        cost += A[node_from - 1][node - 1]
        all_cost.append(A[node_from - 1][node - 1])

        del nodes[nodes.index(node)]
        node_from = node


    print()
    print('Costs:', end='')
    for item in all_cost:
        print(item, end='-')
    print()
    print("Total cost:", round(cost, 1))


def create_subsets(cur, l, n, subsets, set):
    if l == 0:
        subsets.append(set)
    else:
        for i in range(cur, n + 1):
            if i == 1:
                continue
            set += str(i) + ', '
            subsets = create_subsets(i + 1, l - 1, n, subsets, set)
            set = set[:-(len(str(i)) + 2)]
    return subsets
