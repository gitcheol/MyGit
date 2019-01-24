#include <stdio.h>
#include <stdlib.h>

int num_of_2(int x){
  int a;
  int val=0;
  if(x==0){
    return 0;
  }
  while(1){
    if(x==0){
      break;
    }
    a=x%2;
    x=x/2;
    val+=a;

  }
  return val;
}

int mul(int x){
    if(x==0){
      return 1;
    }
    return 2*mul(x-1);
}


int main(){
  int N,K;
  int num_A;
  int num_B;
  int sum=0;
  int average;
  int i,j;
  int k=0,s=0;
  //N=사과(1개) K=상자
  //각 상자에는 2^(N-K)개의 정수가 있따.
  scanf("%d %d",&N,&K);
  //printf("%d %d\n",N,K);
  num_A=mul(N);
  num_B=mul(K);

  for(i=0; i<num_A; i++){
    sum+=num_of_2(i);
  }

  average=num_A/num_B;

  //printf("%d\n",average);
  for(j=0; j<num_B;j++){
    for(i=0; i<average/2; i++){
      printf("%d ",k);
      k++;
    }
    for(i=0; i<average/2; i++){
      k--;
      printf("%d ",(num_A-1)-k);

    }
    k+=average/2;
    printf("\n");
  }
  return 0;
}
