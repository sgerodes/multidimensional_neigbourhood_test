from itertools import product


def get_neighbourhood(type, arr, coordinates, distance=1):
    matrix_properties = hyperrectangularity_properties(arr)
    for dimension in range(len(matrix_properties)):
        if not 0 <= coordinates[dimension] < matrix_properties[dimension]:
            return []
    indexes = get_moore(coordinates, distance, matrix_properties) if (type is 'moore') \
        else get_von_neumann(coordinates, distance, matrix_properties) if (type is 'von_neumann') else None
    return get_elements(arr, indexes)


def get_elements(matrix, indexes):
    def get_recc(mat, ind):
        if not ind:
            return mat
        return get_recc(mat[ind.pop(0)], ind)

    return [get_recc(matrix, list(i)) for i in indexes]


def get_moore(coordinates, distance, matrix_properties):
    c = coordinates
    d = distance
    moore_range = [[rc for rc in range(c[i] - d, c[i] + d + 1) if 0 <= rc < matrix_properties[i]] for i in
                   range(len(c))]
    moore_coordinates = list(product(*moore_range))
    moore_coordinates.remove(coordinates)
    return moore_coordinates


def get_von_neumann(coordinates, distance, matrix_properties):
    moore_coordinates = get_moore(coordinates, distance, matrix_properties)
    von_neumann_coordinates = []
    for m_coord in moore_coordinates:
        if manhattan_distance(coordinates, m_coord) <= distance:
            von_neumann_coordinates.append(m_coord)
    return von_neumann_coordinates


def manhattan_distance(start, end):
    return sum(abs(e - s) for s, e in zip(start, end))


def hyperrectangularity_properties(arr):
    array_tree_properties = []
    rectangularity(arr, 0, array_tree_properties)
    return tuple([element[0] for element in array_tree_properties])


def rectangularity(arr, depth, array_tree_properties):
    if not isinstance(arr, list):
        return
    if len(array_tree_properties) < depth + 1:
        array_tree_properties.append([len(arr)])
    else:
        array_tree_properties[depth].append(len(arr))
    for element in arr:
        rectangularity(element, depth + 1, array_tree_properties)
