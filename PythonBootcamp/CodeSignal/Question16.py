"""def areSimilar(a, b):
    count = 0
    count_A = 0
    count_B = 0

    if len(a) != len(b):
        return(False)
    else:

        for i in range(len(a)):
            if a[i] == b[i] and b[i] in a:
                count_A += 1
            elif a[i] != b[i] and not b[i] in a:
                count_B += 1
            elif a[i] != b[i] and b[i] in a:
                count += 1

        if count_A == len(a):
            return(True)
        elif count_B >= 1:
            return(False)
        elif count > 2:
            return(False)
        elif count == 2:
            return(True)
        elif count < 2:
            return(False)


areSimilar([2, 3, 4, 5, 6, 7, 8], [2, 3, 8, 5, 6, 7])"""

import cmath
num = 1+2j
num_sqrt = cmath.sin(num)
print(f"The square root of {num} is {num_sqrt :.3f}")
