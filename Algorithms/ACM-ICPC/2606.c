#include <stdio.h>
#include <stdlib.h>

struct computer{
  char visit;
  struct computer * temp;
  struct computer * head;
  struct computer * next=NULL;
  link(head,next,temp);

}
void link(struct computer *head ,struct computer *next,struct computer *temp){
  struct computer *i;
  //head부터 다음 next가 NULL일 때 까지.
  i=head;
  while(i->next!=NULL){
    i=next->next;
  }
  temp=malloc(sizeof(struct computer));
  temp=next;
  return;
}


/*
next의 next는 어떻게 구하까 ..
temp라는 임시변수를 만들고, 컴퓨터 안에 시작점인 내가 원하는 애의 head, 다음 노드로 이동할 수 있도록
도와주는 next를 하나 만들었다.(처음에는 NULL로 초기화했다.)
link에 이 세 가지 성분을 넘겨주고 이제 next성분이 NULL일 떄 까지 for문으로 확인해준다.
for문으로 확인하는 방법은 head부터 시작해서 다음 다음 노드로 주욱 주욱 옮겨준다.

NULL까지 가면은 그 NULL자리에 temp를 넣어주면 끝.


linked list
클래스와 메소드관의 관계를 함수에서 적용시켜보자.

*/


int main(){
  struct computer *com;
  int com_num;
  int relation_num;
  int **pair;
  int i;
  scanf("%d",&com_num);
  com=malloc(sizeof(struct computer)*com_num);

  scanf("%d",&relation_num);
  pair=malloc(sizeof(int *)*relation_num);
  for(i=0; i<relation_num; i++){
    pair[i]=malloc(sizeof(int)*2);
  }
  //입력받음
  for(i=0; i<relation_num; i++){
    scanf("%d %d",&pair[i][0],&pair[i][1]);
  }
  //com->visit초기화
  for(i=0; i<relation_num; i++){
    com[i].visit='u';
    com[i].head=com[i];
  }
  //com에 linked list형태로 전달.
  for(i=0; i<relation_num; i++){
    com[pair[i][0]]
  }





  //memory 해제
  for(i=0; i<relation_num; i++){
    free(pair[i]);
  }
  free(pair);
  return 0;
}
//show
// for(i=0; i<relation_num; i++){
//   printf("%d %d\n",pair[i][0], pair[i][1] );
// }
