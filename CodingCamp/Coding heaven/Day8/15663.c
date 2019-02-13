#include <stdio.h>
#include <stdlib.h>

int permutation(int N,int M){
  if(N==M){
    return 1;
  }

  return N*permutation(N-1,M);
}

int main(){
  int N,M;
  int i,j;
  int max=0;
  scanf("%d %d",&N,&M);
  int *temp;
  int *P;
  int line_num;
  temp=malloc(sizeof(int)*N);
  for(i=0; i<N; i++){
    scanf("%d",&temp[i]);
    if(temp[i]>max)max=temp[i];
  }
  //printf("%d\n",max);

  //숫자배열 선언
  P=malloc(sizeof(int)*max+4);
  for(i=0; i<=max; i++){
    P[i]=0;
  }
  //모든 i에 해당되는 값에 있는 개수.
  for(i=0; i<N; i++){
    P[temp[i]]+=1;
  }
  //show
  // for(i=0; i<=max; i++){
  //   printf("P[%d] : %d\n",i,P[i]);
  // }

  //mPn을 구해주는 (몇 줄 출력할건지) 함수
  line_num=permutation(N,N-M);
  printf("%d\n",line_num);

  //일단은 예외 빼고 다 출력하게 만들어주자.
  for(i=0; i<line_num; i++){
    for(j=0; j<M; j++){

    }
    printf("\n");
  }








  return 0;
}

// 경우의 수
// for(i=0; i<N; i++){
//   printf("%d ",P[i]);
// }
