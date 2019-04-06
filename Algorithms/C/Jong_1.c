#include <stdio.h>

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
	for(i=0; i<=n; i++){
		if(B[i]==0){
			k=i;
			break;
		}
	}
	quickSort(B,0,k-1);

	for(i=0; i<k; i++){
		if(B[i]>S){
			k=i;
			break;
		}			
	}

	for(i=k-1; i>=0 ;i--){
		for(j=0; j<k; j++ ){
			if(B[i]+B[j]<=S&&S-(B[i]+B[j])<S-(x+y)){
				if(B[i]>B[j]){
					x=B[i];y=B[j];
				}else{
					x=B[j];y=B[i];
				}
			}
			if(B[i]+B[j]<=S&&S-(B[i]+B[j])==S-(x+y)){
				if(B[i]>B[j]&&x>y&&B[i]<x){
					x=B[i]; y=B[j];
				}	
			}
		}
	}
	printf("%d %d",y,x);
	return 0;
}
