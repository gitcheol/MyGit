#include <stdio.h>
#include <stdlib.h>
// bubble sorting

// void sorting(int *M,int size){
//   int temp;
//   for(int i=size-1; i>=0; i--){
//     for(int j=0; j<i; j++){
//       if(M[j]>M[j+1]){
//         temp=M[j];
//         M[j]=M[j+1];
//         M[j+1]=temp;
//       }
//     }
//   }
//
//   return ;
// }

int main(){
  int n;
  scanf("%d",&n);
  int *M;
  int sum=0;
  int max=-100000;
  int min=-1000;
  int count=0;
  M=malloc(sizeof(int)*n);
  for(int i=0; i<n; i++){
    scanf("%d",&M[i]);
    if(M[i]>0)sum+=M[i];
    if(M[i]<0){
      if(M[i]>min)min=M[i];
      count++;
      if(count==n){
        printf("%d",min);
        return 0;
      }
      if(max<sum)max=sum;
      sum=0;
    }
  }
  printf("%d",max);

  //sorting(M,n);
  // for(int i=0; i<n; i++){
  //   printf("%d ",M[i]);
  // }

  return 0;
}
