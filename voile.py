def span(n_type, mat, coord, d, t):
    v = len(t)
    if v == len(coord):
        if coord != t: yield mat
    elif type(mat) in (list, tuple) and coord[v]>=0 and coord[v]<len(mat):
        if n_type == "von_neumann":
            for r in range(coord[v]-d, coord[v]+d+1):
                if r>=0 and r<len(mat): yield from span(n_type, mat[r], coord, d-abs(coord[v]-r), t+[r])
        elif n_type == "moore":
            for r in range(coord[v]-d, coord[v]+d+1):
                if r>=0 and r<len(mat): yield from span(n_type, mat[r], coord, d, t+[r])

def get_neighbourhood(n_type, mat, coord, d=1):
    return list(span(n_type, mat, list(coord), d, []))