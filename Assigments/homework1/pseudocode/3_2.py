def kthSmallest(root, k):
	if (root == None):
		return None
	left = kthSmallest(root.left)
	if (left != None):
		return left
	k -= 1
	if (k == 0):
		return root
	return kthSmallest(root.right)