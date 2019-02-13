import java.util.*;
/
public class P2231{
	public static void main(String[] args){
	Scanner sc=new Scanner(System.in);
	int N;
	N=sc.nextInt();
	String string_N;
	boolean check_cons=false;
	int ans=0;	

	for(int i=N-1; i>0; i--){
		ArrayList<Integer> temp=new ArrayList<>();
		int temp_sum=0;
		string_N=Integer.toString(i);
		for(int j=0; j<string_N.length();j++){
			temp.add(Character.getNumericValue(string_N.charAt(j)));
			temp_sum+=temp.get(j);
		}
	

		if(i+temp_sum==N){
			ans=i;
//			System.out.println(i);
		}
	}
	if(ans==0){
		System.out.println(ans);
		return ;
	}
	System.out.println(ans);

	}
}
