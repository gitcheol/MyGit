import java.util.*;

public class P1713{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int N;
		int C;
		N=sc.nextInt();
		C=sc.nextInt();
		int[] S=new int[101];
		int[] SS=new int[101];
		int count;	
		int dupl_count;
		int temp;
		int min;
		int index=0;
		int m=0;

		for(int i=0; i<C; i++){
			temp=sc.nextInt();
			count=0;
			S[temp]+=1;
			SS[i]=temp;
			for(int j=1;j<=100;j++){
				if(S[j]==0)continue;
				count++;
			}
			//	System.out.println("count : " +count);	
                        if(count>N){
                                min=1000;
                                dupl_count=0;
                                for(int j=1; j<=100;j++){
                                        if(S[j]<min&&S[j]!=0){
                                                min=S[j];
                                                index=j;
                                        }
                                }
                                for(int j=1; j<=100;j++)
                                        if(S[j]==min)dupl_count++;
                                if(dupl_count>1){
                                        for(int j=0; i<=100; j++){
                                                if(S[SS[j]]==min){
                                                        S[SS[j]]=0;
                                                        break;
                                                }
                                        }
                                }
                                else {
                                        S[index]=0;
                                }
                        }	
for(int k=1; k<=100; k++){
        if(S[k]==0)continue;
        System.out.print(k+" ");
}
        System.out.println();



		}		
		
	
		for(int i=1; i<=100; i++){
			if(S[i]==0)continue;
			System.out.print(i+" ");
		}
		
	}
}
