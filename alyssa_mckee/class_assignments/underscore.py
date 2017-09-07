class Underscore(object):
	def map(self, foo, sequ):
		list = []
		for item in sequ:
			list.append(foo(item))
		return list	
	def reduce(self, foo, sequ, initial=None):
		if len(sequ) >0:
			result = sequ[0] if initial == None else initial
			for item in range(1 if initial == None else 0,len(sequ)):
				result = foo(result, sequ[item])
			return result
		return
	#@return list, tuple, string
	#return items for which f(item) is true
	#if function is None return items that are true (?)
	#if item is string or tuple, return same type else retun list
	def filter(self, foo, sequ):
		result = [] if type(sequ)== list else "" if type(sequ) == str else ()
		for item in sequ:
			if foo != None and foo(item):
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
			elif item:
					result += [item] if type(sequ)== list else item if type(sequ) == str else (item,)
		return result
	#I feel AWESOME!
		
		
_ = Underscore()

def add(x):
	return x+x

print(_.map((lambda x: x+x), "Hello"))



print(_.reduce((lambda x,y: x + y),"abcd"))
x = _.filter(None, [-1,0,True,2,False,"false"])
print(x)