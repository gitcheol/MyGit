import java.util.*;

public class P7570{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N;
		N=sc.nextInt();
		int[] B=new int[N+1];
		int cur;
		for(int i=1; i<=N; i++){
			cur=sc.nextInt();
			B[cur]=B[cur-1]+1;	
		}		
		Arrays.sort(B);

		System.out.println(N-B[N]);
	
	}
}
