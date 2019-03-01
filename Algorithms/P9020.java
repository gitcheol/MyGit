import java.util.*;

public class P9020{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int[] PS=new int[10001];	
		int T;
		find(PS);
		int xx;
//	for(int k=0;k<10001;k++){
//		System.out.println(PS[k]);
//	}


		T=sc.nextInt();
		int i=0;
		int x,y;
		int temp;
		int[][] ans=new int[T][2];
		while(i<T){	
			temp=sc.nextInt();
			x=temp/2;
			y=temp/2;
			while(true){
				x=make_prime1(x,PS);
				y=make_prime2(y,PS);
//	System.out.println(x+" " +y);
				if(x+y==temp)break;
				xx=x;
				x--;
				x=make_prime1(x,PS);
				if(x+y==temp)break;
				x=xx;
				y++;
				y=make_prime1(y,PS);
				if(x+y==temp)break;
				x--; y++;
			
			}
			ans[i][0]=x;
			ans[i][1]=y;





			i++;
		}
		for(i=0; i<T; i++){
			System.out.println(ans[i][0]+" "+ans[i][1]);
		}

	}


	static int make_prime1(int x,int[] PS){
		int i=0;
		boolean check=true;
		while(check){
			if(PS[x-i]==1){
				check=false;
				return x-i;
			}	
			i++;
		}
		return 0;
	}

	static int make_prime2(int y,int[] PS){
		int i=0;
		boolean check=true;
		while(check){
			if(PS[y+i]==1){
				check=false;
				return y+i;
			}	
			i++;
		}
		return 0;
	}

	static void find(int[] PS){
		int count;
		for(int i=2; i<10001; i++){
			count=0;
			for(int j=2; j<i; j++){
				if(i%j==0)count++;
			}	
			if(count==0){
				PS[i]=1;
			}
		}

		return;
	}



}
