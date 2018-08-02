# example 1
# an example for a cool input checker for an int

while True:
    try:
        int_input = int(input("Enter an integer:\n"))
        print("The number you have entered is ", int_input, "\n")
        break
    except ValueError:
        print("Error: Please enter an integer\n")
    except:
        print("Aw! snap. Something nasty has happened.")
    finally:
        print("Input success")

# example 2
# an example for sorting a complex dictionary
# using heapq library
import heapq

stock = [12, 24, 28323, 23289, 343, 232, 111, 1, -24234]

# new_stock = max(heapq.nsmallest(1,stock))
st = [
    {"a": 123, "b": 111},
    {"a": 112, "b": 101},
    {"a": 100, "b": 99}
]

print(heapq.nlargest(len(st), st, key=lambda stock: stock["b"]))
