import java.util.*;

public class P2606{
	static Computer[] com;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N;
		int P;
		N=sc.nextInt();
		P=sc.nextInt();
		com=new Computer[N+1];
		for(int i=0; i<N+1; i++){
			com[i]=new Computer();
		}		
		com[1].visit=true;
		int x,y;
		int[][] pair=new int[P][2];
		for(int i=0; i<P;i++){
			x=sc.nextInt();
			y=sc.nextInt();
			pair[i][0]=x;
			pair[i][1]=y;
		}
		
		for(int i=0; i<P; i++){
			for(int j=0; j<P; j++){
				if(com[pair[j][0]].visit==true||com[pair[j][1]].visit==true){
					com[pair[j][0]].visit=true;
					com[pair[j][1]].visit=true;
				}
			}
		}
		int ans=0;
		for(int i=2; i<N+1; i++){
			if(com[i].visit==true)
				ans++;	
		}
		System.out.println(ans);
	}

}


class Computer{
	boolean visit;
	public Computer(){
		this.visit=false;
	}

}
