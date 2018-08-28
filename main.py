import timeit

do_performance = True
do_functional = False

######## Matrices

M, N, K = 5, 5, 3
type = ["moore", "von_neumann"][0]
matrix3D = [[[k + K * n + K * N * m for k in range(K)] for n in range(N)] for m in range(M)]
coord3D = (1, 1, 1)
matrix2D = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
coord2D = (1, 1)
distance = 3


def mean_x10(arr):
    return sum(arr) / len(arr) * 10


######## implementations
# modules = ["sgerodes4", "popov"]
# modules = ["FArekkusu", "Blind4Basics", "voile", "sgerodes4", "ragnar_codes", "lechevalier"]
modules = ["sgerodes4", "ragnar_codes", "lechevalier"]

try:
    import N_Neigbourhood
    import FArekkusu
    import Blind4Basics
    import sgerodes
    import sgerodes2
    import sgerodes3
    import sgerodes4
    import sgerodes5
    import popov
    import voile
except ModuleNotFoundError as e:
    print(e)

####### Functional Tests
if do_functional:
    print("####### Functional tests #######")
    for name in modules:
        passed = True
        # if empty matrix: neigbourhood == []
        expression = 'get_neighbourhood("von_neumann", [[]], (0, 0), 1)'
        if not eval("{}.{}".format(name, expression)) == []:
            passed = False
        # if distance 0: neigbourhood == []
        expression = 'get_neighbourhood("von_neumann", matrix2D, (0, 0), 0)'
        if not eval("{}.{}".format(name, expression)) == []:
            passed = False
        # if indices outside the matrix: neigbourhood == []
        expression = 'get_neighbourhood("von_neumann", matrix2D, (-1, -1), 1)'
        if not eval("{}.{}".format(name, expression)) == []:
            passed = False
        expression = 'get_neighbourhood("von_neumann", matrix2D, (100, 100), 1)'
        if not eval("{}.{}".format(name, expression)) == []:
            passed = False
        # border indexes
        expression = 'get_neighbourhood("von_neumann", matrix2D, (0, 0), 1)'
        if not sorted(eval("{}.{}".format(name, expression))) == [1, 3]:
            passed = False
        expression = 'get_neighbourhood("moore", matrix2D, (0, 0), 1)'
        if not sorted(eval("{}.{}".format(name, expression))) == [1, 3, 4]:
            passed = False
        # 3D matrix
        expression = 'get_neighbourhood("von_neumann", matrix3D, (0, 0, 0), 1)'
        if not sorted(eval("{}.{}".format(name, expression))) == [1, 3, 15]:
            passed = False
        expression = 'get_neighbourhood("moore", matrix3D, (0, 0, 0), 1)'
        if not sorted(eval("{}.{}".format(name, expression))) == [1, 3, 4, 15, 16, 18, 19]:
            passed = False
        # distance > 1
        expression = 'get_neighbourhood("von_neumann", matrix3D, (1, 1, 1), 2)'
        if not sorted(eval("{}.{}".format(name, expression))) == [1, 3, 4, 5, 7, 15, 16, 17, 18, 20, 21, 22, 23, 25, 31,
                                                                  33, 34, 35, 37, 49]:
            passed = False

        if not passed:
            print("NOT PASSED : ", name)
        else:
            print("PASSED : ", name)
    print()

####### Performance Tests
number_of_tests = 1000
repeat_number = 10

if do_performance:
    print("####### Performance tests #######")
    for name in modules:
        print(mean_x10(
            timeit.repeat('get_neighbourhood({}, {}, {}, {})'.format("'{}'".format(type), matrix3D, coord3D, distance),
                          'from {} import get_neighbourhood'.format(name), number=number_of_tests,
                          repeat=repeat_number)), ":", name)
