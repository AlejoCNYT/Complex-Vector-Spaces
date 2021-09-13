import Libcplx as lc


# 1.Adición de vectores complejos
def adVector(v, w):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.cplxsum(v[k], w[k])]
    return r


# 2.Inverso (aditivo) de un vector complejo
def invVector(v):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.cplxproduct((-1, 0), v[k])]
    return r


# 3.Multiplicación de un escalar complejo
def MultEscalarVector(v, w):
    n = len(w)
    r = []
    for k in range(n):
        r += [lc.cplxproduct(v, w[k])]
    return r


# 4.Adición de matrices complejas
def sumaMatrix(v, w):
    m = len(w)
    n = len(v[0])
    fila = []
    r = [fila] * m
    for j in range(m):
        fila = []
        r[j] = fila
        for k in range(n):
            r += [lc.cplxsum(v[j][k], w[j][k])]
    return r


# 5.Inversa (aditiva) de una matriz compleja
def invAdMtx(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(m):
        fila = []
        r[j] = fila
        for k in range(n):
            r[j] += [lc.cplxproduct((-1,0), v[j][k])]
    return r


# 6. Multiplicación de un escalar por una matriz compleja
def MultEscMtx(v, w):
    m = len(w)
    n = len(w[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [lc.cplxproduct(v, w[j][k])]
    return r


# 7. Transpuesta de una matriz/vector
def trMtx(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [v[k][j]]
    return r


# 8. Conjugada de una matriz/vector
def conjMtx(A):
    m = len(A)
    n = len(A[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [lc.cplxconj((-1,0), A[j][k])]
    return r


# 9.Adjunta (daga) de una matriz/vector
def adjMtx(A):
    n = len(A)
    m = len(A[0])
    r = [n] * m
    for j in range(n):
        fila = [] * n
        r[j] = fila
        for k in range(m):
            r[j] += [lc.cplxconj((-1,0), A[k][j])]

    return r


# 10.Producto de dos matrices (de tamaños compatibles)
def ProdMtx(A, B):
    m = len(A)
    n = len(A[0])
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):
        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxproduct(A[j][k], B[j][k])
    return r


# 11. Función para calcular la "acción" de una matriz sobre un vector
def MtxVec(A, B):
    m = len(A)
    n = len(A[0])
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):
        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxproduct(A[j][k], B[j][k])
    return r


# 12. Producto interno de dos vectores
def vectorPrInt(v):
    r = int(lc.cplxmod(v) ** 2)
    return r


# 13. Norma de un vector
def vectorNorm(v):
    r = int(lc.cplxmod(v))
    return r


# 14. Distancia entre dos vectores
def disV(v,w):
    ele = 0
    s = 0
    for i in range(len(v)):
        ele = v[i]-w[i]
        ele = ele**2
        s += ele
    n = s ** (1/2)
    return n


# 15. Revisar si una matriz es unitaria



# 16. Revisar si una matriz es Hermitiana
def hermMtx(v):
    if adjMtx(v) == v:
        return True


# 17. Producto tensor de dos matrices/vectores
def vectorTsorProduct(A, B):
    na = len(A)
    nb = len(B)
    nr = nb * na
    R = [(0, 0)] * nr
    index = 0
    for j in range(na):
        for k in range(nb):
            R[index] = MultEscalarVector(A[j], B[k])
            index = index + 1
    return R

    # print(adVector(v,w))
    # print(invVector(v))
    # print(MultEscalarVector(v,w))
    # print(sumaMatrix(v,w))
    # print(InvAdMtx(v,w))
    # print(MultEscMtx(v,w))
    # print(trMtx(v))