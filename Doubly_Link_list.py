class node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
class linklist():
	def __init__(self):
		self.head=None
def ins_at_end(lst,data):
	temp=lst.head
	if temp==None:
		lst.head=node(data)
		lst.head.next=None
		lst.head.prev=None
	else:
		while temp.next!=None:
			temp=temp.next
		temp.next=node(data)
		temp.next.prev=temp
		temp.next.next=None
def ins_atpos(lst,pos,data):
	if pos==1:
		temp=node(data)
		temp.next=lst.head
		temp.prev=None
		lst.head=temp
	else:
		temp=lst.head
		i=pos-2
		while(i):
			temp=temp.next
			i=i-1
		if temp.next==None:
			ins_at_end(lst,data)
		else:
			cur=temp
			temp=node(data)
			nxt=cur.next
			cur.next=temp
			temp.prev=cur
			temp.next=nxt
			nxt.prev=temp
def delnodehead(lst):
	lst.head=lst.head.next
def deltail(lst):
	temp=lst.head
	while(temp.next!=None):
		temp=temp.next
	temp.prev.next=None
def delnodepos(lst,pos):
	temp=lst.head
	if pos==1:
		delnodehead(lst)
	else:
		i=pos-2
		while i:
			temp=temp.next
			i=i-1
		if temp.next.next==None:
			deltail(lst)
		else:
			cur=temp
			temp=cur.next
			nxt=temp.next
			nxt.prev=cur
			cur.next=nxt
def prlist(lst):
	temp=lst.head
	while(temp!=None):
		print(temp.data)
		temp=temp.next
lst=linklist()
ins_at_end(lst,10)
ins_at_end(lst,20)
ins_atpos(lst,3,456)
delnodepos(lst,2)
prlist(lst)
