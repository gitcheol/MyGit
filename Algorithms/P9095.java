import java.util.*;

public class P9095{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int T;
		T=sc.nextInt();
		int i;
		int[] B=new int[11];
		B[1]=1;
		B[2]=2;
		B[3]=4;
		for(i=4; i<11; i++){
			B[i]=B[i-1]+B[i-2]+B[i-3];
		}

		i=0;
		while(i<T){
			int temp;
			temp=sc.nextInt();
			System.out.println(B[temp]);			
			i++;
		}
	
	}
}
