import math


def find_coprimes(numbers):
    coprimes = {}
    for num in numbers:
        coprimes[num] = list(set([i for i in numbers if num != i and math.gcd(num, i) == 1]))
    return coprimes


def print_coprimes(coprimes):
    for num, coprime_list in coprimes.items():
        if coprime_list:
            print(f"{num} - {', '.join(map(str, sorted(coprime_list)))}")


numbers = [int(i) for i in input().split(';')]
numbers.sort()
coprimes = find_coprimes(numbers)
print_coprimes(coprimes)
