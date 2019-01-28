package Day11;
import java.util.*;

public class P9455 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		ArrayList<Integer> ans=new ArrayList<>();
		int T;
		int m,n;
		T=sc.nextInt();
		for(int k=0; k<T;k ++) {
			int count=0;
			m=sc.nextInt();
			n=sc.nextInt();
			int[][] G=new int[m][n];
			for(int i=0; i<m; i++) {
				for(int j=0; j<n; j++) {
					G[i][j]=sc.nextInt();
				}
			}
		
			for(int i=0; i<m; i++) {
				for(int j=0; j<n; j++) {
					if(G[i][j]==1) {
						for(int l=i; l<m; l++) {
							if(G[l][j]==0)count++;
						}
					}
				}
			}
			ans.add(count);
		
		

		}
		//출
		for(int i=0; i<ans.size(); i++) {
			System.out.println(ans.get(i));
		}
	}

}
