#1.Delete the elements in an linked list whose sum is equal to zero
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def deleteZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sum_dict = {0: dummy}
    while head:
        prefix_sum += head.value
        if prefix_sum in prefix_sum_dict:
            prev = prefix_sum_dict[prefix_sum].next
            curr_sum = prefix_sum + prev.value
            while curr_sum != prefix_sum:
                prev = prev.next
                curr_sum += prev.value
            prefix_sum_dict[prefix_sum].next = prev.next
        else:
            prefix_sum_dict[prefix_sum] = head
        head = head.next
        
    return dummy.next
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)
print("Original Linked List:")
printLinkedList(head)
new_head = deleteZeroSumSublists(head)
print("Linked List after Deleting Zero Sum Sublists:")
printLinkedList(new_head)
#2.Reverse a linked list in groups of given size
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def reverseKGroup(head, k):
    def reverseLinkedList(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    while True:
        current_group_start = prev_group_end.next
        current = current_group_start
        for _ in range(k - 1):
            if not current:
                return dummy.next  
            current = current.next
        if not current:
            return dummy.next 
        next_group_start = current.next
        current.next = None  
        reversed_group_start = reverseLinkedList(current_group_start)
        prev_group_end.next = reversed_group_start
        current_group_start.next = next_group_start
        prev_group_end = current_group_start
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1)
current = head
for i in range(2, 9):
    current.next = ListNode(i)
    current = current.next
print("Original Linked List:")
printLinkedList(head)
k = int(input("Enter the size to reverse:"))
new_head = reverseKGroup(head, k)
print(f"Linked List after Reversing in Groups of {k}:")
printLinkedList(new_head)
#3.Merge a linked list into another linked list at alternate positions.
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def mergeAlternate(head1, head2):
    current1 = head1
    current2 = head2
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        current2.next = next1
        current1 = next1
        current2 = next2
def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head2 = ListNode('A')
head2.next = ListNode('B')
head2.next.next = ListNode('C')
head2.next.next.next = ListNode('D')
print("Original Linked List 1:")
printLinkedList(head1)
print("Original Linked List 2:")
printLinkedList(head2)
mergeAlternate(head1, head2)
print("Merged Linked List:")
printLinkedList(head1)
# 4.In an array, Count Pairs with given sum
def countPairsWithSum(arr, target_sum):
    num_dict = {}  
    count = 0
    for num in arr:
        complement = target_sum - num

        if complement in num_dict:
            count += num_dict[complement]
        num_dict[num] = num_dict.get(num, 0) + 1
    return count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = int(input("Enter the target_sum:"))
result = countPairsWithSum(arr, target_sum)
print(f"Number of pairs with sum {target_sum}: {result}")
#5.Find duplicates in an array
def findDuplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
arr = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8, 7]
duplicate_elements = findDuplicates(arr)
if duplicate_elements:
    print("Duplicate elements in the array:", duplicate_elements)
else:
    print("No duplicates found in the array.")
#6.Find the Kth largest and Kth smallest number in an array
def findKthLargestAndSmallest(arr, k):
    arr.sort()  
    kth_smallest = arr[k - 1]  
    kth_largest = arr[-k]  
    return kth_smallest, kth_largest
arr = [12, 3, 1, 2, 45, 22, 56, 8, 9]
k = int(input("Enter the value of k:"))  
kth_smallest, kth_largest = findKthLargestAndSmallest(arr, k)
print(f"{k}th smallest number is: {kth_smallest}")
print(f"{k}th largest number is: {kth_largest}")
#7.Move all the negative elements to one side of the array
def moveNegativesToSide(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
print("Original Array:")
print(arr)
moveNegativesToSide(arr)
print("Array after moving negatives to one side:")
print(arr)
#8.Reverse a string using a stack data structure
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def is_empty(self):
        return len(self.items) == 0
def reverseString(input_string):
    stack = Stack()
    reversed_string = ""
    for char in input_string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
input_string = "I'm studying data science at Edyoda"
reversed_str = reverseString(input_string)
print(f"Original string: {input_string}")
print(f"Reversed string: {reversed_str}")
#9.Evaluate a postfix expression using stack
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")
    def is_empty(self):
        return len(self.items) == 0
def evaluatePostfixExpression(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2  
            stack.push(result)
    return stack.pop()
postfix_expression = "5 3 4 * + 7 -"
result = evaluatePostfixExpression(postfix_expression)
print(f"Postfix Expression: {postfix_expression}")
print(f"Result: {result}")
#10.Implement a queue using the stack data structure
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = [] 
    def enqueue(self, item):
        self.stack1.append(item)
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeue operations:")
print(queue.dequeue())  
print(queue.dequeue())  
queue.enqueue(4)
queue.enqueue(5)
print("Dequeue operations:")
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  