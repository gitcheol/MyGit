
public class Ex{
	public static void main(String[] argr){
		Q1 Q=new Q1();
		int[] a=new int[]{1,2,3,4,5};
		int[] b=new int[5];
		b=Q.change(a);	
		for(int i=0; i<5; i++){
			System.out.println(b[i]);
		}
		for(int i=0; i<5; i++){
			System.out.println(a[i]);
		}

	}
}

class Q1{
//java에서 배열의 참조값을 넘겨서 값을 변경하면 원래 있던 배열값도 바뀔까.?
	public int[] change(int[] a){
		for(int i=0; i<5; i++){
			a[i]*=2;
	}
	return a;
	}

}
