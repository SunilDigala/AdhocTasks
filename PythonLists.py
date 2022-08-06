Sample Input

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print


if __name__ == '__main__':
    N = int(input())

list1 = []
# list1.insert(1,"a")
# print(list1)
for i in range(N):
    s = str(input()).split(" ")
    # print(s)
    if s[0] == "insert":
        list1.insert(int(s[1]), int(s[2]))
    elif s[0] == "remove":
        list1.remove(int(s[1]))
    elif s[0] == 'append':
        list1.append(int(s[1]))
    elif s[0] == 'sort':
        list1.sort()
    elif s[0] == 'pop':
        list1.pop()
    elif s[0] == 'reverse':
        list1.reverse()
    else:
        print(list1)




thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
Marks = [91,92,95,100,86,45,100]
thislist.sort()
print(thislist)

#print second highest
Marks = list(set([91,92,95,100,86,45,100]))
Marks.sort(reverse=1)
print(Marks[1])

#print the difference between first and last mark
print("First Mark is: %d" %Marks[0])
print("Last  Mark is: %d" %Marks[-1])
print("The Difference between 1st and last mark is :%d"%(Marks[0]-Marks[-1]))



#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.\


# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
