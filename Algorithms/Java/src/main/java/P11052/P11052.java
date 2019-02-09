package P11052;
import java.util.*;

public class P11052 {
	static int[] P;
	static int[] C;

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N;
		N=sc.nextInt();
		P=new int[N+1];
		C=new int[N+1];
		for(int i=1; i<=N; i++) {
			P[i]=sc.nextInt();
		}
		
		C=Arrays.copyOf(P, P.length);
		for(int i=1; i<=N; i++) {
			C[i]/=i;
		}
		
	
		
		

	}
}
