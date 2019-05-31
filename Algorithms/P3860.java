import java.util.*:
 

public class vP3860{
	static int[][] B;
	static int W,H;
	static int G;
	static int X,Y;
	static int X1,Y1,X2,Y2,T;
	static int[] time;
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		W=sc.nextInt();
		H=sc.nextInt();
		B=new int[H][W]
		G=sc.nextInt();
		for(int i=0; i<G; i++){
			X=sc.nextInt();
			Y=sc.nextInt();
			B[Y][X]=10001;
		}

		E=sc.nextInt();
		E=new int[E];
		for(int i=0; i<E;i++){
			X1=sc.nextInt();
			Y1=sc.nextInt();
			X2=sc.nextInt();
			Y2=sc.nextInt();
			T=sc.nextInt();
			B[Y1][X1]=100000;
			B[Y2][X2]=100003;
			
			
		}
	
	}
}
