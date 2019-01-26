package Day10;
import java.util.Scanner;

public class P2573 {
	static int N,M;
	static int[][] I;
	static int count=0;
	static int ans;
	static int num_ice;
	static int num_of_0;


	public static void main(String[] args) {
		int val;
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		I=new int[N][M];
		num_ice=(N-2)*(M-2);
		for(int i=0;i<N;i++) {
			for(int j=0; j<M; j++) {
				I[i][j]=sc.nextInt();
			}
		}	
		//k는 몇 번 돌렸는지 
		for(int k=1;k<=M*N;k++) {
			val=rotation();
			if(val==0) {
				System.out.println(k);
				return ;
			}
			if(val==-1) {
				System.out.println(0);
				return ;
			}
		}
		
		
	}
	//얼음을확인해주고값을 빼준다.
	static int rotation() {
		int i,j;
		num_of_0=0;
		for(i=1;i<N-1;i++) {
			for(j=1; j<M-1; j++) {
				if(check(i,j)==0) {
					return 0;
				}else {
					I[i][j]-=check(i,j);
					if(I[i][j]<0)I[i][j]=0;
					return 1;
				}
			}
		}
		if(num_of_0==num_ice)
		return -1;
		
		return 1000;
	}
	
	static int check(int i,int j) {
		if(I[i][j]==0) {
			num_of_0++;
			return 0;
		}
		if(I[i][j+1]==0)count++;
		if(I[i][j-1]==0)count++;
		if(I[i+1][j]==0)count++;
		if(I[i-1][j]==0)count++;
		
		return count; 
		
	}
	
	
	 
	
	
	
	
	
	
	
}

//show
//for(i=0;i<N;i++) {
//	for(j=0; j<M; j++) {
//		System.out.print(I[i][j]+" ");
//	}
//System.out.print("\n");
//}	
