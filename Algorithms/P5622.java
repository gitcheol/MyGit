import java.util.*;

public class P5622{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int ans=0;
		String N;
		N=sc.nextLine();
		for(int i=0; i<N.length(); i++){
			char temp=N.charAt(i);
			if(temp=='A'||temp=='B'||temp=='C')ans+=3;	
			else if(temp=='E'||temp=='D'||temp=='F')ans+=4;
			else if(temp=='G'||temp=='H'||temp=='I')ans+=5;
			else if(temp=='J'||temp=='K'||temp=='L')ans+=6;
			else if(temp=='M'||temp=='N'||temp=='O')ans+=7;
			else if(temp=='R'||temp=='P'||temp=='Q'||temp=='S')ans+=8;
			else if(temp=='T'||temp=='U'||temp=='V')ans+=9;
			else if(temp=='W'||temp=='X'||temp=='Y'||temp=='Z')ans+=10;
			else ans+=11;
				
				
				
				
				
				
				
				
				
				
		}
		System.out.println(ans);
		
	}
}
