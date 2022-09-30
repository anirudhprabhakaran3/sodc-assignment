from boolalg.bdd.bdd import BDD
from boolalg.utils import process, pretty_print, order
from boolalg.visualisation.visualisation import show_tree
from boolalg.rules import apply_rules

print("RULES FOR ENTERING EQUATION")
print("1. Enter everything in lowercase, without spaces.")
print("2. Use SOP form only.")
print("3. To denote NOT a, use `a'`")
print("-"*10)

print("Enter equation:")
a = input()
# a = "bce+ce+afe+d"
a = process(a)

print("Enter order: ")
print("Enter order as a comma seperated string. For example, if you want order as c<b<a, enter 'c, b, a'")
print("-"*10)
ordering = input()
# order = "a, b, c, d, e, f"

bdd = BDD()
bdd.generate(a, ordering)
print("BDD has been generated")

pretty_print(order(bdd.reduce()), opt="Reduced function from ROBDD: ")
pretty_print(order(apply_rules(a)), opt="Reduced function from ROBDD: ")

show_tree(bdd)