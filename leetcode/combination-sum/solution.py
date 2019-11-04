class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output_list = []
        self.step(target, [], 0, candidates, output_list)
        return output_list

    def step(self, curr, path, currindex, candidates, output_list):
        if curr < 0:
            return
        elif curr == 0:
            output_list.append(path)
            return
        for i in range(currindex, len(candidates)):
            c = candidates[i]
            self.step(curr - c, path + [c], i, candidates, output_list)
