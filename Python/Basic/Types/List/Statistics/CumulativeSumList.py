# Previous input
a = [float(x.strip()) for x in input("Enter numbers (comma-separated): ").split(",") if x.strip()]

# Process
def cumulative_Sum_List(a):
    res = []
    current_sum = 0.0
    for x in a:
        current_sum += x
        res.append(current_sum)
    return res

# Post process
print("Cumulative sum list:", cumulative_Sum_List(a))
