numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in numbers:
    if i == 1:
        continue
    elif i == 2:
        Primes.append(i)
    else:
        x = i
        v = 2
        while x % v != 0:
            v = v + 1
        if v == x:
            Primes.append(x)
        else:
            Not_Primes.append(x)
print(Primes, " - Простые числа")
print(Not_Primes, " - Составные числа")






