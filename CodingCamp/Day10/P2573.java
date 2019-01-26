import java.util.Scanner;

public class P2573 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N,M;
		int i,j;
		N=sc.nextInt();
		M=sc.nextInt();
		int[][] I=new int[N][M];
		for(i=1;i<N-1;i++) {
			for(j=1; j<M-1; j++) {
				I[i][j]=sc.nextInt();
			}
		}
		for(i=0;i<N;i++) {
			for(j=0; j<M; j++) {
				System.out.print(I[i][j]+" ");
			}
		System.out.print("\n");
		}
		
		
		
		
		
		
		
		
		
		
		
	}
}

