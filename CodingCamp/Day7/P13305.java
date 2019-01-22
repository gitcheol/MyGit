import java.util.Scanner;


public class P13305{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int i,j;
    int result=0;
    int temp=0;
    int N=sc.nextInt();
    int K=N;
    int[] edge=new int[N-1];
    int[] node=new int[N];

    for(i=0; i<N-1;i++){
      edge[i]=sc.nextInt();
    }
    for(i=0; i<N;i++){
       node[i]=sc.nextInt();
    }

    for(;;){
      int Y=0;
      int min=1000000000;
      //가장 작은 값
      for(i=0; i<N; i++){
        //같을수도 있는데 같은거는 > 함으로써 알아서 짤 min
        if(node[i]!=0){
          if(min>node[i]){
            min=node[i];
            temp=i;
          }
          if(node[i]==0)break;
        }
      }
        node[temp]=0;
      //같은 index의 edge(temp)부터 ~ 끝까지 더한 값을 나타내는 반복문 Y
      for(i=temp; i<N-1; i++){
        Y+=edge[i];
        if(edge[i]==0)break;
        edge[i]=0;

      }
      result+=min*Y;

      if(node[temp]==node[0]&&node[0]==0)break;
    }


    System.out.println(result);
    //
    // for(i=0; i<N-1; i++){
    //   System.out.print(edge[i]+" ");
    // }
    // System.out.print("\n");
    // for(i=0; i<N; i++){
    //   System.out.print(node[i]+" ");
    // }


  }
}
