class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output_list = []
        for i in range(len(candidates)):
            self.step(target - candidates[i], [candidates[i]], i+1, candidates, output_list)
        return list(set(tuple(o) for o in output_list))

    def step(self, curr, path, currindex, candidates, output_list):
        if curr < 0:
            return
        elif curr == 0:
            output_list.append(path)
            return
        elif currindex >= len(candidates):
            return
        for i in range(currindex, len(candidates)):
            c = candidates[i]
            self.step(curr - c, path + [c], i+1, candidates, output_list)
