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


		for(int i=1; i<=N; i++){
			index=sc.nextInt();
			cup=sc.nextInt();

			if(B[index]==0){
				B[index]=cup;
				continue;
			}

			min=B[index];
			temp=index;
			while(index!=0){
				if(min>B[index]){
					min=B[index];
					temp=index;
				}
				index--;
			}
			B[temp]=cup;
			//System.out.println("B["+index+"] : "+B[index]);


		}
	
		for(int i=0; i<N+1; i++){
			System.out.println("B["+i+"] : "+B[i]);
		}
	

		for(int i=1; i<=N; i++){
			sum+=B[i];
		}
		System.out.println(sum);
	
	
	}
}
