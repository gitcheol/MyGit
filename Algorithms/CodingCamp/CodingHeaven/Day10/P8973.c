#include <stdio.h>
#include <stdlib.h>

int main() {
		int i,j;
		int N,K;
		int ans=1;
		int P[1001] ={0,};
		int M[1001][3]={0,};


		scanf("%d %d",&N,&K);
    // scanf("%d",&K );


		for(i=1; i<=N; i++) {
			scanf("%d %d %d %d",&P[i],&M[i][0],&M[i][1],&M[i][2]);

        // scanf("%d",&M[i][1] );
        // scanf("%d",&M[i][2] );

		}
		for(i=1;i<=N;i++) {
			if(M[i][0]>M[K][0]) {
				ans++;
				continue;
			}
			if(M[i][0]==M[K][0]&&M[i][1]>M[K][1]) {
				ans++;
				continue;
			}
			if(M[i][0]==M[K][0]&&M[i][1]==M[K][1]&&M[i][2]>M[K][2]) {
				ans++;
			}
		}
		printf("%d\n",ans );

//		System.out.println(N+" "+K);
//		for(i=1;i<=N;i++) {
//			System.out.println(P[i] + " "+M[i][0] +" "+M[i][1]+" "+M[i][2]);
//		}
  return 0;
}
