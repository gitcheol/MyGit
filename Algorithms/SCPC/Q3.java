import java.util.Scanner;

class Q3{
    static int Answer;

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
		int[] B=new int[10001];
		int temp=0;
		for(int i=0; i<10001; i++){
			temp+=i;
			if(temp>10000)break;
			B[temp]=i;
		}

		
		for(int i=1; i<10001; i++){
			if(B[i]!=0){
				temp=i;	
				continue;
			}
			B[i]=B[temp]+B[i-temp];
		
		}
		

	//	for(int i=1; i<30;i++)
	//		System.out.println("B["+i+"] : "+B[i]);

        
        int T = sc.nextInt();
        for(int test_case = 0; test_case < T; test_case++) {
            int Answer = 0;
			int N1=sc.nextInt();
			int N2=sc.nextInt();
			for(int i=N1;i<=N2; i++){
				if(Answer<B[i])Answer=B[i];
			}

            System.out.println("Case #"+(test_case+1));
            System.out.println(Answer);
        }
    }
}
