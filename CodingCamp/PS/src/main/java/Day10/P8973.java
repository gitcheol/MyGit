package Day10;
import java.util.Scanner;

public class P8973 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int i,j;
		int N,K;
		int ans=1;
		int[] P =new int[1001];
		int[][] M=new int[1001][3];


		N=sc.nextInt();
		K=sc.nextInt();

		for(i=1; i<=N; i++) {
			P[i]=sc.nextInt();
			for(j=0; j<3; j++) {
				M[P[i]][j]=sc.nextInt();		
			}
		}
		for(i=1;i<=N;i++) {
			if(M[i][0]>M[K][0]) {
				ans++;
				continue;
			}
			else if(M[i][0]==M[K][0]&&M[i][1]>M[K][1]) {
				ans++;
				continue;
			}
			else if(M[i][0]==M[K][0]&&M[i][1]==M[K][1]&&M[i][2]>M[K][2]) {
				ans++;
				continue;
			}
		}
		System.out.println(ans);

	}
}
