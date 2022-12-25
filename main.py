# #  # CREATING SETS WITH HOMOGENEOUS ELEMENTS
# # s={1, 2, 3}
# # print(s)
# # # CREATING SETS WITH HETEROGENEOUS ELEMENTS
# # s1= {1.0, "Hello", (1, 2, 3)}
# # print(s1)
# # # set cannot have duplicates
# # s2= {1, 2, 3, 4, 3, 2}
# # print(s2)
# # # type function
# # print(type(s2))
# # # Add function
# # s.add(4)
# # #update function
# # s.update([5])
# # # discard function
# # s.discard(1)
# #  # remove function
# # s.remove(2)
# set1=set("helloworld")
# #  # pop function
# # set1.pop()
# # print("mc")
# # # clear function
# # set1.clear()
# # # Union of two sets
# A={1,2,3,4}
# B={5,6,7,8}
# # print(A | B)
# # A.union(B)
# # intersection of two sets
# # print(A & B)
# # A.intersection(B)
#  # difference of two sets
# # print(A-B)
# # print(B.difference(A))
# # Symmetric difference of two sets
# # print(A ^ B)
# print(A.symmetric_difference(B))
# # to check presence of certain element
# print("a" in set1)
# print("p" not in set1)
# # frozen sets
# Aa=frozenset([1,2,3,4])
# Bb=frozenset([4,5,6,7])
# Aa.isdisjoint(Bb)
# Aa.difference(Bb)
# Aa | Bb
# # Aa.add(3)    # show error


from tkinter import *
root=Tk()
root.title("boss")
root.geometry("440x440")
# w=Label(text="boss")
# w.pack()
root.mainloop()