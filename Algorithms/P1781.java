import java.util.*;


public class P1781{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);	
		int N;
		N=sc.nextInt();
		int[] B=new int[N+1];
		int index,cup;
		int sum=0;
		
		int temp;
		int min;
		int flag;
		for(int i=1; i<=N; i++){
			index=sc.nextInt();
			cup=sc.nextInt();
			temp=index;
			if(B[index]==0){
				B[index]=cup;
				continue;
			}
			min=B[index];
			flag=0;
			while(temp!=0){
				if(B[temp]<min){
					min=B[temp];
					index=temp;
					flag=1;
				}
				temp--;
			}
			
			if(flag==0)
				B[index]=cup;
			System.out.println("B["+i+"] : "+B[i]);
		}
	
		for(int i=0; i<N+1; i++){
		
		}
	

		for(int i=1; i<=N; i++){
			sum+=B[i];
		}
		System.out.println(sum);
	
	
	}
}
