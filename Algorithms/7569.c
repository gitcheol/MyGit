#include <stdio.h>
#include <stdlib.h>

enum LogicValue {False, True};

typedef struct {
    int tom[100][100][100];
    int M;
    int N;
    int H;
} STORE;

int MinRipeDays(STORE *s);

int main()
{   
    STORE *store;
    int i, j, k;

    store = (STORE *) malloc(sizeof(STORE));

    scanf("%d %d %d", &store->M, &store->N, &store->H);
    
    for (i = 0; i < store->H; i++) {
        for (j = 0; j < store->N; j++) {
            for (k = 0; k < store->M; k++) 
                scanf("%d", &store->tom[i][j][k]);
        }
    }
    printf("%d\n", MinRipeDays(store));

    free(store);

    return 0;
}

int MinRipeDays(STORE *s)
{
    enum LogicValue isLR;
    int *temp;
    int index[3];
    int d_count = 0;
    int r_count;
    int i, j, k, l;

    temp = (int *) malloc(1000000 * sizeof(int));

    while (1) {
        isLR = False;
        r_count = 0;
        l = 0;

        for (i = 0; i < s->H; i++) {
            for (j = 0; j < s->N; j++) {
                for (k = 0; k < s->M; k++) {
                    if (s->tom[i][j][k] == 0) 
                        isLR = True;
                    else if (s->tom[i][j][k] == 1) {
                        temp[l] = 100 * i + 10 * j + k;
                        r_count++;
                        l++;
                        s->tom[i][j][k] = 2;
                    }    
                }
            }
        }
        
        if (isLR == True && r_count == 0 || isLR == False && r_count == 0)
            return -1;
        else if (isLR == False)
            return d_count;        

        for (i = 0; i < r_count; i++) {
            for (j = 0; j < 3; j++) {
                index[j] = temp[i] % 10;                
                temp[i] /= 10;
            }

            if (index[0] > 0) {
                if (s->tom[index[2]][index[1]][index[0] - 1] ==  0)
                    s->tom[index[2]][index[1]][index[0] - 1] = 1;
            }
            
            if (index[0] < s->M - 1) {
                if (s->tom[index[2]][index[1]][index[0] + 1] == 0)
                    s->tom[index[2]][index[1]][index[0] + 1] = 1;
            }

            if (index[1] > 0) {
                if (s->tom[index[2]][index[1] - 1][index[0]] == 0)   
                    s->tom[index[2]][index[1] - 1][index[0]] = 1;
            }
            
            if (index[1] < s->N - 1) {
                if (s->tom[index[2]][index[1] + 1][index[0]] == 0)
                    s->tom[index[2]][index[1] + 1][index[0]] = 1; 
            }

            if (index[2] > 0) {
                if (s->tom[index[2] - 1][index[1]][index[0]] == 0)          
                    s->tom[index[2] - 1][index[1]][index[0]] = 1;
            }
            
            if (index[2] < s->H - 1) {
                if (s->tom[index[2] + 1][index[1]][index[0]] == 0)  
                    s->tom[index[2] + 1][index[1]][index[0]] = 1;  
            }
        }
        d_count++;
    }
    free(temp);
}
