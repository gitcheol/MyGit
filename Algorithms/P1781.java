import java.util.*;


public class P1781{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);	
		int N;
		N=sc.nextInt();
		Pro[] num=new Pro[N+1];
		int[] count=new int[200001];
		int[] count_2=new int[200001];
		Pro[] sort=new Pro[N+1];
		//init 
		for(int i=0; i<N+1; i++){
			num[i]=new Pro();
		}
		for(int i=0; i<N+1; i++){
			sort[i]=new Pro();
		}
	

		//counting sort
		for(int i=1; i<N+1; i++){
			num[i].dead=sc.nextInt();
			num[i].cup=sc.nextInt();
			count[num[i].dead]++;
			count_2[num[i].cup]++;
		}
		
		for(int i=1; i<200001; i++){
        	count[i]=count[i-1]+count[i];
        	count_2[i]=count_2[i-1]+count_2[i];
		}	
		
		for(int i=1; i<N+1; i++){
			sort[count_2[num[i].cup]]=num[i];
			count_2[num[i].cup]--;
		}
	
		/*
		Pro temp=new Pro();
		for(int i=1; i<N+1; i++){
			temp=num[i];
			num[i]=sort[i];
			sort[i]=temp;
		}
		
		
		
		for(int i=1; i<N+1; i++){
			sort[count[num[i].dead]]=num[i];
			count[num[i].dead]--;
		}
		int sum=0; 
		int lock=1;
		for(int i=1; i<N+1; i++){
			if(lock<=sort[i].dead){
				lock++;
				sum+=sort[i].cup;
			}
		}
		*/

		int[] ans=new int[200001];
		int sum=0;
		int coun;
		for(int i=N; i>=1; i--){
			if(ans[sort[i].dead]==1){
				coun=0;
				while(true){
					if(ans[sort[i].dead-coun]==0||sort[i].dead-coun==0){
						ans[sort[i].dead-coun]=1;
						break;
					}
						coun++;
				}
			}
			ans[sort[i].dead]=1;
		
		}

		for(int i=1; i<N+1; i++){
			System.out.println("ans : " + ans[i]);
			if(ans[i]==1)sum+=sort[i].cup;
		}


		/*
		for(int i=0; i<10; i++){
			System.out.println("count"+i+" : "+count[i]);
		}
	*/	
		for(int i=1; i<N+1; i++){
			System.out.println("Dead : "+sort[i].dead+" Cup : "+sort[i].cup);
		}
		
		System.out.println(sum);	
		






	}


}

class Pro{
	int dead;
	int cup;
}




