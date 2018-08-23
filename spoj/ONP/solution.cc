#include <cstdio>
#include <cstring>

using namespace std;

int t;
char expr[401];
int len;
char out[401];

char stack[401];
int stackpt;

int main() {
    scanf("%d", &t);
    while (t--) {
        scanf("%s", expr);
        len = strlen(expr);
        stackpt = 0;
        for (int i = 0; i < len; ++i) {
            switch (expr[i]) {
                case '*': case '+': case '-': case '/': case '^':
                    stack[stackpt] = expr[i];
                    ++stackpt;
                break;
                case '(':
                break;
                case ')':
                    --stackpt;
                    printf("%c", stack[stackpt]);
                break;
                default:
                printf("%c", expr[i]);
            }
        }
        printf("\n");
    }
}
