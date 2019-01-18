#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char const *argv[]) {
  int N,i;
  scanf("%d",&N);


  for(i=N; i>2; i/=2){
    printf("a\n");
  }
  printf("%d\n",i);

  return 0;
}
