#include <stdio.h>

// 퀵정렬을 통해서 array B를 sorting해주는 function
void quickSort(int *arr, int left, int right) {
    int pivot, left_temp, right_temp; 
    left_temp = left;
    right_temp = right;
    pivot = arr[left];
    while (left < right) {
        while (arr[right] >= pivot && (left < right)) {
            right--;
        }
        if (left != right) {
            arr[left] = arr[right];
        }
        while (arr[left] <= pivot && (left < right)) {
            left++;
        }
        if (left != right) {
            arr[right] = arr[left];
            right--;
        }
    }
    arr[left] = pivot;
    pivot = left;
    left = left_temp;
    right = right_temp;
    if (left < pivot) quickSort(arr, left, pivot - 1);
    if (right > pivot) quickSort(arr, pivot + 1, right);
}


int B[100001];

int main(){
	int n;
	int S;
	int x=0,y=0;
	int i,j;
	scanf("%d", &n);
	for(i=0; i<n; i++){
		scanf("%d",&B[i]);
	}
	scanf("%d",&S);
	int k;
	//array의 사이즈만큼만 이용하기 위해 k를 0이 나올 때 까지 반복해서 array사이즈를 찾아준다.
	for(i=0; i<=n; i++){
		if(B[i]==0){
			k=i;
			break;
		}
	}
	//quickSort를 하기 위해서 array B를 넣어준다 0과 k-1 은 시작 index와 끝 index이다.
	quickSort(B,0,k-1);

	for(i=0; i<k; i++){
		if(B[i]>S){
			k=i;
			break;
		}			
	}
	//2중 반복문을 통해서 최적화된 x,y pair를 찾는다.
	for(i=k-1; i>=0 ;i--){
		for(j=0; j<k; j++ ){
			//case 1. 차가 더 작은애가 있다면은 S-(B[i]+B[j]) and S-(x+y).를 통해서 값을 비교하고 B의 값이 더 차가 적다면은 x와 y를 교체해준다. 이 때 더 큰 수가 x에 들어갈 수 있도록 해준다.  
			if(B[i]+B[j]<=S&&S-(B[i]+B[j])<S-(x+y)){
				if(B[i]>B[j]){
					x=B[i];y=B[j];
				}else{
					x=B[j];y=B[i];
				}
			}
			//case 2. 차가 만약 같을 때 S-(B[i]+B[j]) ==S-(x+y) 이면 더 큰 값 끼리 비교해줘서 더 큰 값이 작은 숫자가 x,y가 되도록 해준다.
			if(B[i]+B[j]<=S&&S-(B[i]+B[j])==S-(x+y)){
				if(B[i]>B[j]&&x>y&&B[i]<x){
					x=B[i]; y=B[j];
				}	
			}
		}
	}
	//위 반복문을 통해서 구한 결과값을 작은 값, 큰 값 순으로 출력해준다.
	printf("%d %d",y,x);
	return 0;
}
