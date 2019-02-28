import java.util.*;

public class P3566{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int min=1000000;
		int[] S=new int[4];
		int n;
		int[][] M;
		for(int i=0; i<4; i++){
			S[i]=sc.nextInt();
		}
		n=sc.nextInt();
		M=new int[n][5];
		for(int i=0; i<n; i++){
			for(int j=0; j<5; j++){
				M[i][j]=sc.nextInt();
			}
		}
		
		for(int i=0; i<n; i++){
			int p_w=M[i][0];
			int p_h=M[i][1];
			int width=M[i][2];
			int height=M[i][3];
			int price=M[i][4];				
			for(int j=1; j<=100;j++){
				if((p_w>=S[0])&&(p_h>=S[1])&&(width>=S[2])&&(height>=S[3])){
					if(min>price)min=price;
					break;
				}
				if((p_h>=S[0])&&(p_w>=S[1])&&(width>=S[3])&&(height>=S[2])){
					if(min>price)min=price;
					break;
				}
				width+=M[i][2];
				height+=M[i][3];
				price+=M[i][4];				
				p_w+=M[i][0];
				p_h+=M[i][1];
			} 

	
		}


		System.out.println(min);

		
	}
}
