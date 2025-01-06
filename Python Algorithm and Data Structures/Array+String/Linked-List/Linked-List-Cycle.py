# - - - PROMPT - - -
# LINKED LIST CYCLE
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. 
# Otherwise, return false.

# Defining the Linked List
class ListNode:
    def __init__(self, value=0, next=None):
     self.val = value
     self.next = next 
# Creating Looped Linked List Cycle head = [3,2,0,-4], pos = 1
# Step 1: Create the nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
# Step 2: Link the nodes to form a chain
node1.next = node2 
node2.next = node3  
node3.next = node4  
node4.next = node2


# Creating Looped Linked List Cycle head = [1], pos = -1
# Step 1: Create the node
node5 = ListNode(1)
# Step 2: Link the nodes to form a chain
node5.next = None



def linkedListCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Space Complexity O(1), No extra memory required
# Time Complexity O(n), slow and fast are iterating through the list
# Test head
print(linkedListCycle(node1))
# Output: True
print(linkedListCycle(node5))
# Output: False