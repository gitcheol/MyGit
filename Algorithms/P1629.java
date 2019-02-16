import java.util.*;

public class P1629{
	public static void main(String[] args){
	Scanner sc=new Scanner(System.in);
	long A,B,C;
	A=sc.nextLong();
	B=sc.nextLong();
	C=sc.nextLong();
	long ans=0;
	for(int i=0; i<B; i++){
		A*=A;
		if(A>C){
			ans=A%C;
			break;
		}
	}	
	System.out.println(ans);
	}
}
