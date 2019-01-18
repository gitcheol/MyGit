#include <stdio.h>

int case_num(int N){
  int num=0;
  int i;
  for(i=0; i<N; i++){
    num=num+N*(N-i);
  }

  return num;
}


int main(){

  printf("%d",case_num(8));


  return 0;
}
