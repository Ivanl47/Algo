import math


def minEatingSpeed(piles, H):
    def canEatAllBananans(piles, K, H):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / K)
        return hours <= H

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if canEatAllBananans(piles, mid, H):
            right = mid
        else:
            left = mid + 1

    return left



piles1 = [3, 6, 7, 11]
H1 = 10000000000
print(minEatingSpeed(piles1, H1))

piles2 = [30, 11, 23, 4, 20]
H2 = 5
print(minEatingSpeed(piles2, H2))

piles3 = [30, 11, 23, 4, 20]
H3 = 6
print(minEatingSpeed(piles3, H3))