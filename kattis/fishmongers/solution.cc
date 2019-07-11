#include <stdio.h>
#include <algorithm>

#define MAX_FISH 100000 + 2
#define MAX_BUYER 100000 + 2

struct buyer_t {
    long long int want;
    long long int price;
} buyers[MAX_BUYER] ;

int compare_buyer (buyer_t a, buyer_t b) {
    return (a.price < b.price) ;
}

long long int weight[MAX_FISH];

int main() {
    int num_fish, num_buyer;
    scanf("%d %d", &num_fish, &num_buyer);
    int tot_weight = 0;
    for (int i = 0; i < num_fish; ++i) {
        scanf("%lld", &weight[i]);
    }
    std::sort(weight, weight+num_fish);
    for (int i = 0; i < num_buyer; ++i) {
        scanf("%lld %lld", &buyers[i].want, &buyers[i].price);
    }
    std::sort(buyers, buyers+num_buyer, compare_buyer);
    long long int ans = 0;
    int best_fish = num_fish-1;
    for (int i = num_buyer - 1; i >= 0; --i) {
        for (int j = 0; j < buyers[i].want; ++j) {
            if (best_fish < 0) break;
            ans += weight[best_fish]*buyers[i].price;
            best_fish -= 1;
        }
    }
    printf("%lld\n", ans);
}
