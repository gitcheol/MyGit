import java.util.*;

public class P10217{
	static P10217Ticket[] B;
	static int min=100000000;
	static int temp=100000000;
	static int N,M,K;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int T;
		int u,v,c,d;
		T=sc.nextInt();
		for(int k=0; k<T;k++){
		min=100000000;
		temp=100000000;
		N=sc.nextInt();	
		M=sc.nextInt();	
		K=sc.nextInt();	
		B=new P10217Ticket[K];
		for(int i=0; i<K;i++)
			B[i]=new P10217Ticket();

		for(int i=0; i<K;i++){
			B[i].u=sc.nextInt();
			B[i].v=sc.nextInt();
			B[i].c=sc.nextInt();
			B[i].d=sc.nextInt();
		}	
		for(int i=0; i<K; i++){
			if(B[i].u==1)
				DFS(B[i].u,B[i].v,B[i].c,B[i].d);
			if(min>temp)min=temp;
		}
		if(min==100000000){
			System.out.println("Poor KCM");
			return;	
		}
		System.out.println(min);
		}
	}

	static void DFS(int u, int v, int c,int cost){	
		//System.out.println("v : "+v+"  N:"+N+"  cost : " + cost);
		if(c>M)return ;
		if(v==N){
			temp=cost;
			return ;
		}
		for(int i=0; i<K; i++){
			if(B[i].u>B[i].v)continue;
			if(v==B[i].u){
				DFS(B[i].u,B[i].v,c+B[i].c,cost+B[i].d);
				//System.out.println("Me :  "+B[i].u+" "+B[i].v+" "+(c+B[i].c)+" "+(cost+B[i].d));
			}
		
		}
		return ;
	
	
	} 


}

class P10217Ticket{
	int u;
	int v;
	int c;
	int d;
	int cost;

	public P10217Ticket(){
		cost=0;
	}

}
