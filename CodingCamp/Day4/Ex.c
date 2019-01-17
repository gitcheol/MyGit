#include<stdio.h>
#include<stdlib.h>

int main(){
  int *a=(int*)malloc(sizeof(int)*10);

  int i;
  for(i=0; i<10; i++){
    a[i]=-1;
    printf("%d ",a[i]);
  }
  return 0;
}
