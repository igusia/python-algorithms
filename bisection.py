"""
Author: Iga Rygielska
Date: 17th August 2018

The script returns a root of a chosen polynomial function using the bisection method.
Code is written in Python 3.

How to run a script.

The script can be run from command line.
:Example:

In Linux environment:
>>> python3 alg.py -4 2 100 0.001 1 0 -2 3
-1.8931884765625

Explanation:
- 1st argument (alg.py) - program name
- 2nd argument (-4) - first endpoint of an interval (start value)
- 3rd argument (2) - second endpoint of an interval (start value)
- 4th argument (100) - maximum number of iterations
- 5th argument (0.001) - tolerated accuracy
- 6th - nth argument (1 0 -2 3) - coefficients of a polynomial function
(in order: a_n, ..., a_1, a_0)

In this example the coefficients are:
a3 = 1
a2 = 0
a1 = -2
a0 = 3

And the whole function is: x^3 + 0*x^2 - 2*x + 3.

This implementation manages edge cases and inappropriate inputs.

"""
import math
import sys

def bisection(k, l, nmax, eps, coeffs):
	"""returns a root of a polynomial function given by coefficients (coeffs), 
	starting from endpoints k, l; exits if values of a function on endpoints 
	do not have opposite signs (! f(k)*f(l) < 0)

	:param k: the first endpoint
	:param l: the second endpoint
	:param nmax: max number of iterations
	:param eps: tolerated accuracy of a solution
	:param coeffs: list of coefficients that define a polynomial function

	* tmp - temporary value, used if the first endpoint is bigger than the second one
	and they must be swapped
	* m - the midpoint of the interval, determined in each iteration

	"""
	if f(l, coeffs)*f(k, coeffs) >= 0:
		print("the signs of function values on endpoints are not opposite, exiting")
		sys.exit(0)
	if k>l:
		tmp = k
		k = l
		l = tmp
	n = 1
	while abs(k-l)> eps and n <= nmax:
		m = (k+l)/2.0
		if f(m, coeffs)==0:
			return m
		elif f(m, coeffs)*f(k, coeffs) > 0:
			k=m
		else:
			l=m
		n += 1
	return (k+l)/2.0

def f(x, coeffs):
	"""returns value of a polynomial function given by coefficients (coeffs) in a point (x)

	* ind - index of a coefficient in a coeffs list (begining from a0 -- the last in coeffs)
	* func - value of a function

	"""
	func = 0
	for i in range(len(coeffs)):
		ind = -i-1
		func += coeffs[ind]*x**i
	return func

def verifyArgs():
	"""exits a program if no coefficients were entered

	The first 5 arguments entered are in order: name of a program, start values (k, l),
	max number of iterations and tolerated accuracy of a solution. If there are (at most) 
	these 5 values, the function cannot be specified.

	"""
	if len(sys.argv)<6:
		print("cannot specify a function, no coefficients found, exiting")
		sys.exit(0)

def castFloat():
	"""exits a program if entered values cannot be converted to floats

	Takes all entered arguments except for the first one (program name) and tries to convert 
	them from strings to floats.

	"""
	try:
		return [float(x) for x in sys.argv[1:]]
	except ValueError:
		print("some arguments cannot be converted to float type, exiting")
		sys.exit(0)

def main():
	"""prints found root of a function

	* args - all arguments (start values, max no. of iterations, eps, coefficients)
	* coeffs - coefficients

	"""
	verifyArgs()
	args = castFloat()
	k, l, nmax, eps = args[0:4]
	coeffs = args[4:]
	print(bisection(k, l, nmax, eps, coeffs))

main()
