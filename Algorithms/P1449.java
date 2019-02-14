import java.util.*;

public class P1449{
	public static void main(String[] args){
		int N,L;
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		L=sc.nextInt();
		int[] P=new int[N];
		for(int i=0; i<N; i++){
			P[i]=sc.nextInt();
		}
		Arrays.sort(P);
		int ans=1;
		int temp=P[0];
		for(int i=1; i<N; i++){
			if(temp+L>P[i])
				continue;
			temp=P[i];
			ans++;
		}
		System.out.println(ans);
		
	}

}
