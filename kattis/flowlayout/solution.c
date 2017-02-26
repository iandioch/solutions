#include <stdio.h>

int main() {
    while (1) {
        int maxw;
        scanf("%d", &maxw);
        if (maxw == 0) break;
        int row_height = 0;
        int tot_height = 0;
        int row_width = 0;
        int tot_width = 0;
        while (1) {
            int x, y;
            scanf("%d %d", &x, &y);
            if (x == -1 && y == -1) {
                break;
            }
            if (row_width + x > maxw) {
                // new row
                if (row_width > tot_width) {
                    tot_width = row_width;
                }
                row_width = x;
                tot_height += row_height;
                row_height = y;
            } else {
                row_width += x;
                if (y > row_height) {
                    row_height = y;
                }
            }
        }
        if (row_width > tot_width) {
            tot_width = row_width;
        }
        tot_height += row_height;
        printf("%d x %d\n", tot_width, tot_height);
    }
    return 0;
}
