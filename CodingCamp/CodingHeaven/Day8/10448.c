#include <stdio.h>
#include <stdlib.h>

int main(){
  int N;
  int m,x;
  int * ans;
  int * val;

  scanf("%d",&N);
  ans=malloc(sizeof(int)*N);
  val=malloc(sizeof(int)*N);
  int T[45]={0,};
  int i,j,k;
  int result;
  for(i=1; i<=44; i++){
    T[i]=i*(i+1)/2;
  }






for(m=0; m<N; m++){
  ans[m]=0;
  scanf("%d",&val[m]);
  result=0;
    for(i=44; i>0; i--){
      for(j=44; j>0; j--){
        for(k=44; k>0; k--){
          result=T[i]+T[j]+T[k];
          if(result==val[m]){
            ans[m]=1;
            break;
          }
        }
        if(result==val[m])
          break;
    }
    if(result==val[m])
      break;
  }
  if(result!=val[m])
    ans[m]=0;
}

  for(i=0; i<N; i++){
    printf("%d\n",ans[i] );
  }


  return 0;
}
