#include <math.h>
#include <stdio.h>
#include <stdint.h>

int is_prime(int num)
{
    double sol = 0;
    double ulim = ceil(sqrt(num));
    if (num ==2){
        return 1;
    }
    for (int i = 2; i <= ulim; i++)
    {
        sol = num/i;
        //printf("%d/%d is %f, ULIM== %f\n",num,i,sol,ulim);
        if (num % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int top;
    int prod = 1;
    uint64_t sum = 0;
    top = 2e6;

    printf("top is %d\n", top);
    for (int i = 2; i < top; i++)
    {
        if (is_prime(i) == 1)
        {
            sum += i;
            printf("%d is a prime, new sum: %ld\n\n", i, sum);
        }
    }
}
