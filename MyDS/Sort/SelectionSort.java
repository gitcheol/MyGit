import java.util.*;


public class SelectionSort{
	static int[] S=new int[]{5,2,3,4,1,6,7,0,11,9};
	
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);	
		Selection();
		for(int i=0; i<S.length;i++){
			System.out.print(S[i]+" ");
		}

	}

	static void Selection(){
		int min;
		int temp=0;
		for(int i=0; i<S.length; i++){
			min=S[i];
			for(int j=i; j<S.length; j++){
				if(S[j]<min){
					temp=S[j];
					S[j]=min;
					min=temp;
				}
			}
			S[i]=min;
		}
	}
}
