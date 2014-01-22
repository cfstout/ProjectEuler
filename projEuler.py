import math

def gcd(a,b):
	if a<b:
		return gcd(b,a)
	if a%b ==0:
		return b
	temp = a
	a = b
	b = temp%b
	return gcd(a,b)

def genCoprimes(x, y):
	ret = []
	for m in range(1,x):
		for n in range(1,y):
			if n>m:
				break
			if gcd(m,n) == 1:
				ret.append((m,n))
	return ret
	
def numFactors(x):
	ret=0
	for i in range(1,int(x ** .5)+1):
		div,mod = divmod(x,i)
		if mod==0:
			if div== x**.5:
				ret+=1
			else:
				ret+=2
	return ret

def isPrime(x):
	if x > 1 and numFactors(x)==2:
		return True
	else:
		return False
def factorial(n):
	ret = 1
	for i in range(n,1,-1):
		ret*=i
	return ret

def propDiv(n):
	ret=[]
	if n<=1:
		return ret
	ret.append(1)
	for i in range(2,int(n**.5)+1):
		div,mod = divmod(n,i)
		if mod == 0:
			if div == n**.5:
				ret.append(i)
			else:
				ret+=[i,div]
	return ret
		
def isCircularPrime(p):
	ret = True
	for rot in range(1,len(str(p))):
		pos = rot
		strNew = str(p)[pos]
		pos = (pos +1)%len(str(p))
		while(pos != rot):
			strNew+=str(p)[pos]
			pos = (pos +1)%len(str(p))
		if not isPrime(int(strNew)):
			ret = False
			break
	return ret

def isPalindrome(word):
	wordFor = str(word)
	wordBack = wordFor[::-1]
	if(wordFor == wordBack):
		return True
	return False
	
def genPrimes(r):
	x = {val:True for val in range(r+1)}

	x[0]=False
	x[1]=False
	prime=2
	while prime<len(x):
		cur = prime*2
		while cur < len(x):
			x[cur]=False
			cur +=prime
		prime +=1
		while prime < r and x[prime]==False:
			prime+=1
		if prime == r:
			break
	return x

def wordVal(st):
	val = 0
	for c in st:
		val+=ord(c)-64
	return val
	
	
#1
'''
sum = 0
for i in range(1000):
	if (i % 3)==0 or (i % 5) == 0:
		sum += i
print(sum)
'''

#2
'''
sum = 0
cur = 1
prev = 1
while cur < 4000000:
	if cur % 2 == 0:
		sum +=cur
	temp = cur
	cur = cur + prev
	prev = temp
print(sum)
'''

#3
'''
num = 600851475143
div = 2
while div < math.sqrt(num):
	if num % div ==0:
		num = num / div
		div = 2
	else:
		div += 1
print(num)
'''

#4
'''
def palProd(x,y):
	#print(x,y)
	prod = x*y
	prods = str(prod)
	prodr = prods[::-1]
	if(prods == prodr):
		return True
	return False
pals = []
for x in range(100,999):
	for y in range(100,999):
		if palProd(x,y):
			pals.append((x,y))
max = 1
for prod in pals:
	if prod[0] * prod[1]>max:
		max = prod[0]*prod[1]
print(max)
'''

#5
'''
start = 2520
while True:
	works = True
	for i in range(20,2,-1):
		if start % i != 0:
			works = False
			break
	if works:
		break
	start += 20

print(start)
'''

#6
'''
sumsqr = 0
for i in range(101):
	sumsqr+= i*i
sqrsum = 0
for i in range(101):
	sqrsum += i
sqrsum = sqrsum *sqrsum
print(sqrsum-sumsqr)
'''

#7
'''
primes = [2,3,5,7,11,13]
numprimes = 6
cur =17
while numprimes < 10001:
	isPrime = True
	for i in primes:
		if cur % i == 0:
			isPrime=False
			break
	if isPrime:
		primes.append(cur)
		numprimes +=1
	cur +=1
print(primes[-1])
'''

