import java.util.*;

public class Ex{
	public static void main(String[] args){
		int A,B;
		long C=0;
		Scanner sc=new Scanner(System.in);
		A=sc.nextInt();
		B=sc.nextInt();
		for(int i=0; i<=200000000; i++){
			C++;
			for(int j=0; j<=2000000000; j++){
				C++;	
			}

		}	
		System.out.println(A+B);
		

	}
}
