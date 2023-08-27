class Solution:
    def canCross(self, stones: List[int]) -> bool:
        jump_dict = {stone: set() for stone in stones}
        jump_dict[0] = {0}  # The frog starts at the first stone with jump length 0

        for stone in stones:
            for jump_length in jump_dict[stone]:
                # Try next jump lengths: k-1, k, k+1
                for next_jump in range(jump_length - 1, jump_length + 2):
                    if next_jump > 0 and stone + next_jump in jump_dict:
                        jump_dict[stone + next_jump].add(next_jump)

        # Check if the last stone has any possible jump lengths
        return len(jump_dict[stones[-1]]) > 0