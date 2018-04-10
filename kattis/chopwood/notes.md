A graph problem, ish. Keep a count of how many other nodes point to each node (ie. how many times a number appears in the input). We know that there must be at least this many numbers before that number in the output. Create a priority queue, and initialise it with all numbers where this value is 0. Then as you output things from this queue one at a time, decrement the lowest number that still doesn't have this value as zero. When it reaches zero, add it to the queue.

`Error` should be output if the last item in the input is not equal to N+1.
