import java.util.*;

public class P10868{
	static int[] V;
	static int[][] P;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N,M;
		int min=1000000000;
		N=sc.nextInt();
		M=sc.nextInt();
		V=new int[N+1];
		P=new int[M][2];
		for(int i=1; i<=N; i++)
			V[i]=sc.nextInt();
		for(int i=0; i<M;i++){
			min=1000000000;
			P[i][0]=sc.nextInt();
			P[i][1]=sc.nextInt();
			for(int j=P[i][0]; j<=P[i][1];j++)
				if(V[j]<min)min=V[j];
			System.out.println(min);
			
		}

	}


}
