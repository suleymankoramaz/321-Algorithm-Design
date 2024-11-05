def inorder(root,nodes):
	if not root:
		return

	inorder(root.left,nodes)
	nodes.append(root)
	inorder(root.right,nodes)


def buildTree(nodes,start,end):
	if start>end:
		return None

	mid=(start+end)//2
	node=nodes[mid]

	node.left=buildTree(nodes,start,mid-1)
	node.right=buildTree(nodes,mid+1,end)
	return node


def balanceTree(root):
	nodes=[]
	inorder(root,nodes)
	n=len(nodes)
	return buildTree(nodes,0,n-1)