#include <stdio.h>

#define VMAX 10000

int primzahlen(void);


int main(){
    primzahlen();
    return 0;
}

int primzahlen(void){
    int is_prime[VMAX] = {1};

    for (int i = 0; i<VMAX;++i){
        is_prime[i] = 1;
    }    

    for (int i = 2; i < VMAX+1 ;++i){
        if (is_prime[i] == 1){
            printf("%i is prime\n",i);
            for (int j = i; j < VMAX; j=j+i){
                is_prime[j] = 0;
            }
        }
    }
    return 0;
}