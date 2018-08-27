# Excercise src: http://www.codewars.com/kata/multidimensional-neighbourhood
# Solution v1 by Dimitri Popov
# The idea of the algorithm is probably best described by the term "iteratively implemented end recursion".

# the "von_neumann" implemenation should be highly efficient
# the "moore" implemenation is mostly efficient, but might be improved by not having to flatten the list.
#    also, I don't know if "get_all_elements" is the best variant or if it slow because using a queue here
#    instead of a recursive call might use data in a way that doesn't make much use of the Cpu-L1-cache
# It should also be noted that using NumPy instead of plain Python should also add efficiency.


from collections import deque


def get_all_elements(matrix, coordinates, from_to):
    cur = deque()
    cur.append(matrix)
    for (fr, to) in from_to:
        nxt = deque()
        for c in cur:
            for x in range(fr, to):
                nxt.append(c[x])
        cur = nxt

    return cur


def get_neighbourhood_m(matrix, coordinates, distance):
    depth = len(coordinates)
    width = len(matrix)

    results = []
    for d in range(depth):
        c = coordinates.pop()
        from_to = [(max(0, x - distance), min(width, x + distance + 1)) for x in coordinates]
        for x in range(max(0, c - distance), c):
            results.append(get_all_elements(matrix[x], coordinates, from_to))
        for x in range(c + 1, min(width, c + distance + 1)):
            results.append(get_all_elements(matrix[x], coordinates, from_to))
        matrix = matrix[c]

    # return results
    return[item for sublist in results for item in sublist]


def get_element(matrix, coordinates):
    m = matrix
    for c in coordinates:
        m = m[c]
    return m


def get_neighbourhood_n(matrix, coordinates, distance):
    depth = len(coordinates)
    width = len(matrix)

    results = []
    for d in range(depth):
        c = coordinates.pop()
        for x in range(max(0, c - distance), c):
            results.append(get_element(matrix[x], coordinates))
        for x in range(c + 1, min(width, c + distance + 1)):
            results.append(get_element(matrix[x], coordinates))
        matrix = matrix[c]

    return list(results)


def get_neighbourhood(ttype, matrix, coordinates, distance):
    coordinates = list(coordinates)
    if ttype == "moore":
        return get_neighbourhood_m(matrix, coordinates, distance)
    elif ttype == "von_neumann":
        return get_neighbourhood_n(matrix, coordinates, distance)


# Simple functionality test (3d)

#m = [[[111, 112, 113, 114], [121, 122, 123, 124], [131, 132, 133, 134], [141, 142, 143, 144]],
#     [[211, 212, 213, 214], [221, 222, 223, 224], [231, 232, 233, 234], [241, 242, 243, 244]],
#     [[311, 312, 313, 314], [321, 322, 323, 324], [331, 332, 333, 334], [341, 342, 343, 344]],
#     [[411, 412, 413, 414], [421, 422, 423, 424], [431, 432, 433, 434], [441, 442, 443, 444]]]

#print(get_neighbourhood("moore", m, [1, 1, 1], 1))
#print(get_neighbourhood("von_neumann", m, [1, 1, 1], 2))
