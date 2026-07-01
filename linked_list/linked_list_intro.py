# Step 1: Create the Node Class
# This is exactly what you had in your prompt. It's the blueprint for every single element in your list.

class Node:
    def __init__(self,data):
        self.data = data # the value of the node
        self.next = None # points to the next node in the list, initialized to None

# Step 2: Create a Linked List Manager Class (Optional but helpful)
# While you can just manually link nodes, creating a wrapper class makes managing the list (like adding elements or printing) much cleaner.

class LinkedList:
    def __init__(self):
        self.head = None # the starting point of the list, initialized to None

    def append(self, data):
        new_node = Node(data) # create a new node with the provided data

        # if the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        # otherwise, traverse to the end of the list and append the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def delete(self, data):
        # 1. If the list is empty, there's nothing to delete
        if not self.head:
            return

        # 2. If the head node itself holds the data to be removed
        if self.head.data == data:
            self.head = self.head.next
            return

        # 3. Traverse the list to find and bypass the target node
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next  # Bypass the target node
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None") # indicates the end of the list



# 1. Create a linked list and add some data
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.delete(50)  # Deleting the last node to test the delete method
my_list.delete(20)  # Deleting a middle node to test the delete method

print("Original List:")
my_list.display()  # Output: 10 -> 20 -> 30 -> None

# 2. Use the reversal logic
# (We adapt your Solution class logic here directly on the head)
prev = None
curr = my_list.head

while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

# 3. Update our list's head to the new reversed head
my_list.head = prev

print("Reversed List:")
my_list.display()  # Output: 30 -> 20 -> 10 -> None
