from LinkedList import LinkedList
from Stack import Stack
# 1. Use your linked list code and add a method called reverse() that will reverse the linked list. You can start with making a reversed copy and build up to reversing the linked list "in place" as a strecth goal. For example if your linked list is 3->5->6 your function will return 6->5->3

reverseList = LinkedList()
# add items to the list
reverseList.append(3)
reverseList.append(5)
reverseList.append(6)

# print the lsit
print("List")
reverseList.printList()

# reverse the items in the list
reverseList.reverse()
print("Reversed List")
reverseList.printList()

# add a number to the beginning of the reversd list
print("Prepend 7 to reversed list")
reverseList.prepend(7)
reverseList.printList()
print()
# 2. Write a function called reverse_num() that will reverse an integer using a stack. For example if the integer is 123 your function will return 321, make sure to use a stack!


def reverse_num(num):
    """Reverses an integer"""
    # reverse an integer using a stack
    stack = Stack()

    numString = str(num)
    reverseNum = ""

    for digit in numString:
        stack.push(digit)

    for i in range(len(numString)):
        reverseNum = f"{reverseNum}{stack.peek()}"
        stack.pop()

    try:
        reverseNum = int(reverseNum)
        return reverseNum
    except ValueError:
        raise ValueError("reverse_num expects valid integer input")


print("Reversed Number: 54784534")
print(reverse_num(54784534))
print("Reversed Number: 123456789")
print(reverse_num(123456789))
print()
# 3. Write a recursive function called sum_num that will take in a list and return the sum of all the elements in the list starting. For example if the list is [5, 4, 1] your funtion will return 10. Be sure to use recursion!


def sum_num(num_list, val=0):
    """Recursively sums numbers in an array"""
    if len(num_list) < 1:
        return val

    # increment the value by the last item in the list
    value = val + num_list[-1]
    # remove the last item in the list
    new_list = list(num_list)
    new_list.pop()

    # move on to the next item
    return(sum_num(new_list, value))


print("Add a list: (10, 11, 12)")
add_list = (10, 11, 12)
print(sum_num(add_list))

print("Add a list: (7, 13, 21, 5, 51)")
add_list2 = (7, 13, 21, 5, 51)
print(sum_num(add_list2))
