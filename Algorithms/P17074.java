import java.util.*;

public class P17074{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int[] A=new int[N+1];
		int ans=0;
		int count=0;
		int index; 
		for(int i=1; i<=N; i++){
			A[i]=sc.nextInt();
			if(A[i]<A[i-1]){
				count++;
				index=i;
			}
		}


		if(count==2){
			System.out.println(0);
			System.exit(0);
		}
		if(count==0){
			System.out.println(N);
			System.exit(0);
		}
		
		


		System.out.println(ans);



		}		

	
	
	
	}

}
