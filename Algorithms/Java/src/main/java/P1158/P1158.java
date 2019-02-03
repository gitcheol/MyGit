package P1158;
import java.util.*;

public class P1158 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N,M;
		N=sc.nextInt();
		M=sc.nextInt();
		int[] P=new int[N+1];
		int[] ans=new int[N];
		Arrays.fill(P, 1);
		P[0]=0;
		int count=0;
		int i=1;
		//전체를 반복해준다.
		while(count!=N){
			int check=0;
			//0이면 넘어가고 check만큼 돌아갈 수 있도록 해준다.
			while(true) {
				if(P[i]==1) {
					check++;
					if(check==M)break;
					i++;
					if(i==N+1)i=1;
					continue;
				}
				i++;
				if(i==N+1)i=1;
			}
			
			P[i]=0;
			ans[count]=i;
			count++;
		}	
		
//		for(int e: P) {
//			System.out.print(P[e]+" ");
//		}
		System.out.print("<");
		for(int e=0; e<N-1; e++) {
			System.out.print(ans[e]+", ");
		}
		System.out.print(ans[N-1]);
		System.out.println(">");
//		System.out.println(" ");
//		System.out.println(count);

	}

}
