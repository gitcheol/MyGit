import java.util.Scanner;


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
			if(L==0)break;
			int temp=(V/P)*L;
			if(V%P>L)temp+=L;
			else temp+=V%P; 
			ans[num++]=temp;
		}	
		for(int i=0; i<num; i++){
		
			System.out.println("Case "+(i+1)+": "+ans[i]);
		}
		return ;
	}
}

		
