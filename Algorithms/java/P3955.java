import java.util.*;

public class P3955{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		//int t=sc.nextInt();
		int K=sc.nextInt();
		int C=sc.nextInt();
		int x=1;
		while((K*x+1)%C!=0){
			x++;
			if(x>=1000000001)break;
		}
		System.out.println((K*x+1)/C);
		
	}

}
