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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;

        ListNode* prev = dummy;
        ListNode* end = dummy;

        while (end->next) {
            for (int i = 0; i < k && end; ++i) {
                end = end->next;
            }
            if (end == nullptr) {
                return dummy->next;
            }

            ListNode* start = prev->next;
            ListNode* next_group = end->next;
            end->next = nullptr;
            prev->next = reverseList(start);
            start->next = next_group;

            prev = start;
            end = start;
        }
        
        return dummy->next;
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* cur = head;

        while (cur) {
            ListNode* tmp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = tmp;
        }

        return prev;
    }
};
