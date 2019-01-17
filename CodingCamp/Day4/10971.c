#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool check_used(int useless[],int A,int N){
  int i;
  for(i=0; i<N; i++){
    if(useless[i]==A){
      return true;
    }
  }
  return false;
}

int magic(int N,int **P,int x,int y,int useless[]){
  int v;
  int i,j;
  for(i=0; i<N; i++){
    if(i==y) continue; //(n,n) pass
    if(check_used(useless,i,N))continue;

  }

  //x,y값이 들어온다.

  return v;
}




int main(){

  int N;
  int i,j;
  int **P;
  scanf("%d",&N);
  //This is hard to make free because of indivisual free function call
  //Easy way is doing Linear 2-D array malloc http://codeng.tistory.com/8
  P = (int**) malloc ( sizeof(int*) * N);
  for(i=0 ; i<N; i++){
    P[i]=(int*)malloc(sizeof(int)*N);
  }

  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      scanf("%d",(*P+j));
    }
    P++;
  }
  P=P-N;

  //2-D array 출력
  // for(i=0; i<N; i++){
  //   for(j=0; j<N; j++){
  //     printf("%d ",P[i][j]);
  //   }
  //   printf("\n");
  // }
  int min=0;
  int val;
  //사용된 애들을 넣어두는 array
  int *useless=(int*)malloc(sizeof(int)*N);
  for(i=0; i<10; i++){
    useless[i]=-1;
  }

  for(i=0; i<N; i++){
    //행에 나온 것은 다시 겹치지 않게.
    useless[0]=i;
    for(j=0; j<N; j++){
      if(i==j) continue; //(n,n)은 패스
      val=magic(N,P,i,j,useless);
      if(val<min){
        min=val;
      }
    }
  }
  printf("%d",min);

  for(i=0 ; i<N; i++){
    free(P[i]);
  }
  free(P);
  return 0;
}
