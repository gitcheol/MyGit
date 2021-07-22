import java.util.*;


public class P2342{
	static int ans=0;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		State s=new State();
		int input;
		
		int temp1,temp2;
		do{
			input=sc.nextInt();
			if(input==0)break;
			temp1=move(s.right,input);
			temp2=move(s.left,input);
			
			if(temp1>temp2){
				ans+=move(s.left,input);
				s.left=input;
			}
			else{
				ans+=move(s.right,input);
				s.right=input;
			}
			System.out.println(s.left +" "+ s.right);
		}while(input!=0);			


		System.out.println(ans);
	}

	static int move(int x, int y){
		if(x==y)return 1;
		if(x==0)return 2;
		if(x==1||x==3){
			if(y==2||y==4)return 3;
			else return 4;
		}
        if(x==2||x==4){
            if(y==1||y==3)return 3;
			else return 4;
        }
		return 0;
	}








}

class State{
	int right;
	int left; 
	public State(){
		right=0;
		left=0;
	}
}
