import art
def add(a, b):
  return a+b
def subt(a, b):
  return a-b
def mult(a, b):
  return a*b
def div(a, b):
  return a/b

# we write without paranthesis/cirBracket so, 
# Means: add is just a name pointing to a function in memory.
# to access we write operations['+'](1,2)  to work
operations={
  '+': add,
  '-': subt,
  '*': mult,
  '/': div
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1= float(input("What's the First number?: "))
    while should_accumulate:
      for symbol in operations:
        print(symbol)
      operation_symbol= input("Pick an operation: ")
      num2= float(input("What's the next number?: "))
      result= operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {result}")

      choice = input(f"Type 'y' to continue calculation with {result}, or type 'n' to start new operation.")
      if choice== 'y':
        num1 = result
      else:
        should_accumulate=False
        print("\n" * 20)
        calculator()

calculator()

