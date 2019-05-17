def pascal_triangle(mylist):
	o=[1]
	for i,v in enumerate(mylist):
		if i!=(len(mylist)-1):
			o.append(mylist[i]+mylist[i+1])
	o.append(1)
	return o
		
	
def solv(n):
	ans=[[1]]
	i=2
	outlist=[1]
	while i<=n:
		outlist=pascal_triangle(outlist)
		ans.append(outlist)
		i=i+1
	print(ans)
solv(3)