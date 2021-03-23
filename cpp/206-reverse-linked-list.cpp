#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        ListNode* prev = nullptr;
        ListNode* cur = head;

        while (cur) {
            ListNode* tmpNode = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmpNode;
        }

        return prev;
    }
};