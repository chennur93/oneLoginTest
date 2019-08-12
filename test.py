from FracCalc import Calc

print("\n0. Run sample test cases.")
print("1. User-defined input: ")
print("2. Exit")

sample = ["? 1/2 * 3_3/4", "? 2_3/8 + 9/8", "? 2_1/2", \
"? 4_1/3 / 2_1/6 - 3/4 * 2", "1/2 +      3_1/2", "? 3/4 + 2/6 + 2_2/4"]

option = input("\nSelect option:")

while option != 2:
    if int(option) == 0:
        for x in sample:
            print("\n" + str(x))
            calc = Calc(x)
            print(calc.getResult())
    elif int(option) == 1:
        val = input("Enter input value:")
        calc = Calc(val)
        print("\n" + str(calc.getResult()))
    elif int(option) == 2:
        quit()
    elif int(option) > 2:
        print("Invalid option! Please re-enter a valid option.")
    option = input("\nSelect option:")
