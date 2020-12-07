import sys

from collections import defaultdict

all_bags = set()
# map of X contains set((Y, quant), (Z, quant))
rules = defaultdict(set)

for line in sys.stdin.readlines():
    bag, contents = line.strip().strip('.').split('contain')
    bag = ' '.join(bag.split()[:-1]) # remove the word 'bags'
    all_bags.add(bag)
    for content in contents.split(','):
        quantity, *type_ = content.split()[:-1]
        if quantity == 'no':
            # should be empty
            break
        quantity = int(quantity)
        type_ = ' '.join(type_)
        print(quantity, type_)

        rules[bag].add((type_, quantity))


reverse_rules = defaultdict(set)
for bag in rules:
    for contained, quantity in rules[bag]:
        reverse_rules[contained].add(bag)

cost = {}
# bags which have nothing inside them left to calculate. Initialise to the set
# of bags with no contents
done = set(all_bags - set(rules))
for bag in done:
    cost[bag] = 0

while len(done) < len(all_bags):
    for bag in all_bags - done:
        if set(p[0] for p in rules[bag]) <= done:
            done.add(bag)
            cost[bag] = sum(cost[p[0]] * p[1] + p[1] for p in rules[bag])
            break

print(cost)
print(cost['shiny gold'])
