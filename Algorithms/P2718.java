import java.util.*;

public class P2718{
	static int[][] L;	

	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N,M;
		N=sc.nextInt();
		M=sc.nextInt();
		L=new int[N+1][M+1];
		for(int i=1; i<=N; i++){
			for(int j=1; j<=M; j++){
				L[N][M]=sc.nextInt();		
			}
		}
		
		for(int i=1; i<=N; i++){
			for(int j=1; j<=M; j++){
				System.out.print(L[N][M]+ " ");
			}
			System.out.println("");
		}


	}

}
