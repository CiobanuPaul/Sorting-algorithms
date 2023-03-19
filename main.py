import random
import time

def onlyOneValue(L1, st, dr):
    x = L1[st]
    for elem in L1[st: dr+1]:
        if elem != x:
            return False
    return True


#for quicksort
def InsertionSort(L, st, dr):
    for i in range(st + 1, dr + 1):
        j = i - 1
        key = L[i]
        while j >= st and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key


#for quicksort
def MedianaMedi(L):
    M = []
    for i in range(len(L)//5):
        L1 = L[i*5: i*5+5]
        InsertionSort(L1, 0, 4)
        M.append(L1[2])
    if len(M) > 9:
        return MedianaMedi(M)
    else:
        InsertionSort(M, 0, len(M)-1)
        return M[len(M)//2]


def Mediana5(L):
    M = [random.choice(L) for _ in range(5)]
    InsertionSort(M, 0, 4)
    return M[2]

def QuickSort(L, st, dr, pivChoice = Mediana5):
    if(dr-st < 24):
        InsertionSort(L, st, dr)
        return
    if onlyOneValue(L, st, dr):
        return
    piv = pivChoice(L[st:dr+1])
    ok = False
    i= st-1
    j = st
    while j < dr:
        if L[j] < piv:
            i += 1
            L[i], L[j] = L[j], L[i]
        elif L[j] == piv and ok is False:
            L[j], L[dr] = L[dr], L[j]
            ok = True
            j -= 1
        j += 1
    L[i+1], L[dr] = L[dr], L[i+1]
    QuickSort(L, st, i)
    QuickSort(L, i+2, dr)
    return


#exp - log2 din baza pe care o dorim
def RadixSort(L, exp=3):
    p = 0
    ok = True
    while ok:
        bucks = [[] for _ in range(1 << exp)]
        ok = False
        for x in L: #impartire, apoi modulo
            bucks[(x >> (p*exp)) & ((1 << exp) - 1)].append(x)
            if ok is False and x >> (p*exp) > 0:
                ok = True
        L.clear()
        for buck in bucks:
            L.extend(buck)
        p += 1


def Merge(L, st, dr):
    mij = (st+dr)//2
    i = st
    j = mij+1
    aux = []
    while i <= mij and j <= dr:
        if L[i] <= L[j]:
            aux.append(L[i])
            i += 1
        else:
            aux.append(L[j])
            j += 1
    if i <= mij:
        aux.extend(L[i: mij+1])
    elif j <= dr:
        aux.extend(L[j: dr+1])
    L[st:dr+1] = aux
def MergeSort(L, st, dr):
    if st < dr:
        mij = (st+dr)//2
        MergeSort(L, st, mij)
        MergeSort(L, mij+1, dr)
        Merge(L, st, dr)


def ShellSort(L):
    pas = len(L) >> 1
    while pas > 0:
        for i in range(pas, len(L)):
            aux = L[i]
            j = i
            while j >= pas and aux < L[j-pas]:
                L[j] = L[j-pas]
                j -= pas
            L[j] = aux
        pas = pas >> 1

def CountingSort(L):
    maxi = max(L)
    d = {i: 0 for i in range(0, maxi+1)}
    for x in L:
        d[x] += 1
    L.clear()
    for i in range(0, maxi+1):
        if d[i] > 0:
            L.extend([i]*d[i])


# L = [random.randint(0, 100000000) for _ in range(10000)]
# L1 = L[0 : len(L)]
# print("start")
# start = time.time()
# RadixSort(L, 16)
# QuickSort(L, 0, len(L)-1)
# MergeSort(L, 0, len(L)-1)
# ShellSort(L)
# CountingSort(L)
# end = time.time()
# # print(L1)
# # print(L)
# # if L == sorted(L1):
# #     print("OK")
# # else:
# #     print("Nope")
# print(end-start)
f = open("teste.txt", "w")

T1 = [1 for _ in range(100)]
T2 = [random.randint(0, 100) for _ in range(100)]
T3 = [random.randint(0, 10000) for _ in range(100)]
T4 = [random.randint(0, 100000000) for _ in range(100)]
T5 = [random.randint(10000000, 100000000) for _ in range(100)]
T6 = [1 for _ in range(10000)]
T7 = [random.randint(0, 100) for _ in range(10000)]
T8 = [random.randint(0, 10000) for _ in range(10000)]
T9 = [random.randint(0, 100000000) for _ in range(10000)]
T10= [random.randint(1000000, 10000000) for _ in range(10000)]
T11= [i for i in range(1000000)]
T12= [i for i in range(1000000, -1, -1)]
T13= [random.randint(0, 100) for _ in range(1000000)]
T14= [random.randint(0, 10000) for _ in range(1000000)]
T15= [random.randint(0, 10000000) for _ in range(1000000)]
T16= [random.randint(10000000, 100000000) for _ in range(10000000)]

#         #Numerele, N, Max, eventual, Min
TESTE1 = [(T1, 100, 1, 1), (T2, 100, 100), (T3, 100, 10000), (T4, 100, 100000000),
          (T5, 100, 100000000, 10000000), (T6, 10000, 1, 1), (T7, 10000, 100),
          (T8, 10000, 10000), (T9, 10000, 100000000), (T10, 10000, 10000000, 1000000)]

TESTE2 = [(T11, 1000000, 1000000), (T12, 1000000, 1000000), (T13, 1000000, 100),
          (T14, 1000000, 10000), (T15, 1000000, 10000000), (T16, 10000000, 100000000, 10000000)]
print("Incepe")
nrtest = 1
for i, T in enumerate(TESTE1):
    print("TESTUL ", nrtest)
    nrtest += 1
    f.write("TEST " + str(i+1) + "\n")
    f.write("N= " + str(T[1]) + "\nMax= " + str(T[2]))
    if len(T) == 4:
        f.write("\nMin= " + str(T[3]))
    f.write("\n\n")
    timpi = []

    counter = 0
    print(counter)
    counter += 1
    f.write("Sortarea RADIXSORT, baza 8\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea RADIXSORT, baza 2^10\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L, 10)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea RADIXSORT, baza 2^16\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L, 16)
            end = time.process_time()
            timpi.append(round(end - start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea MERGESORT\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            MergeSort(L, 0, len(L) - 1)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea SHELLSORT\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            ShellSort(L)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea QUICKSORT, Mediana5\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            QuickSort(L, 0, len(L)-1, Mediana5)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea QUICKSORT, Mediana medianelor\n")
    try:
        for nr in range(5):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            QuickSort(L, 0, len(L)-1, MedianaMedi)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea COUNTINGSORT\n")
    try:
        L = T[0][0: len(T[0])]
        start = time.process_time()
        CountingSort(L)
        end = time.process_time()
        timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

f.close()
f = open("teste.txt", "a")
print("Incepe partea II")
for i, T in enumerate(TESTE2):
    print("TESTUL ", nrtest)
    nrtest += 1
    f.write("TEST " + str(i+11) + "\n")
    f.write("N= " + str(T[1]) + "\nMax= " + str(T[2]))
    if len(T) == 4:
        f.write("\nMin= " + str(T[3]))
    f.write("\n\n")
    timpi = []

    counter = 0
    print(counter)
    counter += 1
    f.write("Sortarea RADIXSORT, baza 8\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea RADIXSORT, baza 2^10\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L, 10)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea RADIXSORT, baza 2^16\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            RadixSort(L, 16)
            end = time.process_time()
            timpi.append(round(end - start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")
    print("Radixsort done")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea MERGESORT\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            MergeSort(L, 0, len(L) - 1)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea SHELLSORT\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            ShellSort(L)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    print("Starting quicksort...")
    timpi.clear()
    f.write("Sortarea QUICKSORT, Mediana5\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            QuickSort(L, 0, len(L)-1, Mediana5)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    timpi.clear()
    f.write("Sortarea QUICKSORT, Mediana medianelor\n")
    try:
        for nr in range(2):
            L = T[0][0: len(T[0])]
            start = time.process_time()
            QuickSort(L, 0, len(L)-1, MedianaMedi)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

    print(counter)
    counter += 1
    print("Staring counting sort!")
    timpi.clear()
    f.write("Sortarea COUNTINGSORT\n")
    try:
        L = T[0][0: len(T[0])]
        for nr in range(2):
            start = time.process_time()
            CountingSort(L)
            end = time.process_time()
            timpi.append(round(end-start, 6))
    except:
        f.write("Nu s-a putut rula :(\n\n")
    else:
        geomean = 1
        for timp in timpi:
            f.write(str(timp) + " sec\n")
            geomean *= timp
        geomean = geomean ** (1/len(timpi))
        f.write("Media geometrica: " + str(geomean) + "\n")
        f.write("\n\n")

# poate adaug si radix in baza 2^10
    # RadixSort(T[0], 16)
    # MergeSort(T[0], 0, len(T[0])-1)
    # ShellSort(T[0])
    # QuickSort(T[0], 0, len(T[0])-1, Mediana5)
    # QuickSort(T[0], 0, len(T[0])-1, MedianaMedi)
    # CountingSort(T[0])
f.close()