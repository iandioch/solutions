import sys

from collections import defaultdict

# map of X contains set((Y, quant), (Z, quant))
rules = defaultdict(set)

for line in sys.stdin.readlines():
    bag, contents = line.strip().strip('.').split('contain')
    bag = ' '.join(bag.split()[:-1]) # remove the word 'bags'
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

outer_bags = set()
working_set = set(reverse_rules['shiny gold'])
all_seen = set()
while len(working_set):
    b = working_set.pop()
    all_seen.add(b)
    print('considering', b)
    if b not in reverse_rules:
        # b is an outermost bag
        outer_bags.add(b)
        print('added', b)
    else:
        working_set.update(reverse_rules[b])

print(all_seen)
print(len(all_seen))
