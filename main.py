#import Functions
from treelib import Node, Tree
# https://treelib.readthedocs.io/en/latest/

tree = Tree()

#Gen 1
elizabeth = tree.create_node("Elizabeth", "elizabeth") # root node

#Gen2
marj = tree.create_node("Marj", "marj", parent=elizabeth)
roseanne = tree.create_node("Roseanne", "roseanne", parent=elizabeth)
ruthanne = tree.create_node("Ruthanne", "Ruthanne", parent=elizabeth)
donnie = tree.create_node("Donnie", "donnie", parent=elizabeth)
patricia = tree.create_node("Patricia", "patricia", parent=elizabeth)

#Gen 3
kim = tree.create_node("Kim", "kim", parent=marj)
monica = tree.create_node("Monica", "monica", parent=marj)
martin = tree.create_node("Martin", "martin", parent=marj)
gabe = tree.create_node("Gabe", "gabe", parent=marj)
john = tree.create_node("John", "john", parent=marj)
ben = tree.create_node("Ben", "ben", parent=marj)
jerome = tree.create_node("Jerome", "jerome", parent=marj)

#Gen 4
johng = tree.create_node("John G", "johng", parent=kim)
jamie = tree.create_node("Jamie", "jamie", parent=kim)
julia = tree.create_node("Julia", "julia", parent=kim)

phil = tree.create_node("Phill", "phil", parent=monica)
alley = tree.create_node("Alley", "alley", parent=monica)
anna = tree.create_node("Anna", "anna", parent=monica)
steven = tree.create_node("Steven", "steven", parent=monica)

ellane = tree.create_node("Ellane", "ellane", parent=gabe)
jake = tree.create_node("Jake", "jake", parent=gabe)

veera = tree.create_node("Veera", "veera", parent=jerome)
precila = tree.create_node("Precila", "precila", parent=jerome)
clarence = tree.create_node("Clarence", "clarence", parent=jerome)

#Gen 5
lincoln = tree.create_node("Lincoln", "lincoln", parent=phil)
##########################################################################
tree.show() #the tree sometimes bugs and prints out muiliple times/ incorrectly regreshing the page usually fixes it
############################################################################

Gen1 = ["Elizabeth"]
#Elizabeth Kids
Gen2 = ["Donnie", "Marj", "Patricia", "Roseanne", "Ruthanne"]
#Marj Kids
Gen3 = ["Kim", "Monica", "Martin", "Gabe", "John", "Ben", 'Jerome']
#I needed to write something here so it doesnt look weird
Gen4 = ["Jamie", "John G", "Julia", "Ellane", "Jake", "Ellane", "Jake", "Clarence", "Precila", "Veera", "Alley", "Anna", "Phil", "Steven"]
#Phill Kids
Gen5 = ["Lincoln"]

########################################################################
#nodes
#test = tree.create_node("Donniex", "donniex", parent=elizabeth)
#print(tree.donn(test.identifier))

#elizabeth = tree.create_node("Elizabeth", "elizabeth")
#print(tree.elizabeth(elizabeth.identifier))

#print(tree.elizabeth)
#print(tree.elizabeth(test.identifier))

##################################################################################

print(" ")
print("Enter 2 people to show their relation")
First = input("Enter first person:")
Second = input("Enter second person:")
print(" ")

#filllinage = (linage[], First)
#if First has parent then
# # filllinage(linage, node.parent)
###########################################################

#Each person is given a value for their gen
if First in Gen1:
      P1 = 1
elif First in Gen2:
      P1 = 2
elif First in Gen3:
      P1 = 3
elif First in Gen4:
      P1 = 4
elif First in Gen5:
      P1 = 5    
else:
      print("Error")
      exit()

if Second in Gen1:
        P2 = 1
elif Second in Gen2:
        P2 = 2
elif Second in Gen3:
        P2 = 3
elif Second in Gen4:
        P2 = 4
elif Second in Gen5:
        P2 = 5
else:
      print("Error")
      exit()

##############################################################################

agegap = (P1 - P2)
  
print(f"{agegap}")

  #Persons 2 relation to person 1 The print lines are just for show so we dont get confused

if agegap > 1:
      xgreat = agegap - 2
      print("Great "*xgreat , "Grandparents")
  
elif agegap == 1:
      print("Parent/Parent's Siblings")
  
elif agegap == 0:
      print("Siblings/Cousins")
  
elif agegap == -1:
      print("Child")
  
elif agegap < -1:
    xgreat = (agegap + 2)*(-1)
    print("Great "*xgreat , "Grandchild")
  
else:
    print("Please enter a name from the diagram")
    exit()
    

#print(f"{Second} is {First}'s {relation}")