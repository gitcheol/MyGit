import java.util.Scanner;

class Sol{
  int P,A;

  boolean prime_check(int x){
    int i;
    for(i=2; i<x; i++){
      if(x%i==0)return false;
    }
    return true;
  }

  boolean fake_check(int p, int a){
    int i;
    int val=1;
    for(i=0; i<p; i++)val*=a;
    if(val%p==a)return true;
    return false;
  }

}

public class P4233{

  public static void main(String[] args){
    Scanner sc=new Scanner(System.in);
    Sol Prob = new Sol();
    boolean p_check,f_check;
    Prob.P=sc.nextInt();
    Prob.A=sc.nextInt();
    p_check=Prob.prime_check(Prob.P);
    f_check=Prob.fake_check(Prob.P,Prob.A);
    System.out.println(f_check);
    // if(f_check==true&&p_check==false)
    //   System.out.println(Prob.P);
    // else System.out.println(Prob.A);
  }


}
