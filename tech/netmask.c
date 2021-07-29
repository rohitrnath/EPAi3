#include <stdio.h>

/*
11110000 - 1 = 11101111

*/
int netmask( unsigned char value)
{
    int i, flag_1=0;
    for( i =0; i< (8*sizeof(value)); i++)
    {
        
        unsigned char bitVal = 1 &(value >> i);
        //printf(" bitVal: %d\n", bitVal);
        if(bitVal)
        {
            if(flag_1 == 0) flag_1 = 1;
        }
        else
        {
            if(flag_1 == 1) break;        
        }

    }
    if( i==sizeof(value)*8) return 1;
    else return 0;
}

int main()
{
    unsigned char num = 253;
    printf(" bool netmask: %d\n", netmask(num));
    return 0;
}