#8
'''
nums = "3167176531330624919225119674426574742355349194934"
nums+="96983520312774506326239578318016984801869478851843"
nums+="85861560789112949495459501737958331952853208805511"
nums+="12540698747158523863050715693290963295227443043557"
nums+="66896648950445244523161731856403098711121722383113"
nums+="62229893423380308135336276614282806444486645238749"
nums+="30358907296290491560440772390713810515859307960866"
nums+="70172427121883998797908792274921901699720888093776"
nums+="65727333001053367881220235421809751254540594752243"
nums+="52584907711670556013604839586446706324415722155397"
nums+="53697817977846174064955149290862569321978468622482"
nums+="83972241375657056057490261407972968652414535100474"
nums+="82166370484403199890008895243450658541227588666881"
nums+="16427171479924442928230863465674813919123162824586"
nums+="17866458359124566529476545682848912883142607690042"
nums+="24219022671055626321111109370544217506941658960408"
nums+="07198403850962455444362981230987879927244284909188"
nums+="84580156166097919133875499200524063689912560717606"
nums+="05886116467109405077541002256983155200055935729725"
nums+="71636269561882670428252483600823257530420752963450"

maxprod = 1
for i in range(995):
	prod = int(nums[i])*int(nums[i+1])*int(nums[i+2])*int(nums[i+3])*int(nums[i+4])
	if prod > maxprod:
		maxprod = prod
print(maxprod)
'''

#9
'''
cP= genCoprimes(50,50)
for x in cP:
	for k in range(1,100):
		m = x[0]
		n = x[1]
		a = k*(m**2 - n**2)
		b = k*(2*m*n)
		c = k*(m**2 + n**2)
		sum = a+b+c
		if sum > 1000:
			break
		if sum == 1000:
			print(a,b,c)
			print(a+b+c)
			print(a*b*c)
'''

#10
'''
x = range(2000001)

x[0]=False
x[1]=False
prime=2
sum = long(0)
while prime<len(x):
	sum += long(prime)
	cur = prime*2
	while cur < len(x):
		x[cur]=False
		cur +=prime
	prime +=1
	while prime <2000000 and x[prime]==False:
		prime+=1
	if prime == 2000000:
		break
print(sum)
'''

#11
'''
nums = []
grid = open('C:\Users\Clayton Stout\Documents\grid.txt', 'r')
for line in grid:
	num = line.strip().split(' ')
	for i in num:
		nums.append(int(i))

index = 0
maxProd =1
while index < 397:
	#right
	if index%20 <17: #can go right
		c = nums[index]*nums[index+1]*nums[index+2]*nums[index+3]
		if c >maxProd:
			maxProd = c
	if index / 20 <17: #can go down
		c = nums[index]*nums[index+20]*nums[index+40]*nums[index+60]
		if c >maxProd:
			maxProd = c
	if index%20 < 17 and index/20 < 17: #can go diagonal UD/LR
		c = nums[index]*nums[index+21]*nums[index+42]*nums[index+63]
		if c >maxProd:
			maxProd = c
	if index%20 < 17 and index/20 > 2:
		c = nums[index]*nums[index+1-20]*nums[index+2-40]*nums[index+3-60]
		if c >maxProd:
			maxProd = c
	index+=1
print(maxProd)
'''

#12
'''
tri = 1
n= 2
x = numFactors(tri)
while x <500:
	tri= n+tri
	n +=1
	x = numFactors(tri)
	print(x)
print(tri)
'''

#13
'''
nums = []
sum = long(0)
n = open('C:\Users\Clayton Stout\Documents\grid.txt', 'r')
for line in n:
	sum += long(line)
print(sum)
'''

#14
'''
def seq(num,steps):
	while num!=1:
		x = num%2
		if x == 0: #even
			num = num/2
		else:
			num = num*3 +1
		steps+=1
	return steps
max=1
n =1
for i in range(1,1000000):
	cur = seq(i,1)
	if cur>max:
		max=cur
		n = i
print(n)
'''

#15
#how many routes through 20x20 grid
'''
def moves(pos, x, y, dict):
	if pos in dict:
		return dict[pos]
	if pos==x*y-1:
		dict[pos]=1
		return 1
	m =0
	if pos%x < x-1:
		m+= moves(pos+1, x, y, dict)
	if pos/y < y-1:
		m+= moves(pos+y,x,y,dict)
	dict[pos]=m
	return m
dict={}
print(moves(0,21,21,dict))
'''

#16
'''
l = long(2**1000)
s = str(l)
sum = 0
for i in range(len(s)):
	sum += int(s[i])
print(sum)
'''

