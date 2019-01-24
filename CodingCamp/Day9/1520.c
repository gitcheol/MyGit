#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count;

void sol(int Map[][502],int val, int y, int x, int ans){
  if(val==ans){
    count++;
    return ;
  }
  if(val<ans){
    return ;
  }
  //우
  if(val>Map[y][x+1])
    sol(Map,Map[y][x+1],y,x+1,ans);
  if(val>Map[y][x-1])
    sol(Map,Map[y][x-1],y,x-1,ans);
  if(val>Map[y+1][x])
    sol(Map,Map[y+1][x],y+1,x,ans);
  if(val>Map[y-1][x])
    sol(Map,Map[y-1][x],y-1,x,ans);

  return;
}

int main(){
  int M,N;
  int Map[502][502]={0,};
  int i,j;
  int answer;
  scanf("%d %d",&M,&N);

  for(i=0; i<M+2; i++){
    for(j=0; j<N+2; j++){
      Map[i][j]=10001;
    }
  }

  for(i=1; i<M+1; i++){
    for(j=1; j<N+1; j++){
      scanf("%d",&Map[i][j]);
    }
  }

    sol(Map,Map[1][1],1,1,Map[M][N]);

    printf("%d",count);
    // for(i=0; i<M+2; i++){
    //   for(j=0; j<N+2; j++){
    //     printf("%d ",Map[i][j]);
    //   }
    //   printf("\n");
    // }



  return 0;
}
