import java.util.*;

public class P9020{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int T;
		T=sc.nextInt();
		int i=0;
		int[][] ans=new int[T][2];
		while(i<T){
			int temp;
			temp=sc.nextInt();
			int x,y;
			x=temp/2;
			y=temp/2;
			while(true){
//	System.out.println(x+" " +y);
//	break;
				x=make_prime1(x);
				y=make_prime2(y);
				if(x+y==temp)break;
				
				int xx=x;
				x--;
	
				x=make_prime1(x);
				y=make_prime2(y);
				if(x+y==temp)break;
					
				x=xx;
				y++;				

				x=make_prime1(x);
				y=make_prime2(y);
				if(x+y==temp)break;

				x--;
				y++;
			}
			ans[i][0]=x;
			ans[i][1]=y;
			

	

	
			i++;
		}
		for(i=0; i<T; i++){
			System.out.println(ans[i][0]+" "+ans[i][1]);
		}

	}


	static int make_prime1(int x){
		boolean check=true;
		while(check){
			int count=0;
			for(int i=2; i<x; i++){
				if(x%i==0)count++;
			}
			if(count==0){
				check=false;
				return x;
			}			
			x--;
		}	
		return 0;
	}

	static int make_prime2(int y){
		boolean check=true;
		while(check){
			int count=0;
			for(int i=2; i<y; i++){
				if(y%i==0)count++;
			}
			if(count==0){
				check=false;
				return y;
			}			
			y++;
		}	
		return 0;
	}

}
