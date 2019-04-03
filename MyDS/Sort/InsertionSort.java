import java.util.*;

public class InsertionSort{
	static int[] S=new int[]{5,2,3,4,1,6,7,0,11,9};
        
	public static void main(String[] args){
                Scanner sc=new Scanner(System.in);
                insertion();
                for(int i=0; i<S.length;i++){
                        System.out.println(S[i]+" ");
                }

        }
	
	static void insertion(){
		int temp;
		for(int i=0; i<S.length; i++){
			for(int j=i; j<S.length; j++){
				if(S[i]>S[j]){
					temp=S[i];
					S[i]=S[j];
					S[j]=temp;
				}
			}
		}
	
	}
		
	
}
