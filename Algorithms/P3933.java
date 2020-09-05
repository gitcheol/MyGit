package P3933;
import java.util.*;

public class P3933 {
	static int[] mul=new int[182];
	

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Mul(mul);
		int N;
		ArrayList<Integer> anss=new ArrayList<>();
		int ans;
		int temp;
		while(true) {
			ans=0;
			N=sc.nextInt();
			if(N==0)break;
			for(int i=0; mul[i]<=N; i++) {
				for(int j=i; mul[j]<=N; j++) {
					for(int k=j; mul[k]<=N; k++) {
						for(int l=k; mul[l]<=N; l++) {
							temp=mul[i]+mul[j]+mul[k]+mul[l];
							if(N==temp)ans++;
						}
					}
				}
			}
			anss.add(ans);
		}
		for(int i=0; i<anss.size(); i++) {
			System.out.println(anss.get(i));
		}
	}
	
	
	static void Mul(int[] x) {
		for(int i=0; i<x.length; i++) {
			x[i]=i*i;
		}
	}

}

/*
 * 1^2 2^2 3^2 4^2 5^2 
 *
 * 
 */