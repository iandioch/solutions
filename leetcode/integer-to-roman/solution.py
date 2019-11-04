class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        sorted_keys = sorted(d.keys(), reverse=True)
        ans = []
        while num > 0:
            for k in sorted_keys:
                if k <= num:
                    num -= k
                    ans.append(d[k])
                    break
        return ''.join(ans)