#17
# 1 < x <1000
'''
def writtenNum(x):
	ret = ""
	th = x/1000
	h = (x/100)%10
	t = (x/10)%10
	o = x%10
	tns = x % 100
	T= False
	if tns >10 and tns <=19:
		T = True
	hund= False
	if th >= 1:
		return "onethousand"
	if h >= 1:
		ret += baseNum(h)
		ret += 'hundred'
		hund= True
	if t >= 1 and not T:
		if hund:
			ret += 'and'
			hund =False
		ret += tens(t)
	if T:
		if hund:
			ret += 'and'
			hund = False
		ret += teens(tns)
	if o >=1 and not T:
		if hund:
			ret+='and'
		ret += baseNum(o)
	return ret
		
		

#1 < x < 9
def baseNum(x):
	if x == 1:
		return "one"
	if x == 2:
		return "two"
	if x == 3:
		return "three"
	if x == 4:
		return "four"
	if x == 5:
		return "five"
	if x == 6:
		return "six"
	if x == 7:
		return "seven"
	if x == 8:
		return "eight"
	if x == 9:
		return "nine"

def tens(x):
	if x == 1:
		return "ten"
	if x == 2:
		return "twenty"
	if x == 3:
		return "thirty"
	if x == 4:
		return "forty"
	if x == 5:
		return "fifty"
	if x == 6:
		return "sixty"
	if x == 7:
		return "seventy"
	if x == 8:
		return "eighty"
	if x == 9:
		return "ninety"

def teens(x):
	if x == 11:
		return "eleven"
	if x == 12:
		return "twelve"
	if x == 13:
		return "thirteen"
	if x == 14:
		return "fourteen"
	if x == 15:
		return "fifteen"
	if x == 16:
		return "sixteen"
	if x == 17:
		return "seventeen"
	if x == 18:
		return "eighteen"
	if x == 19:
		return "nineteen"

sum = 0	
for i in range(1,1001):
	sum += len(writtenNum(i))
print(sum)
'''

#20
'''
numString = str(factorial(100))
sum =0
for i in range(len(numString)):
	sum+= int(numString[i])
print sum
'''

#21
'''
def d(n):
	sum = 0
	for x in propDiv(n):
		sum +=x
	return sum
aN = []
for i in range(1,10001):
	a = d(i)
	b = d(a)
	if b == i and a != b:
		aN+= [a]
sum = 0
print(aN)
for num in aN:
	print propDiv(num)
	sum += num
print(sum)
'''

#22
'''
file = open('names.txt', 'r')
names = []
for line in file:
	names += line.strip().split(',')
names.sort()
total=0
for i in range(len(names)):
	strVal = 0
	for s in names[i]:
		strVal+=(ord(s)-64)
	total+=strVal * (i+1)
print(total)
'''

#23
'''
x = {val:True for val in range(1,28124)}
abundant=[]
for i in range(1,28124):
	sum = 0
	for k in propDiv(i):
		sum += k
	if sum > i:
		abundant += [i]

for i in abundant:
	for j in abundant:
		if i + j < 28124:
			#print(i,j)
			x[i+j]=False
sum =0
for i in range(1,28124):
	if x[i] == True:
		sum+=i
print(sum)
'''

#25
'''
this = long(1)
prev = long(1)
cur = 2
while(len(str(this))<1000):
	temp= long(this)
	this = long(this+prev)
	prev = long(temp)
	cur+=1
print(cur)
'''

#26
#recurring cycles in fractions
'''
for d in range (2,1000):
	dec = str(float(1/d))
	'''
	

#27
'''
max = 0
maxA = 0
maxB = 0
for a in range(-1000,1001):
	for b in range(-1000,1001):
		n = 0
		while(isPrime(n**2 + a*n + b)):
			n+=1
		if n > max:
			max = n-1
			maxA=a
			maxB=b
print(maxA*maxB)
'''

#28
#sum of diagonals of 1001 by 1001 spiral
'''
diag = []
for a in range(1001):
	diag.append([])
	for j in range(1001):
		diag[a].append(0)
dir = ['n','e','s','w']
dirI = 0
num = 1
done = False
x,y = 500,500

while(not done):
	if x>1000 or x < 0 or y >1000 or y < 0:
		done = True
		break
	diag[y][x]=num
	num+=1
	nextDir= (dirI+1)%4
	#print(y,x,dir[dirI],dir[nextDir])
	if dir[nextDir]=='e' and diag[y][x+1]==0:
		dirI=nextDir
		x+=1
	elif dir[nextDir]=='s' and diag[y+1][x]==0:
		dirI=nextDir
		y+=1
	elif dir[nextDir]=='w' and diag[y][x-1]==0:
		dirI=nextDir
		x=x-1
	elif dir[nextDir] == 'n' and diag[y-1][x]==0:
		dirI=nextDir
		y=y-1
	else:
		if dir[dirI]=='e':
			x+=1
		elif dir[dirI]=='s':
			y+=1
		elif dir[dirI]=='w':
			x=x-1
		elif dir[dirI]=='n':
			y=y-1
sum = 0
for i in range(1001):
	sum += diag[i][i]
	sum += diag[1000-i][i]
print(sum-1)
'''

