import java.util.*;
import java.io.*;

class Graph{
	private int V;
	private LinkedList<Integer> adj[];

	Graph(int v){
		V=v;
		adj=new LinkedList[v];
		for(int i=0; i<v; i++){
			adj[i]=new LinkedList();
		}
	}

	void addEdge(int v, int w){adj[v].add(w);}

	void BFS(ins s){
		boolean visite[]=new boolean[V];
		LinkedList<Integer> queue=new LinkedList<Integer?();
		
		visited[s]=true;
		queue.add(s);
		
		while(queue.size()!=0){
			s=queue.poll();
		System.out.print(s+ " ");
	
		Iterator<Integer> i=adj[s].listIterator();
			while(i.hasNext()){
				int n=i.next();
				if(!visiter[n]){
					visited[n]=true;
					queue.add(n);
				}
			}	
		}
	
	}
}





public class P7569{
	static int[][][] B;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N,M,H;
		N=sc.nextInt();
		M=sc.nextInt();
		H=sc.nextInt();
		B=new int[H][M][N];	
		
		for(int i=0; i<H; i++){
			for(int j=0; j<M; j++){
				for(int k=0; k<N; k++){
					B[i][j][k]=sc.nextInt();
				}
			}
		}	
			
		

		



	
	}
		


		void ripe(int num){
			
			
		}
}
