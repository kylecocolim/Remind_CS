#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        vector<int> arr;
        ListNode *tmp = head;
        while(tmp){
            arr.push_back(tmp->val);
            tmp = tmp->next;
        }
        tmp = head;
        int idx = 0;
        while(tmp){
            tmp->val = arr[arr.size() -1 - idx];
            idx++;
            tmp = tmp->next;
        }
        
        return head;
    }
};