#Tree application with list
# Left child index is shifted by 2 from the the postition of the root node
# Right index is shifted by 1 from the the postition of the left child


class listTree:
    def __init__(self, lst:list) -> None:
        self.lst = lst

    def left_child_index(self, rootIndex: int = 0) -> int:
        childIndex = 2 * rootIndex +1
        return childIndex
    
    def right_child_index(self, rootIndex: int = 0) -> int:
        childIndex = 2 * rootIndex + 2
        return childIndex
    
    def get_data(self, rootIndex:int):
        if rootIndex in range(len(self.lst)):
            return self.lst[rootIndex]
        return None



_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

tl = listTree(_array)
print(f"rootNode:-> {tl.get_data(0)}")
root_left_child_index = tl.left_child_index(0)
print(f"root_left_child:-> {tl.get_data(root_left_child_index)}")

root_right_child_index = tl.right_child_index(0)
print(f"root_right_child:-> {tl.get_data(root_right_child_index)}")


root_left_left_child_index = tl.left_child_index(root_left_child_index)
print(f"root_left_left_child:-> {tl.get_data(root_left_left_child_index)}")
