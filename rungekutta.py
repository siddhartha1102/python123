def dydx(x,y):
	return (x+y)/2
	pass

def rk(x0,y0,x,h):

	n=round((x0-x)/h)
	k1=0
	k2=0
	k3=0
	k4=0
	y=y0
	for t in range(1,n):
		k1=h*dydx(x0,y0)
		k2=h*dydx(x0+h/2,y0+k1/2)
		k3=h*dydx(x0+h/2,y0+k2/2)
		k4=h*dydx(x0+h,y0+k3)
		x0=x0+h
		
	

	num=y+(h*(k1+2*(k2+k3)+k4)/6)
	return num

# Finds value of y for a given x  
# using step size h  
# and initial value y0 at x0. 

x0 = 0
y = 1  
x = 2
h = 0.2
print("x=",x,"y=",y,"x0=",x0,"h=",h)
print("the function is dy/dx=(x+y)/2")
print(rk(x0,y,x,h))



