#include <stdio.h>
#include <stdlib.h>

int main(){
  int n,m;
  int i,j,k;
  int *P;
  int **R;
  int answer=0;
  scanf("%d",&n);
  scanf("%d",&m);
  P=malloc(sizeof(int)*n+4);
  R=malloc(sizeof(int *)*m);
  for(i=0; i<m; i++){
    R[i]=malloc(sizeof(int)*2);
  }
  for(i=0; i<m; i++){
    scanf("%d %d",&R[i][0],&R[i][1]);
  }
  //0으로 초기화.
  for(i=0; i<=n; i++){
    P[i]=0;
  }
  //싱근이의 친구 찾자.
  for(i=0; i<m;i++){
    if(R[i][0]==1){
      P[R[i][1]]=1;
    }
    if(R[i][1]==1){ 
      P[R[i][1]]=1;
    }
  }
  //상근이의 친구의 친구찾는다.
  for(i=0; i<=n; i++){
    //친구라면
    if(P[i]==1){
      //친구의 친구를 확인.
      for(j=0; j<m; j++){
        //i번 친구랑 친구면 1로 만들어준다.
        if(i==R[j][0]){
          if(P[R[j][1]]!=1)P[R[j][1]]=2;
        }
        if(i==R[j][1]){
          if(P[R[j][0]]!=1)P[R[j][0]]=2;
        }
      }
    }
  }

  // for(i=0; i<=n; i++){
  //   printf("P[%d] %d\n",i,P[i]);
  // }


  for(i=0; i<=n; i++){
    if(P[i]==1||P[i]==2){
      answer++;
    }
  }
  printf("%d",answer-1);







  // show
  // for(i=0; i<m; i++){
  //   printf("%d %d\n",R[i][0],R[i][1] );
  // }
  //Memory 해제
  for(i=0; i<m; i++){
    free(R[i]);
  }
  free(R);
  free(P);
  return 0;
}
