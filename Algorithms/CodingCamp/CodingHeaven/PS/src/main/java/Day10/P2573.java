package Day10;
import java.util.Scanner;

public class P2573 {
	static int N,M;
	static int[][] I;
	static int count=0;
	static int num_ice;
	static int [][] zero;


	public static void main(String[] args) {
		int val=0;
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		I=new int[N][M];
		zero=new int[N][M];
		int num_of_0=0;
		int m;
		
		
		num_ice=(N-2)*(M-2);
		for(int i=0;i<N;i++) {
			for(int j=0; j<M; j++) {
				I[i][j]=sc.nextInt();
			}
		}
		
		for(m=0; m<(M-2)*(N-2);m++) {
			val=rotation();
			
			renewal();
			if(val==4) {
		//		System.out.println(m);
				break;
			}
		}
		rotation();
		renewal();
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M;j++) {
				if(I[i][j]==0)num_of_0++;
			}
		}
		if(num_of_0==N*M||N*M-num_of_0==1) {
			System.out.println(0);
			return ;
		}
		if(val==4) {
			System.out.println(m);
			return;
		}
		
		

	}
	static int rotation() {
		int i,j;
		for(i=1;i<N-1;i++) {
			for(j=1; j<M-1; j++) {
				if(check(i,j)==-1) {
					continue;
				}
				if(check(i,j)==4){
					return 4;
				}
				
				zero[i][j]+=check(i,j);
			}
		}
		return 0;
	}
	
	static int check(int i,int j) {
		count=0;
		if(I[i][j]==0) {
			//그 숫자 자체가 0이면 pass하도록 만들어 줘야된다.
			return -1;
		}
		if(I[i][j+1]==0)count++;
		if(I[i][j-1]==0)count++;
		if(I[i+1][j]==0)count++;
		if(I[i-1][j]==0)count++;

		return count; 
		
	}

	static void renewal() {
		for(int i=1; i<N-1; i++) {
			for(int j=1; j<M-1; j++) {
				I[i][j]-=zero[i][j];
				if(I[i][j]<0)I[i][j]=0;
				zero[i][j]=0;
			}
		}
	}
	

	
	
	
	
	
	
	
}

//show
//for(i=0;i<N;i++) {
//	for(j=0; j<M; j++) {
//		System.out.print(I[i][j]+" ");
//	}
//System.out.print("\n");
//}	


//마지막 1개인 경우 
//for(int i=0; i<N; i++) {
//	for(int j=0; j<M; j++) {
//		if(I[i][j]==0)k++;
//	}
//}
//if(N*M-k==1) {
//	System.out.println(0);
//	return ;
//}
