#include<stdio.h>
#include<stdlib.h>

int main(){
  int N;
  int i,j;
  int **P;
  scanf("%d",&N);
  P = (int**) malloc ( sizeof(int*) * N);
  for(i=0 ; i<N; i++){
    P[i]=(int*)malloc(sizeof(int)*N);
  }
  for(i=0; i<N; i++){
    scanf("%d",(*P)+i);
  }
  // for(j=0; j<N; j++){
  //   printf("%d ",*(*P+j));
  // }
  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      printf("%d",*(*P+j));
    }
    printf("\n");
    P++;
  }

  return 0;
}
