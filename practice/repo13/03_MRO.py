
# Base class: Yeh sabse pehla room hai jahan treasure (method) dhundha jayega
class Base:
    def greet(self):
        # Yeh method sabse basic hai
        return "Main Base class se hoon!"

# Parent1 class: Yeh Base se cheezen leti hai (inherit karti hai)
class Parent1(Base):
    def greet(self):
        # Parent1 ka apna greet method hai
        return "Main Parent1 class se hoon!"

# Parent2 class: Yeh bhi Base se cheezen leti hai
class Parent2(Base):
    def greet(self):
        # Parent2 ka apna greet method hai
        return "Main Parent2 class se hoon!"

# Child class: Yeh Parent1 aur Parent2 dono se inherit karti hai
class Child(Parent1, Parent2):
    def greet(self):
        # Child ka apna greet method hai
        return "Main Child class se hoon!"

# ---- Code Chalane ka Example ----
# Ek Child object banate hain
child = Child()

# greet method call karo, yeh Child ka greet chalega
print(child.greet())  # Output: Main Child class se hoon!

# MRO dekho: Yeh list batati hai ke Python methods kis order mein dhundta hai
# Child -> Parent1 -> Parent2 -> Base -> object
print(Child.mro())  # Output: [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class '__main__.Base'>, <class 'object'>]

# Agar Child ka greet method na hota, toh Parent1 ka greet chalega
# Agar Parent1 ka bhi na hota, toh Parent2 ka, aur phir Base ka
# Yeh order MRO ke zariye decide hota hai

# ---- MRO Ki Details ----
# MRO ek tarteeb hai jo batati hai ke Python methods ya attributes ko kis order mein dhundta hai
# Jaise treasure hunt mein rooms ka order:
# 1. Pehle Child check hota hai (kyunki yeh apna room hai)
# 2. Phir Parent1 (kyunki Child ne Parent1 ko pehle likha)
# 3. Phir Parent2 (kyunki yeh doosre number par hai)
# 4. Phir Base (kyunki Parent1 aur Parent2 isse inherit karte hain)
# 5. Ant mein object (kyunki sab classes object se inherit karti hain)
# MRO isliye zaroori hai taake koi confusion na ho jab ek hi naam ke methods alag classes mein hon