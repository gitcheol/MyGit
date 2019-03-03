import java.util.*;

public class P1398{
	public static void main(String[] args){
	Scanner sc=new Scanner(System.in);
	int T;
	T=sc.nextInt();
	long ans;
	long[] A=new long[T];
	long price;
	int i;
	long[] C=new long[30];
	long x=1;
	for(i=0; i<28; i=i+3){
		C[i]=x;
		C[i+1]=10*x;
		C[i+2]=25*x;
		x=x*100;
	}
//	for(i=0; i<28;i++){
//		System.out.println(C[i]);
//	}


	i=0;
	while(i<T){
		ans=0;
		price=sc.nextLong();
		for(int j=27;j>=0;j--){
			if(price-C[j]>=0){
				while(true){
					if(price-C[j]>=0){
						price=price-C[j];
						ans++;
					}
					else break;	
				}	
			}
		}		




		A[i]=ans;
		i++;
	} 	
	for(i=0; i<T; i++){
		System.out.println(A[i]);
	}


	}


}
