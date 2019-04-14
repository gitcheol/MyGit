#include <stdio.h>
#include <stdlib.h>
//정수의 개수로 이루어진 배열S, 정답을 넣는 행렬 data를 global 변수로 선언한다.
int N, data[10001], S[10001];
int visited[10001];//방문한 element인가 아닌가를 확인해주는 array

int main() {
   int i, j;
   scanf("%d", &N);
   
   for (i=0; i<N; i++)
      scanf("%d", &S[i]);

   int count=0;
   int ispossible=1;
   //가장 뒤에있는 숫자부터 가능한 경우를 확인해준다.
   for (i=N-1; i>=0; i--) {
      count=0;//뒤에서부터 한 칸 앞으로 갈 때 마다 count를 1씩 더해준다
      for (j=0; j<N; j++) {
         if (!visited[j]) {//아직 방문하지 않았으면 밑에 count를 하나 더해준다.
            count++;
            if (S[i] == count-1) { //S[i]에 들어갈 수 있는 숫자가 들어오면 visited를 1로 바꿔주고 정답을 넣는 data array에 j+1을 넣어준다.
               visited[j]=1;
               data[i]=j+1;
               break;
            }
         }
      }
      if (j == N) { //만약 모든 원소의 visited했으면 S를 찾는 것이 불가능하므로 impossible에 0을 넣어준다.
         ispossible=0;
         break;
      }
   }

   if (ispossible) {//불가능한 S가 있다면 -1 아리나면 결과값을 출력해준다.
      for (i=0; i<N; i++) {
         printf("%d ", data[i]);
      }
   }
   else {
      printf("-1\n");
   }

   return 0;
}
