#include<iostream>
#include<vector>
using namespace std;
void swap(int *x, int *y){
    int tmp = *y;
    *x = *y;
    *y = tmp;
}


void BubbleSort(vector<int> arr){
    for(int i=0; i<arr.size;i++){
        for(int j =0; i<j ; j++){
            if(arr[i]>arr[j]){
                swap(arr[i],arr[j]);
            }
        }      
    }
}