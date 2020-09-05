#include <stdio.h>
#include <stdlib.h>


void init(int **P,int N){
  int i,j;
  for(i=0;i<N;i++){
    for(j=0;j<N;j++){
      P[i][j]=0;
    }
  }
  return;
}

int main(){
  int N,answer;
  int i,j;
  scanf("%d",&N);
  int **P=malloc(sizeof(int *)*N);
  for(i=0; i<N; i++){
    P[i]=malloc(sizeof(int)*N);
  }
  init(P,N);













  //show
  // for(i=0;i<N;i++){
  //   for(j=0;j<N;j++){
  //     printf("%d ",P[i][j]);
  //   }
  //   printf("\n");
  // }


  //memory deallocation
  for(i=0;i<N;i++){
    free(P[i]);
  }
  free(P);
  printf("%d",answer);
  return 0;
}
