'''
    reverse odd values in linked list
    ip = [1,2,3,4,5,6]
    op = [2,4,6,5,3,1]
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        pass
        
    def insert_item(self, node, data):
        new_node = Node(data)
        new_node.next = node
        node = new_node
        return node
    
    def append(self, node, new_data): 
        new_node = Node(new_data)
        if node is None: 
            node = new_node 
            return node

        last = node
        while last.next: 
            last = last.next
       
        last.next =  new_node
        return node
        
    def print_item(self, head):
        tmp = head
        while tmp:
            print(tmp.data, end='->')
            tmp = tmp.next
        print(" ")
        
def split_odd_even_list(ll):
    cur_item = ll.head
    odd_list = even_list = None
    while cur_item:
        if cur_item.data % 2:
            odd_list = ll.insert_item(odd_list, cur_item.data)
        else:
            even_list = ll.append(even_list, cur_item.data)
            
        cur_item = cur_item.next
        
    return odd_list, even_list

def reverse_odd_in_ll(ll):
    odd_list, even_list = split_odd_even_list(ll)
    current = even_list 
    while current and current.next:
        current = current.next
    
    current.next = odd_list
    return even_list
    
if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.head = None
    for i in range(1, 10):
        ll.head = ll.append(ll.head, i)
    
    # ll.print_item(ll.head)
    result = reverse_odd_in_ll(ll)
    ll.print_item(result)
