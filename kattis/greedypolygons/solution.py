import math

def regular_polygon_area(num_sides, side_size):
    return 0.25*num_sides*side_size*side_size*(1/math.tan(math.pi/num_sides))

def circle_area(radius):
    return math.pi*radius*radius

for _ in range(int(input())):
    num_sides, initial_size, expansion_size, num_expansions = map(int, input().split())
    tot_exp = expansion_size*num_expansions
    corners = circle_area(tot_exp)
    rect = tot_exp*initial_size
    orig_area = regular_polygon_area(num_sides, initial_size)
    print(orig_area + corners + num_sides*rect)

