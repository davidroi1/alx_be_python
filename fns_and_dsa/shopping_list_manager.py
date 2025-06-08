def operation_of_list(shopping_list_, choice_, element_):
    if choice_ == '1':
        shopping_list_.append(element_)
    elif choice_ == '2':
        try:
            index_of = shopping_list_.index(element_)
        except ValueError:
            print(f"error : {element_} is not in list")
        else:
            del shopping_list_[index_of]
    elif choice_ == '3':
        for item in shopping_list_:
            print(item)
    elif choice_ == '4':
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice != '3':
            element = input('provide the name: ')
        
        operation_of_list(shopping_list, choice, element)
        

if __name__ == "__main__":
    main()