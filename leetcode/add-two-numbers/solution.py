class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        j = l2
        a = []
        b = []
        while True:
            if i is None:
                break
            a.append(i.val)
            i = i.next
        while True:
            if j is None:
                break
            b.append(j.val)
            j = j.next
        a = int(''.join(str(c) for c in a[::-1]))
        b = int(''.join(str(c) for c in b[::-1]))
        ans = str(a + b)
        t = None
        while len(ans):
            d = int(ans[0])
            ans = ans[1:]
            s = ListNode(d)
            s.next = t
            t = s
        return t
