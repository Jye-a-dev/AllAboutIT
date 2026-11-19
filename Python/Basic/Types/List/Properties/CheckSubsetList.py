# Previous input
sub = [x.strip() for x in input("Enter subset list (comma-separated): ").split(",") if x.strip()]
main_list = [x.strip() for x in input("Enter main list (comma-separated): ").split(",") if x.strip()]

# Process
def is_Subset_List(sub, main_list):
    main_set = set(main_list)
    return all(item in main_set for item in sub)

# Post process
print("The first list is a subset of the second list:", is_Subset_List(sub, main_list))
