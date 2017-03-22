#include <stdio.h>

long int parent[200005];

long int find(long int a) {
    while (a != parent[a]) {
        a = parent[a];
    }
    return a;
}

void merge(long int a, long int b) {
    a = find(a);
    b = find(b);
    if (a < b) {
        parent[b] = a;
    } else {
        parent[a] = b;
    }
}

int main() {
    long int numhouse, numlink;
    scanf("%ld %ld", &numhouse, &numlink);
    long int i;
    for (i = 1; i <= numhouse; ++i) {
        parent[i] = i;
    }
    for (i = 0; i < numlink; ++i) {
        long int a, b;
        scanf("%ld %ld", &a, &b);
        merge(a, b);
    }
    long int connected = find(1);
    short allConnected = 1;
    for (i = 2; i <= numhouse; ++i) {
        if (find(i) != connected) {
            allConnected = 0;
            printf("%ld\n", i);
        }
    }
    if (allConnected > 0) {
        printf("Connected\n");
    }
    return 0;
}
