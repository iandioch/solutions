An ad-hoc problem. Simply keep a count (here in a `defaultdict`) of each interval, and then output the interval with the highest frequency in the inputs. Stable sorting in python came in useful here.

Took me a long time to figure out: If there's no valid answer, output 0.

Runs in 3.64s in python3.
