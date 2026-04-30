class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        cur_return = head
        cur = l1
        cur2 = l2
        carry = 0

        while cur != None or cur2 != None:
            if not cur:
                val = cur2.val
            elif not cur2:
                val = cur.val
            else:
                val = cur.val + cur2.val

            val += carry
            carry = val // 10
            val = val % 10

            cur_return.next = ListNode(val, None)
            cur_return = cur_return.next

            if cur:
                cur = cur.next
            if cur2:
                cur2 = cur2.next

        if carry:
            cur_return.next = ListNode(carry, None)

        head = head.next
        return head