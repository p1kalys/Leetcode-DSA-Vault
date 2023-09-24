class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        #initialize array of 100x100 glasses
        glasses = [[0.0 for _ in range(100)] for _ in range(100)]
        
        #initialize the first glass with all the the poured cups
        glasses[0][0] = poured

        #iterate through all rows but 0, which has been already computed before
        for level in range(99):
           
            #iterate through the amount of glasses in every level, which is level+1, as it has a pyramid shape: [[1], [1,1], [1,1,1],...]
            for glass_pos in range(level + 1):
                
                #if a glass in a given glass position has an overflow (meaning more than 1 cup in it)
                if glasses[level][glass_pos] > 1:
                    
                    #we store the overflow value, and subtract 1, which is the amount that should remain in the overflowed glass
                    overflow = glasses[level][glass_pos] - 1
                    #we divide the overflow equally between the glasses in the positions below (left and right)
                    glasses[level+1][glass_pos] += overflow / 2
                    glasses[level+1][glass_pos+1] += overflow /2

                    #we set the value of the glass at the position that had an overflow to 1
                    glasses[level][glass_pos] = 1

        #return the amount of cups in the glass for a given level and glass_postion, this should always be 1 or less.
        return min(1, glasses[query_row][query_glass])