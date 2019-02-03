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
            if (arr[minidx] < arr[j]) {
                minidx = j;
            }
        }
        Swap(&arr[minidx], &arr[i]);
    }
}

int main(){
  int a[10]={9,1,5,3,4,5,6,7,8,9};
  int i;
  selection_sort(a,10);

  for(i=0; i<10; i++){
    printf("%d ",a[i]);
  }

  return 0;
}
