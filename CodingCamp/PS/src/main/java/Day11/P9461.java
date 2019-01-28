package Day11;
import java.util.Scanner;
import java.util.ArrayList;

public class P9461 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int T;
		long N;
		ArrayList<Long> ans=new ArrayList<>();
		T=sc.nextInt();
		long[] wave=new long[101]; 
		wave[1]=1;
		wave[2]=1;
		wave[3]=1;
		wave[4]=2;
		wave[5]=2;
		
		for(int i=6; i<=100; i++) {
			wave[i]=wave[i-1]+wave[i-5];
		}
		
		for(int i=0; i<T; i++) {
			N=sc.nextInt();
			ans.add(wave[(int)N]);
		//	System.out.println(N);	
		}
		
		for(int i=0; i<T; i++) {
			System.out.println(ans.get(i));
		}
		
		//System.out.println(wave[11]);
	}

}
