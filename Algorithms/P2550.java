import java.util.*;

public class P2550{
	static int[] A;
	static int[] B;
	static int N;
	static int[] ans=new int[10001];
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		A=new int[N+1];
		B=new int[N+1];
	for(int i=1; i<=N; i++)
		A[i]=sc.nextInt();
	for(int i=1; i<=N; i++)
		B[i]=sc.nextInt();
	

		
		Arrays.sort(ans);
		for(int i=0; i<=10000; i++){
			if(ans[i]==0)continue;
			System.out.println(ans[i]+" ");
		}
	}

	static int find(int x){
		int i;
		for(i=1; i<=N; i++)
			if(B[i]==x)break;
		return i;
	}

}
