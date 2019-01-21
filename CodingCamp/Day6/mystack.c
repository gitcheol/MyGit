#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

//stack으로풀어야겠다.
int top(int *T,int size){
  int i;
  for(i=size; i>=0; i--){
    if(T[i]!=0) break;
  }
  return T[i];
}

bool is_empty(int *T,int size){
  if(top(T,size)==0){
    return true;
  }
  return false;
}

int pop(int *T,int size){
  int val=0;
  int i;
    for(i=size; i>=0; i--){
      if(T[i]!=0){
        val=T[i];
        T[i]=0;
        break;
      }
      if(i==0)return 0;
    }
    return val;
}

void push(int *T,int size,int val){
  int i;
  for(i=1; i<=size; i++){
    if(T[i]==0){
      T[i]=val;
      break;
    }
    if(i==size)return;
  }
}

int answer(int N){
  if(N==1)return 1;
  return 2*answer(N-1)+1;
}
void show(){


}

int main(){
  int N,X;
  int i;
  scanf("%d",&N);
  int *A;
  int *B;
  int *C;

  A=malloc(sizeof(int)*N+4);
  B=malloc(sizeof(int)*N+4);
  C=malloc(sizeof(int)*N+4);

  for(i=0; i<=N; i++){
    A[i]=i;
    B[i]=0;
    C[i]=0;
    //printf("%d ",B[i]);
  }
  //material : pop(T,size); top(T,size);, push(T,size,val)
  //push(T,N);
  //stack구현 끝. class없으니깐 개오래걸리고, 개어렵네

  X=answer(N);

  printf("%d\n",X);
  // if(N<=20){
  //
  // }















  free(A);
  free(B);
  free(C);
  return 0;
}
