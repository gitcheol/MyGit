package Day11;
import java.util.*;

public class P10451 {
	static int[] P;
	static int N;
	static int temp;

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		ArrayList<Integer> ans=new ArrayList<>();
		int T;
		int num=0;
		T=sc.nextInt();
		for(int l=0; l<T; l++) {
			num=0;
			N=sc.nextInt();
			P=new int[N+1];
			for(int i=1; i<=N; i++) {
				P[i]=sc.nextInt();
			}
			//System.out.println(recu());
			//recu
			//System.out.println(recu());
			num=recu();
			ans.add(num);
//			for(int i=1; i<=N; i++) {
//				System.out.println(P[i]);
//			}
//			System.out.println(num);

		}
		//츨
		for(int i=0; i<T; i++) {
			System.out.println(ans.get(i));
		}
	}
	
	static int recu() {
		int count=0;
		for(int i=1;i<=N; i++ ) {
			if(P[i]!=0) {
				count++;
			}
			go(i); 
		}
		return count;
	}
	
	static int go(int x) {
		if(P[x]==0)return 0;
		temp=P[x];
		P[x]=0;
		return go(temp);
	}
	

}
