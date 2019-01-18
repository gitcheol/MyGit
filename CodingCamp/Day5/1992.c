#include <stdio.h>
#include <stdlib.h>

int main(){
  int N;
  int i,j;
  int **P;
  scanf("%d",&N);
  //This is hard to make free because of indivisual free function call
  //Easy way is doing Linear 2-D array malloc http://codeng.tistory.com/8
  P = (int **) malloc ( sizeof(int)*N);
  for(i=0 ; i<N; i++){
    P[i]=(int *)malloc(sizeof(int)*N);
  }

  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      scanf("%1d",&P[i][j]);
    }
    P++;
  }
  P=P-N;




//show
  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      printf("%d ",P[i][j]);
    }
    printf("\n");
  }

  return 0;
}
