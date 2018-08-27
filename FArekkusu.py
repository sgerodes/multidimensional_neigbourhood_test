def get_neighbourhood(t, a, c, d=1):
    if not(d): return []
    b, s = a, []
    while isinstance(b, (list, tuple)):
        s.append(len(b))
        b = b[0] if b[0] else None
    s += [0] * (len(c) - len(s))
    if not all(0 <= x < y for x, y in zip(c, s)): return []
    t = t == "von_neumann"
    def f(matrix=a, change=0, index=None):
        if index is None: index = []
        for i in range(-d+change*t, d-change*t+1):
            j = c[len(index)] + i
            if s[len(index)] > j >= 0:
                if len(s) - len(index) > 1:
                    yield from f(matrix[j], change+abs(i), index+[i])
                else:
                    if any(index+[i]): yield matrix[j]
    return list(f())