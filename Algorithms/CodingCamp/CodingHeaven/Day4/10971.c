#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int count;
int answer[300];

struct Path{
  char visit;
  int value;
};

void show(struct Path **P,int N){
  //2-D array 출력
  int i,j;
  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      printf("%c ",P[i][j].visit);
    }
    printf("\n");
  }
}

bool check_visit(struct Path P){
  if(P.visit=='u')return false;
  return true;
}

void init(struct Path **P,int size){
  int i,j;

  for(i=0; i<size; i++){
    for(j=0; j<size; j++){
      if(i==j){
        (*P+j)->visit='v';
        continue;
      }
      (*P+j)->visit='u';
    }
    P++;
  }
  P=P-size;
  return;
}
int sum(struct Path **P,int size){
  int ans=0;
  int i,j;
  for(i=0;i<size;i++){
    for(j=0; j<size; j++){
      if(P[i][j].visit=='u'){
        ans+=P[i][j].value;
      }
    }
  }
  return ans;
}
void change_char(struct Path**P,int size){
  return;
}



void select(struct Path **P, int size,int x,int y,int N){
  int i,j;
  int key;
  if(size-1==N){
    key=x;
  }
  // //recursive의 끝을 나타냄

  N--;
  if(N==0) {
    answer[count++]=sum(P,size);
    return ;
  }

  //(x,y)를 제외하고 모두 'v'로 바꿈
  for(i=0; i<size; i++){
    if(i==y)continue; // x,y일 때 빼고
    P[x][i].visit='v';
  }
  for(i=0; i<size; i++){
    P[i][x].visit='v'; //다시 원래로 돌아가는거 막기
  }
  show(P,size);
  printf("\n\n");

  //처음으로 돌아가는거 다시 열어준다.
  if(N==1){
    P[y][key].visit='u';
  }

  //다음행에 대해서 다시 실시.
  for(j=0; j<size; j++){
    if(P[y][j].visit=='v')continue;
    select(P,size,y,j,N);
  }

}

int main(){

  int N;
  int i,j;
  struct Path **P;
  scanf("%d",&N);
  //This is hard to make free because of indivisual free function call
  //Easy way is doing Linear 2-D array malloc http://codeng.tistory.com/8
  P = (struct Path**) malloc ( sizeof(struct Path*) * N);
  for(i=0 ; i<N; i++){
    P[i]=(struct Path*)malloc(sizeof(struct Path)*N);
  }

  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      scanf("%d",&((*(*P+j)).value));
    }
    P++;
  }
  P=P-N;
  init(P,N);

  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      if(check_visit(P[i][j])==true){
        continue;
      }
      select(P,N,i,j,N-1); return 0;
      init(P,N);
    }
  }

  //최솟값 골라내기
  int min;
  for(i=0; i<50; i++){
    printf("%d ",answer[i]);
  }
  //printf("%d",min);


  //메모리 해제
  for(i=0 ; i<N; i++){
    free(P[i]);
  }
  free(P);
  return 0;
}
