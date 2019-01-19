#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool check_prime(int n){
  int i;
  for(i=2; i<n; i++){
    if(n%i==0){
      return false;
    }
  }
  return true;
}

void Swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void selection_sort(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        int minidx = i;
        for (int j = i + 1; j < size; j++) {
            if (arr[minidx] < arr[j]) {
                minidx = j;
            }
        }
        Swap(&arr[minidx], &arr[i]);
    }
}

//find함수부터 다시. min부터 짜면 되겠다.
void find(int *P, int *answer,int n){
  int i,j,temp;
  int x,y;
  int min=100000;
  for(i=0; i<n; i++){
    if(P[i]==-1)break;
    for(j=0; j<n; j++){
      if(P[j]==-1)break;
      if((P[i]!=-1)&&(P[j]!=-1)){
        if(P[i]+P[j]==n){
          answer[0]=P[i];
          answer[1]=P[j];
          //작은 수가 0 큰 수가 1로.
          if(answer[0]>answer[1]){
            temp = answer[0];
            answer[0]=answer[1];
            answer[1]=temp;
          }
          //큰 수 - 작은 수의 값이 작은 순으로.
          if(answer[1]-answer[0]<=min){
            min=answer[1]-answer[0];
            x=answer[1];
            y=answer[0];
          }
        }
      }
    }
  }
  answer[1]=x;
  answer[0]=y;
  return;
}


int main(){
  int n,i,j;
  int T;
  scanf("%d",&T);
  int answer[2];
  int **A;
  A=malloc(sizeof(int *)*T);

  for(i=0; i<T; i++){
    A[i]=malloc(sizeof(int)*2);
  }

  for(j=0; j<T; j++){
    scanf("%d",&n);
    int *P=malloc(sizeof(int)*n);
    P[0]=-1;
    P[1]=-1;
    //소수가 아니면 -1
    for(i=2; i<n; i++){
      if(check_prime(i)){
        P[i]=i;
      }
      else P[i]=-1;
    }
    selection_sort(P,n);
    find(P,answer,n);
    A[j][0]=answer[0];
    A[j][1]=answer[1];

}
for(i=0; i<T; i++){
  printf("%d %d\n",A[i][0], A[i][1] );
}

  return 0;
}


// for(i=0; i<n; i++){
//   printf("%d ",P[i]);
// }
// printf("%d\n",check_prime(n));

/*
어떻게 풀까 생각해봤는데 생각이 안난다.
n이 주어졌을 때 생각을 시작해야겠네.
n의 소수가 어떤게 있는지 찾아야겠다.

 step1 .  소수인지 확인해주는 function을 하나 짜자.
 step2 . 그 function을 활용해서 n이라는 숫자를 넣었을 때 2~n까지 반복문을
통해서 소수를 return하는데 소수이면 array에 넣어주자.
 step3 . 소수들을 뽑아냈으니 이제 이 소수들로 조합을 해보자.
 n이라는 숫자랑 같아질 수 있는지 0~(n-1)까지 for문 2개로 계산을 해보자.



*/
