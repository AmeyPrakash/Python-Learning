import converter
while True:
    print("UNIT CONVERTER")
    print("1.Kilometer to Meter")
    print("2.Meter to Kilometer")
    print("3.Celsius to Fahrenheit")
    print("4.Fahrenheit to Celsius")
    print(".Kilogram to Gram")
    print("7.Gram to Kilogram")
    print("8.Exit")
    
    choice = int(input("Enter your choice: "))

  
    if choice == 1:
        km = float(input("Enter kilometers: "))
        print("Meters =", converter.km_to_m(km))

    elif choice == 2:
        m = float(input("Enter meters: "))
        print("Kilometers =", converter.m_to_km(m))

    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print("Fahrenheit =", converter.c_to_f(c))

    elif choice == 4:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Celsius =", converter.f_to_c(f))

    elif choice == 5:
        kg = float(input("Enter kilograms: "))
        print("Grams =", converter.kg_to_g(kg))

    elif choice == 6:
        g = float(input("Enter grams: "))
        print("Kilograms =", converter.g_to_kg(g))
        
    else:
        print("Invalid choice!")
