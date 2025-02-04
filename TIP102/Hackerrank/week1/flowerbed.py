from collections import Counter
def can_place_flowers(flowerbed, n):
    # Write your code here
    print(flowerbed, n)
    for i in range(1, len(flowerbed)):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            n -= 1
    counter = Counter(flowerbed)
    print(counter)
    print(flowerbed, counter[0])

    if n <= 0: return True
    return False