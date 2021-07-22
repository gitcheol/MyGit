import java.util.Scanner;
//시간초과
//문자비교: StringUtils 

class Main
{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        int[] ans = new int[1000001];
        int count=0;
        String tmp;
        for(int i=1; i<=N; i++){
            tmp = Integer.toString(i);
            int len=tmp.length();
            count=0;
            for(int j=0; j<len;j++){
                if('3'==tmp.charAt(j)|| '6'==tmp.charAt(j) || '9'==tmp.charAt(j))
                        count+=1;
                }
            ans[i]=ans[i-1]+count;
            
        }
        System.out.println(ans[N]);
    }
}
