import java.util.*;

public class P2104{
	static int[] A;
	static int N;
	static long max=0;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		A=new int[N];
		for(int i=0; i<N; i++){
			A[i]=sc.nextInt();
		}
		select(0,N,A);
		System.out.println(max);
				

	}

	static void select(int left,int right, int[] A){
		long min=100001;
		long sum=0;
		int temp=left;
		if(left>=right)return ;
		for(int i=left; i<right; i++){
			sum+=A[i];
			if(min>A[i]){
				min=A[i];
				temp=i;
			}
		}
		sum*=min;
			


		select(left,temp,A);
		select(temp+1,right,A);
		return;
	}



}
