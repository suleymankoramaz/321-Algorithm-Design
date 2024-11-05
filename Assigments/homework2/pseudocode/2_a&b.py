def height_of_tree(node):
  if node is None:
    return 0
  
  left_side = height_of_tree(node.left)
  right_side = height_of_tree(node.right)
  
  return max(left_side, right_side) + 1
  


def Is_Balanced(node):
  if node is None:
    return True
  left_side = Is_Balanced(node.left)
  right_side = Is_Balanced(node.right)

  height_balance = height_of_tree(node.left) - height_of_tree(node.right)

  return (left_side and right_side and (height_balance <= 1))
