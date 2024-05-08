information = {}

# Add information
def add_info(key, value):
    information[key] = value

# Get information
def get_info(key):
    return information.get(key, "Information not found.")

# Remove information
def remove_info(key):
    if key in information:
        del information[key]
        print("Information removed successfully.")
    else:
        print("Information not found.")

# Example usage:
def main():
    add_info(input("Enter key: "), input("Enter value: "))
    add_info(input("Enter key: "), input("Enter value: "))
    add_info(input("Enter key: "), input("Enter value: "))

    key_to_retrieve = input("Enter key to retrieve: ")
    print("Name:", get_info(key_to_retrieve))
    key_to_retrieve = input("Enter key to retrieve: ")
    print("Age:", get_info(key_to_retrieve))
    key_to_retrieve = input("Enter key to retrieve: ")
    print("City:", get_info(key_to_retrieve))

    key_to_remove = input("Enter key to remove: ")
    remove_info(key_to_remove)

    key_to_retrieve_after_removal = input("Enter key to retrieve after removal: ")
    print("Age:", get_info(key_to_retrieve_after_removal))

if __name__ == "__main__":
    main()