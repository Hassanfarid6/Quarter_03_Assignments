# 12. Static Methods Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c)
# that returns the Fahrenheit value.




class TemperatureConverter:


 # This is a decorator that tells Python to use this method without creating an instance of the class
    @staticmethod
    def celsius_to_fahrenheit(c):

        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(c):

        return (c -32) * 5/9
    
res = TemperatureConverter()
print(f"Temperature in fahrenheit ==  {res.celsius_to_fahrenheit(40)} °f")
print(f"Temperature in Celsius ==  {res.fahrenheit_to_celsius(104)} °C")