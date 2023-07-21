from d010_module import logo 

# Calculator

# Add
def add(n1, n2):
  return n1 + n2
# Subtract
def subtract(n1, n2):
  return n1 - n2
# Multiply
def multiply(n1, n2):
  return n1 * n2
# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)

  repeat = True
  while repeat:
    symbol = input("Which operation do y ou choose?")
    num2 = float(input("What's the next number?: "))
    answer = operations[symbol](num1, num2)
      
    print(f"{num1} {symbol} {num2} = {answer}")
        
    if "y" == input("repeat?").lower():
      num1 = answer
    else:
      repeat = False
      calculator()

calculator()