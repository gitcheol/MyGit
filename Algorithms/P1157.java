import java.util.*;

public class P1157{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		String word;
		int[] A=new int[150];
		word=sc.nextLine();
		word=word.toLowerCase();
		for(int i=0; i<word.length();i++){
			char temp=word.charAt(i);
			A[temp]++;
			
		}
		int max=0;
		int index=0;
		int count=0;
		for(int i=0; i<150; i++){
			if(max<A[i]){
				max=A[i];
				index=i;
			}
		}	
		for(int i=0; i<150; i++){
			if(max==A[i])count++;
		}	
		if(count>=2){
			System.out.println("?");
			return ;
		}
		char ans=(char)(index-32);
		System.out.println(ans);
		
	}

}
