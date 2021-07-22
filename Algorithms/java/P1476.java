import java.util.*;

public class P1476{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		String N;
		N=sc.nextLine();
		int[] P=new int[10];
		int temp;
		for(int i=0; i<N.length(); i++){
			temp=N.charAt(i)-'0';
			P[temp]++;
		}	
		int count=P[6]+P[9];
		
		P[6]=0;
		P[9]=count-count/2;		
		Arrays.sort(P);
		int ans=P[9];
		System.out.println(ans);
	}
}
