#include <stdio.h>
#include <stdlib.h>

int main(){
  int n;
  scanf("%d",&n);
  int *M;
  int *N;
  M=malloc(sizeof(int)*n);
  N=malloc(sizeof(int)*n);
  for(int i=0; i<n; i++){
    scanf("%d",&M[i]);
  }

  for(int i=1; i<n; i++){
    //M[i-1]>0&&M[i-1]+M[i]>0
    if(M[i-1]>0&&M[i-1]+M[i]>0){
      M[i]=M[i-1]+M[i];
    }
    if(M[i]>max) {
      max=M[i];
    }

  }

  printf("%d",max);

  return 0;
}
