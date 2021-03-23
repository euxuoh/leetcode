#include <iostream>

using namespace std;


void heapify(int arr[], int start, int end) {
    int parent = start;
    int child = 2 * parent + 1;

    while (child <= end) {
        if (child + 1 <= end && arr[child] < arr[child+1]) {
            child++;
        }
        
        if (arr[parent] > arr[child]) {
            return;
        } else {
            swap(arr[parent], arr[child]);
            parent = child;
            child = 2 * parent + 1;
        }
    }
}

void heap_sort(int arr[], int len) {
    for (int i = len/2-1; i >= 0 ; --i) {
        heapify(arr, i, len-1);
    }

    for (int i = len-1; i > 0; --i) {
        swap(arr[0], arr[i]);
        heapify(arr, 0, i-1);
    }
}

void print_arr(int arr[], int len) {
    for (int i = 0; i < len; ++i) {
        cout << arr[i] << ", ";
    }
    cout << endl;
}

int main() {
    int arr[] = {3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6};
    int length = sizeof(arr) / sizeof(arr[0]);
    print_arr(arr, length);

    heap_sort(arr, length);
    print_arr(arr, length);

    return 0;
}