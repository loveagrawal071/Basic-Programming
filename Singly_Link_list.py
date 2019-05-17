class node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linklist:
	def __init__(self):
		self.head=None

def ins_at_end(lst,data):
	if lst.head==None:
		lst.head=node(data)
		lst.head.next=None
	else:
		temp=lst.head
		while(temp.next!=None):
			temp=temp.next
		temp.next=node(data)
def print_list(lst):
	temp=lst.head
	while(temp!=None):
		print(temp.data)
		temp=temp.next
def ins_atpos(lst,pos,data):
	temp=lst.head
	if pos==1:
		nnode=node(data)
		nnode.next=lst.head
		lst.head=nnode
	else:
		i=pos-2
		while(i):
			temp=temp.next
			i=i-1
		nnode=node(data)
		nnode.next=temp.next
		temp.next=nnode

def del_item(lst,data):
	temp=lst.head
	if temp.data==data:
		lst.head=temp.next
	else:
		while(temp.next.data!=data):
			temp=temp.next
		temp.next=temp.next.next

lst=linklist()
ins_at_end(lst,20)
ins_at_end(lst,30)
ins_at_end(lst,40)
ins_at_end(lst,50)
ins_at_end(lst,60)
print_list(lst)
ins_atpos(lst,1,300)
print_list(lst)