#29
'''
seq = []
for a in range(2,101):
	for b in range(2, 101):
		seq+=[a**b]
print(len(set(seq)))
'''

#34
'''
sum = 0
for i in range(3,5000000):
	num = str(i)
	sumDigs=0
	for digit in num:
		sumDigs += factorial(int(digit))
	if sumDigs == i:
		sum += i
print(sum)
'''

#30
'''
sum = 0
for i in range(2, 295246):
	num = str(i)
	sumDigs=0
	for digit in num:
		sumDigs += int(digit)**5
	if sumDigs == i:
		sum +=i
print(sum)
'''

#35
'''
#gen prime table
x = range(1000001)

x[0]=False
x[1]=False
prime=2
primes = []
while prime<len(x):
	primes+=[prime]
	cur = prime*2
	while cur < len(x):
		x[cur]=False
		cur +=prime
	prime +=1
	while prime <1000000 and x[prime]==False:
		prime+=1
	if prime == 1000000:
		break

count = 0
for p in primes:
	if isCircularPrime(p):
		print(p)
		count+=1
print(count)
'''

#36
'''
sum=0
for i in range(1,1000000):
	if(isPalindrome(i)):
		b = bin(i)
		if(isPalindrome(b[2:])):
			sum+=i
print(sum)
'''

#37
#truncatable primes
'''
t=[]
def isTruncatable(p):
	pS = str(p)
	for i in range(1,len(pS)):
		if(not isPrime(int(pS[i:]))):
			return False
	for i in range(1, len(pS)):
		if(not isPrime(int(pS[0:i]))):
			return False
	return True
	
primes = genPrimes(1000000)
sum = 0
for index in range(10,len(primes)):
	if primes[index]:
		if isTruncatable(index):
			sum +=index
print(sum)
'''

#39
# pythagorean triplets
'''
sums={}
cP= genCoprimes(100,100)
for x in cP:
	for k in range(1,100):
		m = x[0]
		n = x[1]
		a = k*(m**2 - n**2)
		b = k*(2*m*n)
		c = k*(m**2 + n**2)
		cur = a+b+c
		if sum == 120:
			print(a,b,c)
		if sum < 1000:
			if sum in sums:
				sums[sum]+=1
			else:
				sums[sum]=1
			
max =1
maxx=12
for x in sums:
	if sums[x]>max:
		max = sums[x]
		maxx=x
print(x, sums[x])
'''

#40
#decimal digits
'''
s=""
for i in range (1,500000):
	s += str(i)
	if(len(s)>1000000):
		break;
print(int(s[1-1])*int(s[9])*int(s[100-1])*int(s[1000-1])*int(s[10000-1])*int(s[100000-1])*int(s[1000000-1]))
'''

#42
#triangle words	
'''
tris = [0,1,3,6]	
file = open("words.txt","r")
words = []
for line in file:
	words += line.strip().split(',')
numT=0
for w in words:
	val=wordVal(w)
	while val > tris[-1]:
		next = len(tris)+tris[-1]
		tris+=[next]
	if val in tris:
		numT+=1
		
print(numT)
'''

#44
#pentagonal numbers
'''
def genPent(r):
	nums = []
	for i in range(1,r+1):
		nums += [i*(3*i-1)/2]
	return nums

pents = genPent(10000)

for i in pents:
	for j in pents:
		if i+j>pents[-1]:
			break
		if math.fabs(i-j) in pents and (i+j) in pents:
			print(i,j)
'''
			
#48
#series addition
'''
sum = 0
for i in range(1, 1001):
	val = str(long(i**i))
	sum += long(val[-11:])
	#if len(val)>15:
	#	sum += long(val[-15:])
	#else:
	#	sum += long(val
print(sum)
'''

#53
#combinatorics
facs={0:1}
tot=1
for i in range(1,101):
	tot*=i
	facs[i]=tot

sum = 0
for n in range(1, 101):
	for r in range(1,101):
		if n<r:
			break
		if facs[n]/(facs[r]*facs[n-r]) > 1000000:
			sum += 1 
print(sum)

	

