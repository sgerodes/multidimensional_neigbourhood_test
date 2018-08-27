def genNeigh(isNeum, arr, coords, d, var=0, idx=()):
    depth = len(idx)
    x     = coords[depth]

    if not (0 <= x < len(arr)): raise IndexError()

    low, up = -d + isNeum*var, d - isNeum*var+1
    for j in range(max(0, low+x), min(up+x, len(arr))):
        indexes = idx+(j,)
        if 0 <= j < len(arr) and indexes != coords:
            if depth < len(coords)-1:
                yield from genNeigh(isNeum, arr[j], coords, d, var+abs(j-x), indexes)
            else:
                yield arr[j]


def get_neighbourhood(typ, arr, coords, d=1):
    try:
        return list(genNeigh(typ=='von_neumann', arr, coords, d))
    except IndexError:
        return []