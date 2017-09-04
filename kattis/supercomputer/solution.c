#include <stdio.h>

short st[2000005]; /* segment tree */
long int n; /* number of leaves in tree */

void update(long int id, short val) {
    id += n;
    st[id] = val;
    while (id > 1) {
        id /= 2; /* get parent node */
        st[id] = st[2*id] + st[2*id+1];
    }
}

static inline void flip(long int id) {
    update(id, st[id+n] ^ 1);
}

long int get_range(long int left, long int right) {
    /* left inclusive, right exclusive */
    left += n;
    right += n;
    long int ans = 0;
    while (left < right) {
        if (left % 2 == 1) {
            /* left elem is a right child node, so
            we can't move up a layer */
            ans += st[left];
            ++left;
        }
        if (right % 2 == 1) {
            --right;
            ans += st[right];
        }
        left /= 2;
        right /= 2;
    }
    return ans;
}

int main() {
    long int queries;
    scanf("%ld %ld\n", &n, &queries);
    long int i;
    for (i = 1; i <= 2*n; ++i) {
        st[i] = 0;
    }

    for (i = 0; i < queries; ++i) {
        char c;
        scanf("%c", &c);
        if (c == 'F') {
            long int id;
            scanf("%ld\n", &id);
            flip(id);
        } else {
            long int l, r;
            scanf("%ld %ld\n", &l, &r);
            printf("%ld\n", get_range(l, r+1));
        }
    }
    return 0;
}
