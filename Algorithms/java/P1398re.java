import java.util.*;

public class P1398re{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int T;
		T=sc.nextInt();
		long[] B=new long[8];
		long ans;
		while(0<T){
			ans=0;
			long temp=sc.nextLong();
			for(int i=0; i<8;i++){
				B[i]=0;
				B[i]=temp%100;
//		System.out.println(B[i]);		
				temp/=100;
			}
			for(int i=0; i<8; i++){
				while(B[i]>0){
					if(B[i]>=75){
						B[i]-=50;
						ans+=2;
					}
					if(B[i]>=50){
						B[i]-=25;
						ans+=1;
					}
					if(B[i]==25){
						ans+=1;
						break;
					}
					if(B[i]==26){
						ans+=2;
						break;
					}
					if(B[i]==27){
						ans+=3;
						break;
					}
					if(B[i]==28){
						ans+=4;
						break;
					}
					if(B[i]==29){
						ans+=5;
						break;
					}
					if(B[i]>=10){
						B[i]-=10;
						ans++;
					}
					if(B[i]<10&&B[i]>0){
						B[i]--;
						ans++;
					}
				}
			}
			System.out.println(ans);
			T--;			
		}




	}
}
