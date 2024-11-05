def find(root, k1, k2):
	if root is None:
		return

	if k1 < root.data :
		find(root.left, k1, k2)

	if k1 <= root.data and k2 >= root.data:
		print (root.data,end=' ')

	find(root.right, k1, k2)