import java.util.*;

public class P2873{
	static int[][] R;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int x,y;
		int check=0;
		x=sc.nextInt();
		y=sc.nextInt();
		R=new int[x][y];
		for(int i=0; i<x; i++){
			if(check%2==0){
				for(int j=0; j<y-1; j++)
					System.out.print("R");
			}else{
				for(int j=0; j<y-1; j++)
					System.out.print("L");	
			}
			if(i==x-1)break;
			System.out.print("D");
			check++;
			if(check%2==1&&i==x-2)break;
		}
	
	
	}

}
