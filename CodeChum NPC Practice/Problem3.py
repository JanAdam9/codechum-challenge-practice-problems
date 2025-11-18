# Fuel Efficiency Comparator

distance = float(input("Enter distance in km: "))
fuel_A = float(input("Enter fuel for Car A in L: "))
fuel_B = float(input("Enter fuel for Car B in L: "))
efficiency_A = distance / fuel_A
efficiency_B = distance / fuel_B

if efficiency_A > efficiency_B:
    print(f"Car A is more efficient by {((efficiency_A - efficiency_B)/efficiency_B)*100:.2f}%")
elif efficiency_B > efficiency_A:
    print(f"Car B is more efficient by {((efficiency_B - efficiency_A)/efficiency_A)*100:.2f}%")
else:
    print("Both cars have the same efficiency")