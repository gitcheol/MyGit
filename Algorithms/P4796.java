import java.util.Scanner;
import java.util.Iterator;
import java.util.ArrayList;


public class P4796{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int[] ans=new int[1000];
		int num=0;
		int L,P,V;
		while(true){
			L=sc.nextInt();
			P=sc.nextInt();
			V=sc.nextInt();
			int sum=0;
			int[] M=new int[V+1];
			if(L==0)break;
			for(int i=1; i<=V; i++){
				if(i%P<L)M[i]=1;
			}
			for(int i=0; i<=V; i++){
				sum+=M[i];
			} 	
			ans[num++]=sum;
		}	
		for(int i=0; i<num; i++){
		
			System.out.println("Case 1: "+ans[i]);
		}
		return ;
	}
}

		
