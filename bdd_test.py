from boolalg.bdd.bdd import BDD
from boolalg.utils import process
from boolalg.visualisation.visualisation import show_tree

print("RULES FOR ENTERING EQUATION")
print("1. Enter everything in lowercase, without spaces.")
print("2. Use SOP form only.")
print("3. To denote NOT a, use `a'`")
print("-"*10)

print("Enter equation:")
a = input()
a = process(a)

print("Enter order: ")
print("Enter order as a comma seperated string. For example, if you want order as c<b<a, enter 'c, b, a'")
print("-"*10)
order = input()

bdd = BDD()
bdd.generate(a, order)
bdd.print_all()

show_tree(bdd)