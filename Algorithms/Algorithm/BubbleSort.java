import java.util.*;


public class BubbleSort{
        static int[] S=new int[]{5,2,3,4,1,6,7,0,11,9};

        public static void main(String[] args){
                Scanner sc=new Scanner(System.in);
                bubble(S);
                for(int i=0; i<S.length;i++){
                        System.out.println(S[i]+" ");
                }
        
        }

        static void bubble(int[] x){
		int temp;
                for(int i=S.length-1; i>=0; i--){
			for(int j=0; j<i; j++){
				if(S[j]>S[j+1]){
					temp=S[j];
					S[j]=S[j+1];
					S[j+1]=temp;
				}

			}
		}

        
        }
}

