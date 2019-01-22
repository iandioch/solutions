#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>

using namespace std;

#define ll long long int
#define dcmp(a, b) (abs((a)-(b))<0.00001L)
#define MAXN 200001

ll n, m;
ll numpoint, reqpoint;

int x[MAXN];
int y[MAXN];
int deleted[MAXN];

// shoelace formula
long double tri_area(int x1, int y1, int x2, int y2, int x3, int y3) {
    return abs((x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3 + 0.0L)/2.0L);
}

struct triangle {
    long double area;
    int i1;
    int i2;
    int i3;
    bool operator<(const triangle& rhs) const {
        if (dcmp(area, rhs.area)) {
            return i2 > rhs.i2;
        }
        return area > rhs.area;
    }
};

int main() {
    scanf("%lld %lld", &n, &m);
    numpoint = n+1;
    reqpoint = m+1;
    for (ll i = 0; i < numpoint; ++i) {
        scanf("%d %d", &x[i], &y[i]);
    }
    memset(deleted, 0, numpoint);

    priority_queue<triangle> q;

    for (ll i = 0; i < numpoint-2; ++i) {
        ll j = i + 1; //(i+1)%numpoint;
        ll k = i + 2; //(i+2)%numpoint;
        long double area = tri_area(x[i], y[i], x[j], y[j], x[k], y[k]);
        triangle t = {area, i, j, k};
        q.push(t);
    }

    for (ll i = 0; i < (numpoint - reqpoint); ++i) {
        triangle t;
        while (1) {
            t = q.top();
            q.pop();
            //printf("Chosen triangle %d %d %d with area %Lf\n", t.i1, t.i2, t.i3, t.area);
            if (deleted[t.i1] || deleted[t.i2] || deleted[t.i3]) continue;
            break;
        }
        deleted[t.i2] = 1;
        printf("%d\n", t.i2);
        //printf("(%d %d), (%d %d), (%d %d)\n", x[t.i1], y[t.i1], x[t.i2], y[t.i2], x[t.i3], y[t.i3]);
        ll j = t.i1 - 1;
        while (j >= 0 && deleted[j]) {
            --j;
        }
        if (j >= 0) {
            triangle r = {tri_area(x[j], y[j], x[t.i1], y[t.i1], x[t.i3], y[t.i3]), j, t.i1, t.i3};
            q.push(r);
        }
        j = (t.i3 + 1);
        while (j < numpoint && deleted[j]) {
            ++j;
        }
        if (j < numpoint) {
            triangle s = {tri_area(x[t.i1], y[t.i1], x[t.i3], y[t.i3], x[j], y[j]), t.i1, t.i3, j};
            q.push(s);
        }
    }

    /*while (!q.empty()) {
        triangle t = q.top();
        q.pop();
        
        printf("Chosen triangle %d %d %d with area %Lf\n", t.i1, t.i2, t.i3, t.area);
        printf("(%d %d), (%d %d), (%d %d)\n", x[t.i1], y[t.i1], x[t.i2], y[t.i2], x[t.i3], y[t.i3]);
    }*/

    return 0;
}
