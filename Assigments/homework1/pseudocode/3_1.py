def inorder(root, arr = []):
	if root:
		inorder(root.left, arr)
		arr.append(root.val)
		inorder(root.right, arr)

def merge_sorted_arr(arr1, arr2):
	arr = []
	i = j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	while i < len(arr1):
		arr.append(arr1[i])
		i += 1
	while i < len(arr2):
		arr.append(arr2[j])
		j += 1
	return arr

def arr_to_bst(arr):
	if not arr:
		return None
	mid = len(arr) // 2
	root = Node(arr[mid])
	root.left = arr_to_bst(arr[:mid])
	root.right = arr_to_bst(arr[mid + 1:])
	return root

def merge_two_bst(root1, root2):
	arr1 = []
	arr2 = []
	inorder(root1, arr1)
	inorder(root2, arr2)
  arr = merge_sorted_arr(arr1, arr2)
  return arr_to_bst(arr)