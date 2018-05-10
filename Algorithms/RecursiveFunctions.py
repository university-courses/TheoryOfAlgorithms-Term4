# Function of number incrementation
def inc(z):
	return z + 1


# Function of number decrement
def dec(z):
	return z - 1


# 1 - Function of addition of two numbers
def f_plus(x, y):
	if y == 0:
		return x
	if x == 0:
		return y
	if y > 0:
		return f_plus(inc(x), dec(y))
	return f_plus(dec(x), inc(y))


# 2 - Function of subtraction of two numbers
def f_minus(x, y):
	if y == 0:
		return x
	if y > 0:
		return f_minus(dec(x), dec(y))
	return f_minus(inc(x), inc(y))


# 3 - Function of finding minimum of two natural numbers
def f_minimum(x, y):
	if x > y:
		return f_minus(x, f_minus(x, y))
	return f_minus(y, f_minus(y, x))


# 4 - Function of finding maximum of two natural numbers
def f_maximum(x, y):
	if x > y:
		return f_plus(y, f_minus(x, y))
	return f_plus(x, f_minus(y, x))


# 5 - Function of finding modulus of (x - y), x and y are natural numbers
def f_modulus(x, y):
	return f_minus(f_maximum(x, y), f_minimum(x, y))


# 6 - Function of finding remaining of division of two natural numbers
def f_remaining(x, y):
	if x < y:
		return x
	return f_remaining(f_minus(x, y), y)


# 7 - Function of finding fraction of division of two natural numbers
def f_fraction(x, y):
	if x < y:
		return 0
	else:
		return f_plus(1, f_fraction(f_minus(x, y), y))


# 8 - Function of multiplying of two natural numbers
def f_multiply(x, y):
	if y == 0:
		return 0
	if y < 0:
		return -(f_minus(x, f_multiply(x, inc(y))))
	return f_plus(x, f_multiply(x, dec(y)))


# 9 - Function of finding factorial of natural number
def f_factorial(x):
	if x < 2:
		return 1
	return f_multiply(x, f_factorial(x - 1))


# Function of raising x to the power y, x and y are natural
def f_power(x, y):
	if y == 0:
		return 1
	if y > 0:
		return f_multiply(x, f_power(x, y - 1))
