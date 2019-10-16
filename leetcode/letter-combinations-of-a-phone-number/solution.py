class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = {}
        s["1"] = ""
        s["2"] = "abc"
        s["3"] = "def"
        s["4"] = "ghi"
        s["5"] = "jkl"
        s["6"] = "mno"
        s["7"] = "pqrs"
        s["8"] = "tuv"
        s["9"] = "wxyz"
        s["0"] = " "
        if digits == "":
            return []
        q = [""]
        for d in digits:
            nq = []
            for qu in q:
                for nextlet in s[d]:
                    nq.append(qu + nextlet)
            q = nq
        return q
