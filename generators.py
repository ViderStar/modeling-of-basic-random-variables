def mkm_generator(seed, multiplier, modulo, n):
    max1 = max(multiplier, modulo - multiplier)
    value = seed
    sequence = []
    for _ in range(n):
        value = (max1 * value) % modulo
        random = value / modulo
        sequence.append(random)
    return sequence


def macLarenMarsaglia(MKM1, MKM2, k, n):
    V = []
    for i in range(k):
        V.append(MKM1[i])

    mcl = []
    for i in range(n):
        s = int(MKM2[i] * k)
        alfa = V[s]
        mcl.append(alfa)
        if i + k < n:
            V[s] = MKM1[i + k]
    return mcl

