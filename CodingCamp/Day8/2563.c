#include <stdio.h>
#include <stdlib.h>

int main(){
  int N;
  int i,j,k;
  int x,y;
  int ans=0;
  scanf("%d",&N);
  int Paper[101][101]={0,};

  for(i=0; i<N; i++){
    scanf("%d %d",&x,&y);
    for(j=1;j<11;j++){
      for(k=1; k<11; k++){
        Paper[x+j][y+k]=1;
      }
    }
  }
  for(i=0;i<101;i++){
    for(j=0;j<101;j++){
      if(Paper[i][j]==1){
        ans+=1;
      }
    }
  }
  printf("%d",ans);








  return 0;
}
