package Day7;
import java.util.Scanner;

public class N1712 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int A,B,C,D,X,i;
		int count=0;
		A=sc.nextInt();
		B=sc.nextInt();
		C=sc.nextInt();
		if(C==B) {
			System.out.println(-1);
			return;
		}
		D=A/(C-B);
		X=D+1;
		
		
		if(X<0) {
			System.out.println(-1);
			return;
		}
		System.out.println(X);
		

	}
}
