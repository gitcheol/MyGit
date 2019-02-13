import java.util.Scanner;


public class P13305{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int i;
    long p;
    long sum=0;
    long result=0;
    int N=sc.nextInt();
    int[] edge=new int[N-1];
    int[] node=new int[N];

    for(i=0; i<N-1;i++){
      edge[i]=sc.nextInt();
    }
    for(i=0; i<N;i++){
       node[i]=sc.nextInt();
    }
    //p를 첫 노드로 초기화
    p=node[0];
    i=0;
    while(i<N){
      //더 작은애 나오면 그때까지 edge합은 현재 min과 곱해서 result에 더해준다.
      if(p>=node[i]){
        result+=p*sum;
        p=node[i];
        sum=0;
      }
      //edge값이 최댓값에 도달하면 끝내준다.
      if(i==N-1){
          result+=p*sum;
        break;
      }
      //다음 도시로 넘어갈 때 마다 edge의 값을 더해준다.
      sum+=edge[i];
      i++;
    }

    System.out.println(result);
  }
}








    // for(i=0; i<N-1; i++){
    //   System.out.print(edge[i]+" ");
    // }
    // System.out.print("\n");
    // for(i=0; i<N; i++){
    //   System.out.print(node[i]+" ");
    // }
