#include<stdio.h>
#include<stdlib.h>
int checkprice(int rh,int rv, int sh, int sv, int p);

int rh=0;
int rv=0;
int sh=0;
int sv=0;


int main(void){

  int min=0;
  int i=0;
  int n;
  int *rhn;
  int *rvn;
  int *shn;
  int *svn;
  int *pn;

  scanf("%d %d %d %d",&rh,&rv,&sh,&sv);
  scanf("%d",&n);
  rhn = malloc(sizeof(int)*n);
  rvn = malloc(sizeof(int)*n);
  shn = malloc(sizeof(int)*n);
  svn = malloc(sizeof(int)*n);
  pn = malloc(sizeof(int)*n);
  for(i=0;i<n;i++){
    scanf("%d %d %d %d %d",rhn+i,rvn+i,shn+i,svn+i,pn+i);
  }



  for(i=0 ;i<n;i++){
    if(min==0){
      min=checkprice(*(rhn+i),*(rvn+i),*(shn+i),*(svn+i),*(pn+i));
      continue;
    }
    if(min>checkprice(*(rhn+i),*(rvn+i),*(shn+i),*(svn+i),*(pn+i))){
      min=checkprice(*(rhn+i),*(rvn+i),*(shn+i),*(svn+i),*(pn+i));
    }
  }

  printf("%d\n",min);

  return 0;
}

int checkprice(int h, int v, int s_h, int s_v, int p){
  int min;
  int n_h1=0;
  int n_h2=0;
  int n_v1=0;
  int n_v2=0;
  int n_sh1=0;
  int n_sh2=0;
  int n_sv1=0;
  int n_sv2=0;
  int a=0;
  int b=0;
  int c=0;
  int d=0;
  while(h*n_h1<rh){
    n_h1++;
  }
  while(v*n_v1<rv){
    n_v1++;
  }
  while(s_h*n_sh1<sh){
    n_sh1++;
  }
  while(s_v*n_sv1<sv){
    n_sv1++;
  }
  while(v*n_h2<rh){
    n_h2++;
  }
  while(h*n_v2<rv){
    n_v2++;
  }
  while(s_v*n_sh2<sh){
    n_sh2++;
  }
  while(s_h*n_sv2<sv){
    n_sv2++;
  }
  if(n_h1<n_sh1)
    a=n_sh1;
  else a=n_h1;
  if(n_v1<n_sv1)
    b=n_sv1;
  else b=n_v1;
  if(n_h2<n_sh2)
    c=n_sh2;
  else c=n_h2;
  if(n_v2<n_sv2)
    d=n_sv2;
  else d=n_v2;
  if(a*b>=c*d)
    min=c*d;
  else
    min=a*b;
  return min*p;
}
