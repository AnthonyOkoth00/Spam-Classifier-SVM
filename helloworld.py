
def add(num1, num2):
	return num1 + num2
	
def sub(num1, num2):
	return num1 - num2
	
def mult(num1, num2):
	return num1 * num2
	
def div(num1, num2):
	return num1 / num2
	
def main():
	operation = input("what do you want to do? (+, -, *, /)")
	if(operation != "+" or operation != "-" or operation != "*" or operation != "/"):
		#invalid operation
		print("Enter valid operation")
	else:
		var1 = int(input("Enter num1"))
		var2 = int(input("Enter num2"))
		if(operation == "+"):
			print(add(var1, var2))
		elif(operation == "-"):
			print(sub(var1, var2))
		elif(operation == "*"):
			print(mult(var1, var2))
		else:
			print(div(var1, var2)		
main()