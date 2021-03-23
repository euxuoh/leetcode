#include <bits/stdc++.h>

using namespace std;


int partition(int arr[], int low, int high) {
    int pivot = arr[low];

    while (low < high) {
        while (low < high && arr[high] >= pivot) {
            high--;
        }
        swap(arr[low], arr[high]);

        while (low < high && arr[low] <= pivot) {
            low++;
        }
        swap(arr[low], arr[high]);
    }

    return low;
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pivot = partition(arr, low, high);
        quick_sort(arr, low, pivot-1);
        quick_sort(arr, pivot+1, high);
    }
}

void printArray(int arr[], int size) {  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};  
    int n = sizeof(arr) / sizeof(arr[0]);  
    quick_sort(arr, 0, n - 1);  
    cout << "Sorted array: \n";  
    printArray(arr, n);  
    return 0;
}
