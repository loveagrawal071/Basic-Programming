#A simple solution is to find all prime factors of both numbers, then
#find intersection of all factors present in both numbers. Finally
#return product of elements in the intersection.

#An efficient solution is to use Euclidean algorithm which is the main
#algorithm used for this purpose. The idea is, GCD of two numbers
#doesn’t change if smaller number is subtracted from a bigger number.
def gcd(a,b):
	if a==0:
		return b
	if b==0:
		return a
	if a==b:
		return a
	if a>b:
		return gcd(a-b,b)
	return gcd(b-a,a)

print(gcd(36,60))