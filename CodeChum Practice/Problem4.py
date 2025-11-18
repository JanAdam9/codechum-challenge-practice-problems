#Create a temperature converter that converts between Celsius, Fahrenheit, and Kelvin. The user chooses the conversion type using a menu.

def CelsiusToFahrenheit(c):
    return (c * 9/5) + 32

def CelsiusToKelvin(c):
    return c + 273.15

def FahrenheitToCelsius(f):
    return (f - 32) / (9/5)

def FahrenheitToKelvin(f):
    return FahrenheitToCelsius(f) + 273.15

def KelvinToCelsius(k):
    return k - 273.15

def KelvinToFahrenheit(k):
    return FahrenheitToCelsius(k - 273.15)

def TwoDecimalOutput(s):
    print(f"{s:.2f}")

choice = int(input())
temp = float(input())

if choice == 1:
    TwoDecimalOutput(CelsiusToFahrenheit(temp))
elif choice == 2:
    TwoDecimalOutput(CelsiusToKelvin(temp))
elif choice == 3:
    TwoDecimalOutput(FahrenheitToCelsius(temp))
elif choice == 4:
    TwoDecimalOutput(FahrenheitToKelvin(temp))
elif choice == 5:
    TwoDecimalOutput(KelvinToCelsius(temp))
elif choice == 6:
    TwoDecimalOutput(KelvinToFahrenheit(temp))