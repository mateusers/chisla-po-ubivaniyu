print("Добро пожаловать в вычисление матриц!")
operacia = input("Вас интересует сложение или умножение матриц?\nЕсли сложение, то введите: +\nЕсли умножение, то введите: *\n")
x = int(input("1 число 'первой' матрицы:  "))
y = int(input("2 число 'первой' матрицы:  "))
z = int(input("3 число 'первой' матрицы:  "))
m = int(input("4 число 'первой' матрицы:  "))
n = int(input("5 число 'первой' матрицы:  "))
s = int(input("6 число 'первой' матрицы:  "))
a = int(input("7 число 'первой' матрицы:  "))
b = int(input("8 число 'первой' матрицы:  "))
c = int(input("9 число 'первой' матрицы:  "))
print("Вид 'первой' матрицы:")
print(x, y, z)
print(m, n, s)
print(a, b, c)
print("Значения второй марицы")
X = int(input("1 число 'второй' матрицы:  "))
Y = int(input("2 число 'второй' матрицы:  "))
Z = int(input("3 число 'второй' матрицы:  "))
M = int(input("4 число 'второй' матрицы:  "))
N = int(input("5 число 'второй' матрицы:  "))
S = int(input("6 число 'второй' матрицы:  "))
A = int(input("7 число 'второй' матрицы:  "))
B = int(input("8 число 'второй' матрицы:  "))
C = int(input("9 число 'второй' матрицы:  "))
print("Вид 'второй' матрицы:")
print(X, Y, Z)
print(M, N, S)
print(A, B, C)
if operacia == "+":
	x1 = x+X
	y1 = y+Y
	z1 = z+Z
	m1 = m+M
	n1 = n+N
	s1 = s+S
	a1 = a+A
	b1 = b+B
	c1 = c+C
	print("Результат сложения матриц: ") 
	print(x1, y1, z1)
	print(m1, n1, s1)
	print(a1, b1, c1)

if operacia == "*":
	X1 = x*X+y*M+z*A
	Y1 = x*Y+y*N+z*B
	Z1 = x*Z+y*S+z*C
	M1 = m*X+n*M+s*A
	N1 = m*Y+n*N+s*B
	S1 = m*Z+n*S+s*C
	A1 = a*X+b*Y+c*Z
	B1 = a*Y+b*N+c*B
	C1 = a*Z+b*S+c*C
	print("Результат умножения матриц: ")
	print(X1, Y1, Z1)
	print(M1, N1, S1)
	print(A1, B1, C1)
