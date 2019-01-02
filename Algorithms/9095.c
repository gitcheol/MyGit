#include <stdio.h>

int permutation(int x, int y, int z){
  int num=x+y+z;
  int i;
  int result=1;
  for(i=num; i>0; i--){
    result*=i;
  }
  //1의 개수에 대한 분모부
  if(x!=0){
    for(i=x; i>0; i--)
    result/=i;
  }
  //2의 개수에 대한 분모
  if(y!=0){
    for(i=y; i>0; i--)
    result/=i;
  }
  //3의 개수에 대한 분모
  if(z!=0){
    for(i=z; i>0; i--)
    result/=i;
  }

  return result;
}

int number_of_way(int x){
  int i;
  int count=0;
  for(i=x; i>=0; i--){
    //1이 x개있을때부터 시작 ~ 1이 0개 있을 때 까지.
    if(i==x){
      count++;
    }
    //6의 배수가 아니면서 2로 나누어 떨어질 때
    if((i%2==0)&&(i%6!=0)){
        count=count+permutation(i,(x-i)/2,0);
      }
    //6의 배수가 아니면서 3로 나누어 떨어질 때
    if((i%3==0)&&(i%6!=0)){
      count=count+permutation(i,0,(x-i)/3);
    }
    //6의 배수일 때
    if(i%6==0){
      count=count+permutation(i,0,(x-i)/3);
      count=count+permutation(i,(x-i)/2,0);
    }
  }
  return count;
}



int main(){
  int T,i,n;
  scanf("%d",&T);
  for(i=0; i<T; i++){
    //code
    scanf("%d",&n);

    printf("%d\n",number_of_way(n));
  }


  return 0;
}
