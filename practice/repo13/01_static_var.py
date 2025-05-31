# class aur static variables ko Roman Urdu mein samjhaati hai

# Class ek blueprint hai, jaise tum apne favorite toy ka design banate ho
class Pet:
    # Yeh static variable hai, ek shared dabba jo sab pets ke liye ek hi hai
    # Ismein hum ginte hain ke kitne pets banaye gaye
    total_pets = 0

    # Yeh function har naye pet ke banne par chalta hai
    # 'self' har pet ko represent karta hai (jaise uska personal bag)
    # 'name' woh naam hai jo tum pet ko dete ho
    def __init__(self, name):
        # Yeh instance variable hai, har pet ka apna naam jo uske personal bag mein hai
        self.name = name
        # Har naye pet ke banne par shared dabbe (total_pets) mein 1 jod do
        Pet.total_pets += 1

# Ab kuch pets banate hain!
# Har pet ka apna naam hoga, aur har baar total_pets mein 1 jodta jayega
dog = Pet("Buddy")    # Pehla pet, total_pets ab 1 hai
cat = Pet("Whiskers") # Dusra pet, total_pets ab 2 hai
fish = Pet("Bubbles") # Teesra pet, total_pets ab 3 hai

# Har pet ke personal bag se uska naam print karo
print(f"Dog ka naam: {dog.name}")   # Buddy print hoga
print(f"Cat ka naam: {cat.name}")   # Whiskers print hoga
print(f"Fish ka naam: {fish.name}") # Bubbles print hoga

# Shared dabba (total_pets) ki value print karo, jo batata hai kitne pets hain
print(f"Kul pets: {Pet.total_pets}") # 3 print hoga