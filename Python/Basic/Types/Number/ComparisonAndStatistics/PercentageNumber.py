# Previous input
part = float(input("Enter part: "))
total = float(input("Enter total: "))

# Process
def Percentage_Number(part, total):
    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")
    return (part / total) * 100

# Post process
print("The percentage is:", Percentage_Number(part, total), "%")
