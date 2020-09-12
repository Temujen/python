def user_data(name, surname, year, city, email, phone):
    print(f"User data: {surname} {name} born in {year}, live in {city}, email: {email}, phone number: {phone}")


user_data(name=input("Enter user name: "), surname=input("Enter user surname: "),
          city=input("Enter name of city where user live: "), year=input("Enter year of birth: "),
          email=input("Enter your email: "), phone=input("Enter your phone number: "))
