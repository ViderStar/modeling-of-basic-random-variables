from generators import mkm_generator, macLarenMarsaglia


def LabWork1():
    n = 1000
    a01 = 24149775
    c1 = 19581355
    m = 2 ** 31

    a02 = 179029053
    c2 = 457816087
    k = 128

    # Output sequence values to be tested
    #
    # MKM - 1st element:        0.614329
    # MKM - 15th element:       0.792078
    # MKM - 1000th element:     0.027633
    #
    # MacLaren-Marsaglia - 1st element:     0.008959
    # MacLaren-Marsaglia - 15th element:    0.614329
    # MacLaren-Marsaglia - 1000th element:  0.496629

    mkm1 = mkm_generator(a01, c1, m, n)
    print()
    print("MKM - 1st element:", mkm1[0])
    print("MKM - 14th element:", mkm1[14])
    print("MKM - 1000th element:", mkm1[999])
    print()

    mkm2 = mkm_generator(a02, c2, m, n)
    macLaren_Marsaglia = macLarenMarsaglia(mkm1, mkm2, k, n)
    print("MacLaren-Marsaglia - 1st element:", macLaren_Marsaglia[0])
    print("MacLaren-Marsaglia - 14th element:", macLaren_Marsaglia[14])
    print("MacLaren-Marsaglia - 1000th element:", macLaren_Marsaglia[999])
