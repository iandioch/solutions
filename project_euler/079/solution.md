I solved this problem on paper.

Firstly, I noted that the numbers 4 and 5 didn't occur in the inputs and could be disregarded.

On inspection of the dataset, it became clear that no number was repeated in the answer.

For each number in {0, 1, 2, 3, 6, 7, 8, 9}, I looked through the data and listed which other numbers came before and after that number in the answer.

This resulted in the following:

Number | Numbers that must come before that number
---|:---
0 | [1,2,3,6,7,8,9]
1 | [3,7]
2 | [1.3,6,7]
3 | [7]
6 | [1,3,7]
7 | []
8 | [1,2,3,6,7]
9 | [,2,3,4,5,6,7,8]

It is clear that the first digit in the answer is 7, seeing as it doesn't rely on anything coming before it. The next digit is 3, seeing as everything it relies on is already in the answer; then 1, 6, and so on.

The final answer was 73162890.

