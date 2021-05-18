###this is an implemetation of a hashmap in python, the key to how Database indexing,cryptographic hashing, python \
# Dictionaries,associative arrays e.t.c work

##create a placeholder capacity for the hash table
TOTAL_CAPACITY=100
# create a linkedlist class as a bucket container
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None




class HashTable:
    
    def __init__(self):
        self.size=0##default size of each internal array(bucket)
        self.capacity = TOTAL_CAPACITY
        self.bucket=[None]*self.capacity

    ##create a hash function
    def hashf(self,key):
        for ind,val in enumerate(str(key)):
            hashfunc = ind + len(str(key)) ** ord(val)
            ##ensure the hash function is in range of the total capacity in the array
            hashfunc = hashfunc % self.capacity
        return hashfunc

            
    def insert(self, key, value):
        #increase the size of the array        
        self.size += 1
        # 2. Compute index of key
        index = self.hashf(key)
        # Go to the node corresponding to the hash
        node = self.bucket[index]
        # 3. If bucket is empty:
        if node is None:
            # Create a nodelist, add it, return
            self.bucket[index] = Node(key, value)
            return key,value
        # 4. to avoid collision,iterate to the end of the linked list at provided index

        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value

        prev.next = Node(key, value)
    
    
    ##find a value in the hashtable
    def find(self,key):
        # generate hash of the key
        index = self.hashf(key)
        ##access the index of that particular key value pair
        node = self.bucket[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            ##restrict this node to the actual key value pair
            node = node.next
        if node is None:
            return 'value not found'
        else:
            return node.value
      
    
    ##remove an object from the hashtable
    def remove(self,key):
        index = self.hashf(key)
        node = self.bucket[index]
        prev = None
        #Iterate the requested node

        while node is not None and node.key != key:
            prev = node
            ##restrict the node to be our requested node
            node = node.next
        if node is None:
            #no key has been found
            return 'key not found'
        else:
            #reduce the size of the array as a key value pair has been removed
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted key-value pair
            return result


        
        
##create testcases
hashtest=HashTable()
hashfun=hashtest.insert(100,5)
hashfun_1=hashtest.insert('123',7)
hashfun_3=hashtest.insert('entropy','randomness')
print(hashfun)#(100,5)
print(hashtest.find('123'))#7
print(hashtest.remove('entropy'))#randomness



