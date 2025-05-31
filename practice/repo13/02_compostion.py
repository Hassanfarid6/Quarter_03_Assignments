
# ---- Composition ka Example ----
# Composition ek strong "has-a" relationship hai
# Jaise ek Car ke andar Engine hota hai, aur agar Car khatam ho jaye toh Engine bhi khatam
class Engine:
    # Yeh Engine class hai jo batata hai ke engine kaisa hai
    def __init__(self, type):
        self.type = type  # Engine ka type, jaise Petrol ya Diesel

    def start(self):
        # Engine start hone ka message
        return f"{self.type} engine start ho gaya!"

class Car:
    # Car ke andar Engine rakha jata hai (composition)
    def __init__(self, name, engine_type):
        self.name = name
        # Car ke andar ek Engine object banaya, jo Car ka hissa hai
        self.engine = Engine(engine_type)  # Composition: Engine Car ke baghair nahi hai

    def start_car(self):
        # Car ka engine start karo
        return f"{self.name} bol rahi hai: {self.engine.start()}"

# ---- Aggregation ka Example ----
# Aggregation ek loose "has-a" relationship hai
# Jaise ek School ke andar Students hote hain, lekin students School ke baghair bhi reh sakte hain
class Student:
    # Yeh Student class hai jo batata hai ke student ka naam kya hai
    def __init__(self, name):
        self.name = name

    def introduce(self):
        # Student apna introduction deta hai
        return f"Main {self.name} hoon, ek student!"

class School:
    # School ke andar Students ka list hota hai (aggregation)
    def __init__(self, name):
        self.name = name
        # Yeh students ka list hai, jo School ke baghair bhi zinda reh sakta hai
        self.students = []  # Aggregation: Students alag se bhi exist kar sakte hain

    def add_student(self, student):
        # Ek student ko school mein add karo
        self.students.append(student)

    def show_students(self):
        # School ke sab students ke introduction print karo
        if self.students:
            return f"{self.name} ke students: {[student.introduce() for student in self.students]}"
        else:
            return f"{self.name} mein koi student nahi hai!"

# ---- Code Chalane ka Example ----
# Composition ka test
car = Car("Toyota", "Petrol")  # Ek Car banayi jismein Petrol Engine hai
print(car.start_car())  # Output: Toyota bol rahi hai: Petrol engine start ho gaya!

# Aggregation ka test
student1 = Student("Ali")  # Ek student banaya
student2 = Student("Sana")  # Dusra student banaya
school = School("ABC School")  # Ek school banaya
school.add_student(student1)  # Ali ko school mein add kiya
school.add_student(student2)  # Sana ko school mein add kiya
print(school.show_students())  # Output: ABC School ke students: ['Main Ali hoon, ek student!', 'Main Sana hoon, ek student!']

# ---- Composition vs. Inheritance ----
# Composition: Car ke andar Engine "rakha" hai (has-a). Engine Car ka hissa hai, aur Car ke baghair nahi.
# Aggregation: School ke andar Students hote hain, lekin students School ke baghair bhi zinda reh sakte hain.
# Inheritance: Yeh ek "is-a" relationship hai, jaise agar Car ek Vehicle hai, toh woh Vehicle ki cheezen inherit karegi.
# Composition zyada flexible hai kyunki tum Engine ya Students ko asani se change kar sakte ho.
# Inheritance mein code kabhi kabhi complicated ho jata hai kyunki classes tightly connected hoti hain.
# Composition kam coupling deta hai, toh code samajhna aur badalna asaan hota hai.