x = "100"
y = int(x)      # Convert string to integer
z = float(x)    # Convert string to float
a = str(123)    # Convert integer to string
b = bool(1)

# --- Variable Assignment ---
# Declaring variables of different types
num = 10                # Integer
price = 99.99           # Float
name = "Alice"          # String
is_active = True        # Boolean

print("Variable Examples:")
print("num =", num, "| Type:", type(num))
print("price =", price, "| Type:", type(price))
print("name =", name, "| Type:", type(name))
print("is_active =", is_active, "| Type:", type(is_active))

# --- Typecasting ---
print("\nTypecasting Examples:")
x = "123"
print("Original x:", x, "| Type:", type(x))

x_int = int(x)
print("String to int:", x_int, "| Type:", type(x_int))

x_float = float(x)
print("String to float:", x_float, "| Type:", type(x_float))

y = 0
y_bool = bool(y)
print("Integer to bool (0):", y_bool, "| Type:", type(y_bool))

# --- Local and Global Variables ---
print("\nLocal and Global Variable Examples:")

global_var = "I am a global variable"

# Simulating local scope using a block
print("Global variable (outside any block):", global_var)

# Simulating a local variable inside a code block (not a function)
# In Python, blocks don't create scope like functions do
if True:
    local_var = "I am a 'local' variable (in block)"
    print("Inside block:")
    print("Local variable:", local_var)
    print("Accessing global variable inside block:", global_var)

# The so-called local variable is still accessible outside (Python doesn't restrict it like functions)
print("Outside block, accessing local_var:", local_var)

# Modifying a global variable
global_var = "Global variable modified"
print("Modified global variable:", global_var)
