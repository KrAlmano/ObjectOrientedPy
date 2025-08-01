from car_rental import CarRent,BikeRent,Customer

bike = BikeRent(100)
car = CarRent(100)
customer = Customer()


main_menu = True

while True:
    if main_menu:
        print("""
            *****Vehicle Rental Shop****
              A.Bike Menu
              B.Car Menu
              Q.Exit
                    """)
        main_menu=False

        choice = input("Enter choice :")

    if choice =="a" or choice == "A":
        print("""
                 *****BIKE MENU*****
                1. Display available bikes
                2.Request a bike on hourly basis $5
                3.Request a bike on daily basis $84
                4.Return a bike 
                5.Main Menu
                6.Exit  
                        """)
        choice = input("Enter choice:")
        
        try:
            choice=int(choice)
        except ValueError:
            print("Non valid input")
            continue

        if choice ==1:
            bike.displayStock()
            choice="A"
        elif choice==2:
            customer.rentalBasis_b= bike.rentHourly(customer.requestVehicle("bike"))
            customer.rentalBasis_b=1
            main_menu=1
            print("--------")

        elif choice ==3:
            customer.rentalBasis_b= bike.rentDaily(customer.requestVehicle("bike"))
            customer.rentalBasis_b=2
            main_menu=1
            print("--------")

        elif choice ==4:
            
             request = customer.returnVehicle("bike")
             if request == (0, 0, 0):
                 print("You didn't rent any bike.")
             else:
                         customer.bill = bike.returnVehicle(request, "bike")
                         customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0, 0, 0
                         main_menu = True

        elif choice==5:
            main_menu=True

        elif choice == 6:
            break

        else:
            print("İnvalid input please enter an number 1-6")
            main_menu=True


    elif choice == "b" or choice=="B":
        print("""
                 *****Car MENU*****
                1. Display available cars
                2.Request a car on hourly basis $10
                3.Request a car on daily basis $192
                4.Return a car 
                5.Main Menu
                6.Exit  
                        """)
        choice = input("Enter choice:")
        
        try:
            choice=int(choice)
        except ValueError:
            print("Non valid input")
            continue
        
        if choice ==1:
            car.displayStock()
            choice="B"
        elif choice==2:
            customer.rentalTime_c= car.rentHourly(customer.requestVehicle("car"))
            customer.rentalBasis_c=1
            main_menu=1
            print("--------")

        elif choice ==3:
            customer.rentalTime_c= car.rentDaily(customer.requestVehicle("car"))
            customer.rentalBasis_c=2
            main_menu=1
            print("--------")

        elif choice ==4:
            customer.bill= car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu=True

        elif choice==5:
            main_menu=True

        elif choice == 6:
            break

        else:
            print("İnvalid input please enter an number 1-6")
            main_menu=True

    elif choice == "q" or choice=="Q":
        break

    else:
        print("İnvalid input. Please enter A,B or Q")
        main_menu=True
    print("Thank you for using VehicleRent")