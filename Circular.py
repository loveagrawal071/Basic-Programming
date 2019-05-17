class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class cirlinklst:
	def __init__(self):
		self.head=None
def insnode(lst,data):
	if lst.head==None:
		lst.head=node(data)
		lst.head.next=lst.head
	else:
		temp=lst.head
		while(temp.next!=lst.head):
			temp=temp.next
		nnode=node(data)
		temp.next=nnode
		nnode.next=lst.head
def printlst(lst):
	temp=lst.head
	while temp.next!=lst.head:
		print(temp.data)
		temp=temp.next
	print(temp.data)
lst=cirlinklst()
insnode(lst,10)
insnode(lst,20)
insnode(lst,30)
insnode(lst,40)
insnode(lst,50)
insnode(lst,60)
printlst(lst)

