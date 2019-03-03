import java.util.*;

public class P1398{
	static long[] A;
	static long price1,price2,price;
	public static void main(String[] args){
	Scanner sc=new Scanner(System.in);
	int T;
	T=sc.nextInt();
	long ans;
	A=new long[T];
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
		long temp1=0;
		long temp2=0;
		price=sc.nextLong();
		price1=price;
		price2=price;
		for(int j=27;j>=0;j--){
			if(price-C[j]>=0){
				while(true){
					if(price1-C[j]>=0){
						price1=price1-C[j];
						temp1++;
					}
					else break;
				}

				while(true){
					if(j==0)break;
					if(price2-C[j-1]>=0){
						price2=price2-C[j-1];
						temp2++;
					}
					else break;
				}
	
				if(temp1<temp2){
					ans+=temp1;
					price=price1;
				}else{
					ans+=temp2;
					price=price2;
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
