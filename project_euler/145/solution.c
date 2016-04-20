#include <stdio.h>
#define ll unsigned long long

int reverse(ll a){
    ll b = 0;
    while(a >= 1){
        b *= 10;
        b += a%10;
        a /= 10;
    }
    return b;
}

int main(){
    int ans = 0;
    ll a = 0;
    while(a++ < 600000000L){
        if (a % 10 == 0){
            continue;
        }
        ll b = reverse(a);
        if(b < a){
            continue;
        }
        ll c = a + b;
        int ok = 1;
        while(c >= 1){
            if (c % 2 == 0){
                ok = 0;
                break;
            }
            c /= 10;
        }
        if(ok){
            //printf("%u %u %u\n", a, b, a+b);
            ans += 2;
            if(a == b){
                ans --;
            }
        }
    }
    printf("%d", ans);
    return 0;
}
