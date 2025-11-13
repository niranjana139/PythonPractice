def divide_numbers(a, b):
    try:
        # Custom check and raise
        if b == 0:
            raise ZeroDivisionError("You can't divide by zero.")

        result = a / b

    except ZeroDivisionError as e:
        print("Exception caught:", e)

    except TypeError:
        print("Both inputs must be numbers.")

    else:
        # Runs only if no exceptions occurred
        print("Division successful! Result is:", result)

    finally:
        # Always runs no matter what
        print("Execution completed.\n")


# Test cases
divide_numbers(10, 2)  # Valid
divide_numbers(10, 0)  # Triggers raise and except
divide_numbers(10, 'a')  # Triggers TypeError
