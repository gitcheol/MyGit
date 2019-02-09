import java.util.*;
public class P2440{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N;
		N=sc.nextInt();
		for(int i=N; i>0; i--){
			for(int k=i;k<N;k++){
				System.out.print(" ");
			}


			for(int j=0; j<i*2-1;j++){
				System.out.print("*");
			}
		System.out.println(" ");
		}

	}



}
