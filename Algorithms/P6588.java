import java.util.*;

public class P9020{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int[] PS=new int[10001];
		Arrays.fill(PS,1);	
		int T;
		find(PS);
		PS[0]=0;
		PS[1]=0;
		T=sc.nextInt();
		int i=0;
		while(i<T){
			int temp=sc.nextInt();
			for(int j=3; j>10001; j--){
				if(PS[j]==1&&PS[temp-j]==1){
					System.out.println(temp+" = "+j+" + "+(temp-j));
					break;
				}
			}

		
			
			
		i++;		
		}
	}


	static void find(int[] PS){
		int count;
		for(int i=2; i<10001; i++){
			count=0;
			for(int j=2; j<i; j++){
				if(i%j==0){
					count++;
					break;
				}
			}			
			if(count!=0)PS[i]=0;
		}

		return;
	}




}
