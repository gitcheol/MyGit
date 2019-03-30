import java.util.*;

public class P1150{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int n,k;
		int[] D;
		n=sc.nextInt();
		k=sc.nextInt();
		int[] M=new int[n+1];
		D=new int[n+1];

		for(int i=1; i<=n;i++){
			D[i]=sc.nextInt();
		}
		Arrays.sort(D);
		
		for(int i=2; i<=n; i++){
			M[i]=D[i]-D[i-1];
		}
		
	for(int i=2; i<=n;i++){
		System.out.print(M[i]+" ");
	}
	System.out.println();
		
		int min=1000000000;
		int count=0;
		int temp;
		for(int i=2; i<=n; i++){
			temp=0;
			for(int j=2; j<=n; j+=2){
				temp+=M[j];
				count++;
				if(count==k)break;	
			}
			if(min>temp)min=temp;
		}
		System.out.println(min);
	}


}
