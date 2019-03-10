import java.util.*;

public class P3566{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int min=1000000000;
		int[] S=new int[4];
		int i;
		int n;
		int[][] M;
		for(i=0; i<4; i++){
			S[i]=sc.nextInt();
		}
		n=sc.nextInt();
		M=new int[n][5];
		for(i=0; i<n; i++){
			for(int j=0; j<5; j++){
				M[i][j]=sc.nextInt();
			}
		}
		int k;
		i=0;
		while(i<n){
			k=1;
			int a,b,c,d,e;
			a=M[i][0];b=M[i][1];c=M[i][2];d=M[i][3];e=M[i][4];
			while(true){
				if(S[0]<=M[i][0]&&S[1]<=M[i][1]&&S[2]<=M[i][2]&&S[3]<=M[i][3]){
					break;
				}
				if(S[0]<=M[i][1]&&S[1]<=M[i][0]&&S[2]<=M[i][3]&&S[3]<=M[i][2]){
					break;
				}	
				M[i][0]+=a;
				M[i][1]+=b;
				M[i][2]+=c;
				M[i][3]+=d;
				M[i][4]+=e;
				k++;
			}	
			if(min>M[i][4])min=M[i][4];
			i++;
		}





		System.out.println(min);
//		System.out.println(M[0][0]+" "+M[0][1]);

		
	}
}
