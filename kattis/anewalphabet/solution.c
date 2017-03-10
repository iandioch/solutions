#include <stdio.h>
#include <string.h>

int main() {
    char c[10001];
    fgets(c, 10001, stdin);
    int i;
    int len = strlen(c);
    for (i = 0; i < len; ++i) {
        switch(c[i]) {
            case 'a':
            case 'A':
                printf("@");
                break;
            case 'b':
            case 'B':
                printf("8");
                break;
            case 'c':
            case 'C':
                printf("(");
                break;
            case 'd':
            case 'D':
                printf("|)");
                break;
            case 'e':
            case 'E':
                printf("3");
                break;
            case 'f':
            case 'F':
                printf("#");
                break;
            case 'g':
            case 'G':
                printf("6");
                break;
            case 'h':
            case 'H':
                printf("[-]");
                break;
            case 'i':
            case 'I':
                printf("|");
                break;
            case 'j':
            case 'J':
                printf("_|");
                break;
            case 'k':
            case 'K':
                printf("|<");
                break;
            case 'l':
            case 'L':
                printf("1");
                break;
            case 'm':
            case 'M':
                printf("[]\\/[]");
                break;
            case 'n':
            case 'N':
                printf("[]\\[]");
                break;
            case 'o':
            case 'O':
                printf("0");
                break;
            case 'p':
            case 'P':
                printf("|D");
                break;
            case 'q':
            case 'Q':
                printf("(,)");
                break;
            case 'r':
            case 'R':
                printf("|Z");
                break;
            case 's':
            case 'S':
                printf("$");
                break;
            case 't':
            case 'T':
                printf("']['");
                break;
            case 'u':
            case 'U':
                printf("|_|");
                break;
            case 'v':
            case 'V':
                printf("\\/");
                break;
            case 'w':
            case 'W':
                printf("\\/\\/");
                break;
            case 'x':
            case 'X':
                printf("}{");
                break;
            case 'y':
            case 'Y':
                printf("`/");
                break;
            case 'z':
            case 'Z':
                printf("2");
                break;
            default:
                printf("%c", c[i]);
        }
    }
    return 0;
}
