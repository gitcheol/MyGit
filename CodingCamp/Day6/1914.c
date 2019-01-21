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

void moveADisk(int *A,int*C,int N){
  int tmp;
  tmp=pop(A,N);
  push(C,N,tmp);
  printf("%d %d\n",1,3);
}

void moveDisks(int *A,int *B,int *C,int size,int N){
  if(size==0){
    return;
  }
  printf("%d %d\n",1,3);
  moveDisks(A,B,C,size-1,N);
  moveADisk(A,C,N);
  moveDisks(A,B,C,size-1,N);
  return;
}





int main(){
  int N,X;
  int *A;
  int *B;
  int *C;
  int i;

  scanf("%d",&N);
  A=malloc(sizeof(int)*N+4);
  B=malloc(sizeof(int)*N+4);
  C=malloc(sizeof(int)*N+4);

  for(i=0; i<=N; i++){
    A[i]=i;
    B[i]=0;
    C[i]=0;
    //printf("%d ",B[i]);
  }


  X=answer(N);
  printf("%d\n",X);

  moveDisks(A,B,C,N,N);


  return 0;
}
