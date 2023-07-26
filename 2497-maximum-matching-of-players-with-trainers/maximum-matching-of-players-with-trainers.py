class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i=0
        j=0
        c=0
        players.sort()
        trainers.sort()
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                i+=1
                j+=1
                c+=1
            else:
                j+=1
        return c