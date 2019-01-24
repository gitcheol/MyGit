#include <stdio.h>
#include <stdlib.h>

int fibo(int x){
  if(x==1) return 1;
  if(x==2) return 1;
  return fibo(x-1)+fibo(x-2);
  }


int main(){
  long N;
  scanf("%ld",&N);
  int i;
  long *P;
  P=malloc(sizeof(long)*N+4);
  P[0]=0;
  P[1]=1;
  P[2]=1;
  for(i=3; i<=N; i++){
    P[i]=P[i-1]+P[i-2];
  }


  //printf("%d\n",fibo(N));

  printf("%ld\n",P[N]);
  return 0;
}
