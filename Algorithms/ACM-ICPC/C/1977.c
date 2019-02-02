#include <stdio.h>



int main(){
  int M,N;
  int i;
  int count=0;
  int x,sum=0;
  int a[101]={0,};
  scanf("%d",&M);
  scanf("%d",&N);

  for(i=1; i<101; i++){
    x=i*i;
    if(M<=x&&x<=N){
      a[i]=i;
    }
  }
  //모두 0이면 -1출력
  for(i=1; i<101; i++){
    if(a[i]==0){
      count++;
    }
  }
  if(count==100){
    printf("-1");
    return 0;
  }

  for(i=0; i<101; i++){
    sum+=a[i]*a[i];
  }

  printf("%d\n",sum);

  for(i=0; i<101; i++){
    if(a[i]!=0){
      printf("%d",a[i]*a[i]);
      break;
    }
  }




  return 0;
}
