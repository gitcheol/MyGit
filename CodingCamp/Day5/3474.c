#include <stdio.h>
#include <stdlib.h>

int ex_of_5(int x){
  if(x==0)return 1;
  return 5*ex_of_5(x-1);
}


int main(){
  int answer;
  int i,j;
  int N,T;
  int *a;
  scanf("%d",&T);
  a = (int *)malloc(sizeof(int)*T);

  for(i=0; i<T; i++){
    scanf("%d",&N);
    answer=0;
    for(j=1; j<14; j++){
      answer=answer+N/ex_of_5(j);
    }
    a[i]=answer;
  }
  for(i=0; i<T; i++){
    printf("%d\n",a[i]);
  }

  free(a);
  return 0;
}
