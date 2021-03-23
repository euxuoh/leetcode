#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* prev = new ListNode(-1);
        prev->next = head;
        ListNode* tmp = prev;

        while (tmp->next && tmp->next->next) {
            ListNode* s = tmp->next;
            ListNode* e = tmp->next->next;

            tmp->next = e;
            s->next = e->next;
            e->next = s;

            tmp = s;
        }
        
        return prev->next;
    }
};
