#include <bits/stdc++.h>

using namespace std;


void heapify(int arr[], int start, int end) {
    int parent = start;
    int child = parent * 2 + 1;

    while (child <= end) {
        if (child + 1 <= end && arr[child] < arr[child + 1]) {
            ++child;
        }

        if (arr[parent] > arr[child]) {
            return;
        } else {
            swap(arr[parent], arr[child]);
            parent = child;
            child = parent * 2 + 1;
        }
    }
}

void heapSort(int arr[], int len) {
    // 初始化建堆，i从最后一个非叶子节点开始调整
    for (int i = len / 2 - 1; i >= 0; i--) 
        heapify(arr, i, len-1); 
  
    // One by one extract an element from heap 
    for (int i = len - 1; i > 0; i--) {
        // Move current root to end 
        swap(arr[0], arr[i]);

        // call max heapify on the reduced heap 
        heapify(arr, 0, i-1);
    }
}

void printArray(int arr[], int n) { 
    for (int i=0; i<n; ++i) 
        cout << arr[i] << " "; 
    cout << "\n"; 
}

int main() { 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    cout << "origin array is \n";
    printArray(arr, n);
    heapSort(arr, n); 
  
    cout << "Sorted array is \n"; 
    printArray(arr, n); 
}
