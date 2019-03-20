import java.util.*;

public class P10806{
	static int N,M;	
	static int[] B;
	static Queue<Integer> q1=new LinkedList<>();
	static Queue<Integer> q2=new LinkedList<>();
	static Queue<Integer> w=new LinkedList<>();
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();	
		B=new int[N+1];
		for(int i=0; i<M; i++){
			int x=sc.nextInt();
			int y=sc.nextInt();
			B[x]+=1;
			B[y]+=1;
		}
		//show();	
		int count=0;			
		for(int i=1; i<=N; i++){
			if(B[i]==0){
				count++;
				q.add(i);	
			}
			if(B[i]==1){
				count++;
				q2.add(i);
			}
			if(B[i]>=2){
				w.add(i);
			}
		}
			
		if(count==0){
			System.out.println(0);
		}
	
	}


	static void show(){
		for(int i=1 ;i<=N; i++){
			System.out.println("B["+i+"] :"+B[i]);
		}
	}
}
