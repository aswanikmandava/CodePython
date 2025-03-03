from LinkedList import LinkedList

mylist = LinkedList()
print("LinkedList print at the beginning")
print(f"Init Length: {len(mylist)}")
mylist.print_list()
# insert a bunch of nodes
for i in range(1, 8):
    mylist.insert_at_head(i)

print("LinkedList print after inserting a bunch of nodes")
print("-------------------------------------------------")
mylist.print_list()
print(f"Final Length: {len(mylist)}")