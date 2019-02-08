#include <stdio.h>
#include <stdlib.h>

int main(){
  int A,X;
  scanf("%d %d",&A,&X);
  int *M;
  M=malloc(sizeof(int)*A);
  for(int i=0; i<A; i++){
    scanf("%d",&M[i]);
    if(M[i]<X)printf("%d ",M[i]);
  }








  return 0;
}
