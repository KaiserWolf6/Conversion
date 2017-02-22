def farenheit(c):
	f = ((c * 9.0)/5.0) + 32.0
	return f

def celsius(f):
	c = ((f - 32.0)* 5.0)/9.0
	return c

print "Ingrese un valor de Farenheit"
c = ""
print farenheit(input(c))
print "Ingrese un valor de Celsius"
f = ""
print celsius(input(f))
