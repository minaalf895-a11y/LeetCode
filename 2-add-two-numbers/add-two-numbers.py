class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum_digits = []
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            sum_digits.append(digit)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        temp_head = ListNode(0)
        curr = temp_head
        
        for num in sum_digits:
            curr.next = ListNode(num)
            curr = curr.next
            
        return temp_head.next
