import java.util.*;

public class P7569{
	static int[][][] B;
	static int N,M,H;
	static int ans=0;
	static Queue<Integer> q=new LinkedList<>();	
	
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		H=sc.nextInt();
		B=new int[H][M][N];	
		int count=0;
		int num=0;
		for(int i=0; i<H; i++){
			for(int j=0; j<M; j++){
				for(int k=0; k<N; k++){
					B[i][j][k]=sc.nextInt();
					if(B[i][j][k]==0)count++;
					if(B[i][j][k]==1){
						num++;q.add(i);q.add(j);q.add(k);
					}	
				}
			}
		}
		if(count==0){
			System.out.println(0);
			return ;
		}	
		int x=0,y=0,z=0;
		count=0;
		while(!q.isEmpty()){
			ans++;
			count=0;
			for(int m=0; m<num; m++){
				x=q.remove();
				y=q.remove();
				z=q.remove();
				count+=change(x,y,z);	
				B[x][y][z]=2;		
			}
			num=count;
		}

                for(int i=0; i<H; i++){
                        for(int j=0; j<M; j++){
                                for(int k=0; k<N; k++){
                                	if(B[i][j][k]==0){
						System.out.println(-1);	
						return ;
					}
				}
                        }
                }
		

		System.out.println(ans-1);
		

	
	}
	
		
	static int change(int i,int j,int k){
		int count=0;
		if(k+1<N&&B[i][j][k+1]==0){
			B[i][j][k+1]=1;
			q.add(i);q.add(j);q.add(k+1);
			count++;
		}		
		if(k-1>=0&&B[i][j][k-1]==0){
			B[i][j][k-1]=1;
			q.add(i);q.add(j);q.add(k-1);
			count++;
		}		
		if(j+1<M&&B[i][j+1][k]==0){
			B[i][j+1][k]=1;	
			q.add(i);q.add(j+1);q.add(k);
			count++;
		}	
		if(j-1>=0&&B[i][j-1][k]==0){
			B[i][j-1][k]=1;
			q.add(i);q.add(j-1);q.add(k);
			count++;
		}		
		if(i+1<H&&B[i+1][j][k]==0){
			B[i+1][j][k]=1;
			q.add(i+1);q.add(j);q.add(k);
			count++;
		}		
		if(i-1>=0&&B[i-1][j][k]==0){
			B[i-1][j][k]=1;
			q.add(i-1);q.add(j);q.add(k);
			count++;
		}
		return count; 		
	}

			
			
}
