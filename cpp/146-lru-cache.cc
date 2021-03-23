#include <bits/stdc++.h>

using namespace std;

struct DoubleListNode {
    int key, value;
    DoubleListNode* prev;
    DoubleListNode* next;
    DoubleListNode(): key(0), value(0), prev(nullptr), next(nullptr) {}
    DoubleListNode(int k, int val): key(k), value(val), prev(nullptr), next(nullptr) {}
};

class LRUCache
{
private:
    unordered_map<int, DoubleListNode*> cache;
    DoubleListNode* head;
    DoubleListNode* tail;
    int size;
    int capacity;

public:
    LRUCache(int capacity): capacity(capacity), size(0) {
        head = new DoubleListNode();
        tail = new DoubleListNode();
        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {
        if (!cache.count(key)) {
            return -1;
        }
        DoubleListNode* node = cache[key];
        move_to_head(node);
        return node->key;
    }

    void put(int key, int val) {
        if (cache.count(key)) {
            DoubleListNode* node = cache[key];
            node->value = val;
            move_to_head(node);
        } else {
            DoubleListNode* node = new DoubleListNode(key, val);
            cache[key] = node;
            add_to_head(node);
            ++size;
            if (size > capacity) {
                DoubleListNode* removed = remove_tail();
                cache.erase(removed->key);
                delete removed;
                --size;
            }
        }
    }

    void remove_node(DoubleListNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void move_to_head(DoubleListNode* node) {
        remove_node(node);
        add_to_head(node);
    }

    void add_to_head(DoubleListNode* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    DoubleListNode* remove_tail() {
        DoubleListNode* node = tail->prev;
        remove_node(node);
        return node;
    }
};
