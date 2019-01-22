import java.util.Scanner;


public class P13305{
  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    int i;
    int N=sc.nextInt();
    int[] edge=new int[N-1];
    int[] node=new int[N];

    for(i=0; i<N-1;i++){
      edge[i]=sc.nextInt();
    }
    for(i=0; i<N;i++){
       node[i]=sc.nextInt();
    }


    


    System.out.println(result);

    // for(i=0; i<N-1; i++){
    //   System.out.print(edge[i]+" ");
    // }
    // System.out.print("\n");
    // for(i=0; i<N; i++){
    //   System.out.print(node[i]+" ");
    // }


  }
}
