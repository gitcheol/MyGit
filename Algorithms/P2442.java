import java.util.*;

public class P2442{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N;
		N=sc.nextInt();
		for(int i=0; i<N; i++){
			for(int j=N-1-i; j>0; j--){
				System.out.print(" ");
			}
			for(int k=1; k<=2*i+1;k++){
				System.out.print("*");
			}
		
		System.out.println(" ");
		}
	}	


}
