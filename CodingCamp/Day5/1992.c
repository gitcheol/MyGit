#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


int check(int **Image,int x,int y,int size){
  int i,j;
  for(i=0; i<size; i++){
    for(j=0; j<size; j++){
      //size만큼 크기의 ㅁ안 원소를 확인.
      if(Image[x][y]!=Image[x+i][y+j]){
        //-1이 반환되면 배열 안에 0과1 모두 있는 것
        return -1;
      }
    }
  }
  //모두다 1 or 0이면 그 원소 반환
  return Image[x][y];
}


void solver(int **Image,int x,int y,int size){


  if (size==2){
    if (check(Image,x,y,size)==1 || check(Image,x,y,size)==0) {
      printf("%d",check(Image,x,y,size));
    }
    else {
      printf("(%d%d%d%d)",Image[x][y],Image[x][y+1],Image[x+1][y],Image[x+1][y+1]);
    }
    return;
  }

  if (check(Image,x,y,size)==1 || check(Image,x,y,size)==0) {
    printf("%d",check(Image,x,y,size));
    return;
  }

    printf("(");
    //하나를 만들어 줘야된다.
    solver(Image,x,y,size/2);
    solver(Image,x,y+size/2,size/2);
    solver(Image,x+size/2,y,size/2);
    solver(Image,x+size/2,y+size/2,size/2);
    printf(")");
}






int main(){
  int N;
  int i,j;
  int **Image;

  scanf("%d",&N);
  Image= (int**)malloc(sizeof(int)*N+64*N);  //Memory할당부분 다시 알아보자.
  for(i=0; i<N; i++){
    Image[i] = (int*)malloc(sizeof(int)*N+64*N);
  }

  for(i=0; i<N; i++){
    for(j=0; j<N; j++){
      scanf("%1d",&Image[i][j]);
    }
  }
  solver(Image,0,0,N);
  //solver(Image,0,N/2+1,N/2);
  // solver(Image,size/2+1,y,size/2);
  // solver(Image,size/2+1,size/2+1,size/2);












  //deallocation Memory
  for(i=0; i<N; i++){
    free(Image[i]);
  }
  free(Image);

  return 0;
}
