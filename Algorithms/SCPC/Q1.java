import java.util.*;

class Q1{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int[] B=new int[10000001];
		int T=sc.nextInt();
		int N1,N2;
		int count;

		for(int i=2; i<10000001; i++){
			count=0;
			if(i%2==1)count=(B[(i+1)/2]+2);
			else count=(B[i/2]+1);
			B[i]=count;
		}

		for(int i=1; i<10000001; i++){
			B[i]=B[i]+B[i-1];
		}
		for(int test_case=0; test_case<T; test_case++){
			N1=sc.nextInt();
			N2=sc.nextInt();
			System.out.println("Case #"+(test_case+1));	
			System.out.println(B[N2]-B[N1-1]);
		}
	}
}
