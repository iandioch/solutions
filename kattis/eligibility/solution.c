#include <stdio.h>

int main() {
    int n;
    int i;
    scanf("%d", &n);
    for (i = 0; i < n; ++i) {
        char name[50];
        int schoolyear;
        int birthyear;
        int courses;
        int k;
        scanf("%s %d/%d/%d %d/%d/%d %d", name, &schoolyear, &k, &k, &birthyear, &k, &k, &courses);
        if (schoolyear >= 2010) {
            printf("%s eligible\n", name);
        } else if (birthyear >= 1991) {
            printf("%s eligible\n", name);
        } else if (courses > 40) {
            printf("%s ineligible\n", name);
        } else {
            printf("%s coach petitions\n", name);
        }
    }
    return 0;
}
