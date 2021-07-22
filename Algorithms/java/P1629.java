import java.util.*;

public class P1629{
	static long A,B,C;
	static long ans=1;
	public static void main(String[] args){
	Scanner sc=new Scanner(System.in);
	A=sc.nextLong();
	B=sc.nextLong();
	C=sc.nextLong();
	System.out.println(re(A,B));

	}
	static long re(long n,long k){
		if(k==0)return 1;
		long temp=re(n,k/2);
		long result=temp*temp%C;
		if(k%2==1)result=result*n%C;
		return result;
	}
}
