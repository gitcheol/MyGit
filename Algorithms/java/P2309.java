import java.util.*;

public class P2309{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int[] P=new int[9];
		int sum=0;
		for(int i=0; i<9; i++){
			P[i]=sc.nextInt();
			sum+=P[i];
		}	
		for(int i=0; i<9; i++){
			for(int j=i+1; j<9; j++){
				if(sum-P[i]-P[j]==100){
					P[i]=0; P[j]=0; break;
				}			
			}
			if(P[i]==0)break;		
		}

		Arrays.sort(P);
		for(int i=2; i<9; i++){
			System.out.println(P[i]);
		}
	}
}
