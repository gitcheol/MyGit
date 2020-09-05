#include <stdio.h>

void Swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selection_sort(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        int minidx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[minidx] > arr[j]) {
                minidx = j;
            }
        }
        Swap(&arr[minidx], &arr[i]);
    }
}


int main(){
  int N;
  int i,j;
  int Answer=0;
  scanf("%d",&N);
  int P[N];
  for(i=0; i<N; i++){
    scanf("%d",&P[i]);
  }
  selection_sort(P,N);
  for (i=0; i<N; i++) {
    for(j=0; j<=i; j++){
      Answer+=P[j];
    }
  }
  printf("%d",Answer);




  return 0;
}
