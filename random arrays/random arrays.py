from random import randint

TEST_COUNT = 10
MAX_DISTANCE = 5
MAX_MATRIX_DIMENSION = 8
MIN_DIMENSION_SIZE = 1
MAX_DIMENSION_SIZE = 7


def main():
    matrix, coordinates = random1(2)
    print(matrix)
    print(coordinates)


def random1(dimensions):
    def random_hyperrectangular_matrix_and_random_coordinates_within(dimensions):
        rectangular_properties = [randint(MIN_DIMENSION_SIZE, MAX_DIMENSION_SIZE) for _ in range(dimensions)]

        def recc2(dim):
            if dim < 0:
                return randint(0, 100)
            return [recc2(dim - 1) for _ in range(rectangular_properties[dim - 1])]

        random_n_dimensional_matrix = recc2(dimensions)
        random_coordinates_within_matrix = [randint(0, rectangular_properties[i]) for i in range(dimensions)]
        return random_n_dimensional_matrix, random_coordinates_within_matrix

    return random_hyperrectangular_matrix_and_random_coordinates_within(dimensions)


main()
