class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if  flowerbed[i] != 1 and (i == 0 or flowerbed[i - 1] != 1) and ((i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                n -= 1
        return n <= 0