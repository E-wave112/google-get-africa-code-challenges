# def long(arr):
#     arr = sorted(arr)
#     return [i for i in range(1,len(arr)) if arr[i]==arr[i-1]+1]

# print(long([4,2,5,1,3]))
class Tree:
    def​ __init__​(​self​,​ value​,​​children​):
        self​.​value ​=​ value​
        self​.​children ​=​ children
        #we walk the tree by iterating through it, yielding the length of the path ending at each node we encounter, then take the max of that.
        
    def​ longest_path​(​tree​):
        def​ rec​(​current​,​ parent_value​=​0​,​ parent_path_length​=​0​):
            # Get the Length of the longest chain this node is a part of.    
            current_path_length ​=​​(​parent_path_length ​+​​1​ if​ current​.​value ​==​ parent_value ​+​​1​​ else ​​1​)​
            # Emit the length for this node.
            yield​ current_path_length​# Recurse into the children​
            for​ child ​in​ current​.​children​:
                # For each of the descendant nodes, emit their lengths as well
                for​ value ​in​ rec​(​child​,​ current​.​value​,​ current_path_length​):
                    yield​ value​
                    # select the overall maximum length.
        ​return​ max​(*​rec​(​tree​))