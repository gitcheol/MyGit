package Day12;

public class Kakaocode2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int m,n;
		int[][] T1=new int[][] {
			{0,0,0},{0,0,0},{0,0,0}
		};
		int[][] T2=new int[][] {
			{0,2,0,0,0,2},{0,0,2,0,1,0},{1,0,0,2,2,0}
		};
		int[] answer=new int[2];
		Suolution A=new Suolution();
		answer[0]=A.solution(3, 3, T1);
		answer[1]=A.solution(3, 6, T2);
	}

}

class Suolution {
	  int MOD = 20170805;
	  public int solution(int m, int n, int[][] cityMap) {
	      int answer = 0;
	      
	      
	      
	      
	      
	      return answer;
	  }
	}