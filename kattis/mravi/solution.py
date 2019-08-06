def main():
    num_node = int(input())
    parent = {}
    for _ in range(num_node-1):
        a, b, flow, has_power = map(int, input().split())
        has_power = bool(has_power)
        parent[b] = (a, flow/100.0, has_power)

    leaf_req = map(int, input().split())
    ans = 0
    for ind, val in enumerate(leaf_req):
        if val == -1:
            # Not a leaf
            continue
        curr = ind + 1
        while True:
            if curr not in parent:
                break
            curr, flow, has_power = parent[curr]
            if has_power:
                # Only need the sqrt of the flow
                val **= 0.5
            val /= flow
        ans = max(ans, val)

        
    print(ans)

main()
