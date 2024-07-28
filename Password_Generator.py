"""
Mark Richardson
SDEV 300
Professor: Matthew Parson
Lab 2
The purpose is to create a basic menu that features
Password Generator
Basic math functions
a day counter to 07/04/2025
"""
import math
import random
import string
from datetime import date


def gen_password(password_length):
    """The method Gen password takes input from user
generates a password """

    choice_1 = True
    while choice_1:
        rando_lower = input("Do you want want the password to contain lower case letters?"
                            "\n (Y for Yes or N for No) ")
        if rando_lower.upper() == "Y":
            rando_lower = string.ascii_lowercase
            choice_1 = False
        elif rando_lower.upper() == "N":
            rando_lower = ""
            choice_1 = False
        else:
            print("Invalid Entry")
            choice_1 = True
    choice_2 = True
    while choice_2:
        rando_upper = input("Do you want want your password to contain upper case letters?"
                            "\n (Y for Yes or N for No) ")
        if rando_upper.upper() == "Y":
            rando_upper = string.ascii_uppercase
            choice_2 = False
        elif rando_upper.upper() == "N":
            rando_upper = ""
            choice_2 = False
        else:
            print("Invalid Entry")
            choice_2 = True
    choice_3 = True
    while choice_3:
        special_char = input("Do you want your password to contain characters?"
                             "\n(Y for Yes or N for No) ")
        if special_char.upper() == "Y":
            special_char = string.punctuation
            choice_3 = False
        elif special_char.upper() == "N":
            special_char = ""
            choice_3 = False
        else:
            print("Invalid Entry")
            choice_3 = True
    choice_4 = True
    while choice_4:
        numbers_rando = input("Do you want want your password to contain numbers?"
                              "\n(Y for Yes or N for No) ")
        if numbers_rando.upper() == "Y":
            numbers_rando = string.digits
            choice_4 = False
        elif numbers_rando.upper() == "N":
            numbers_rando = ""
            choice_4 = False
        else:
            print("Invalid Entry")
            choice_4 = True

        pwd_characters = rando_lower + rando_upper + numbers_rando + special_char
        password_random = "".join(random.sample(pwd_characters, password_length))
        print("Your randomly generated password is :", password_random)

        menu()


def percentage(numerator, denominator, decimal_place):
    """
Percentage function takes input from user and produces a percentage
with a decimal place that is configured to user input"""

    print("You wish to Calculate and format a percentage")

    percent = numerator / denominator
    fmt_str = "%." + str(decimal_place) + "f"
    print("Your formatted percent value equals", fmt_str % percent)


def day_counter():
    """
Day count function counts how many days are left until
07/04/2025. Based on current day grabbed from WWW
"""
    print("You wish to count how many days from today until July 4, 2025?")
    today = date.today()
    print("Today is ", today)
    ind_day_2025 = date(2025, 7, 4)
    ind_day_2025 = abs(ind_day_2025 - today)
    print("You have ", ind_day_2025.days, " days until July 4th,2025 ")


def triangle_leg(side_a, side_b, angle_c):
    """
triangle leg is a basic math function
that outputs the missing leg length based on
the inputs from the user who was too hasty in the
measurement of the triangle"""

    print("You wish calculate the leg of a triangle using the law of Cosines.")
    leg = math.pow(side_a, 2) + math.pow(side_b, 2) - (2 * side_a * side_b * math.cos(angle_c))
    leg_length = math.sqrt(leg)
    print("Given the inputs of your triangle. Your missing side length C is: ", leg_length)


def volume(radius, height):
    """
Produces the volume of a right circular cylinder
based on user inputs of radius and height"""

    print("You wish to calculate the Volume of a Right Circular Cylinder.")

    right_cylinder_volume = math.pi * radius * height
    print(float("%.2f" % right_cylinder_volume))


def menu():
    """Displays the menu functions
"""

    operational_menu = True
    while operational_menu:
        print("Welcome to Marks regular python menu!!\n"
              "Here are your options.")
        print("a. Generate Secure Password ")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle. ")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")
        menu_choice = input("What would you like to do today? ")
        if menu_choice == "a":
            password_length_check = True
            while password_length_check:
                print("You have chosen A")
                password_length = input("How long would your password to be? Enter a number 1-20: ")
                password_length = int(password_length)

                if 1 <= password_length <= 20:
                    gen_password(password_length)
                    password_length_check = False

                else:
                    print("Invalid Entry. Try again.")
                    password_length_check = True
        elif menu_choice.upper() == "B":
            print("You have chosen b")
            numerator = input("Enter numerator for your fraction: ")
            numerator = int(numerator)
            denominator = input("Enter denominator for your fraction: ")
            denominator = int(denominator)
            decimal_place = input("How many decimal places would you like to monitor: ")
            decimal_place = int(decimal_place)

            percentage(numerator, denominator, decimal_place)
        elif menu_choice.upper() == "C":
            print("You have chosen c")
            day_counter()

        elif menu_choice.upper() == "D":
            print("You have chosen d")
            input_a = True
            while input_a:
                side_a = input("How long is side A of your triangle."
                               "\n Enter a numerical value 1-999. ")
                side_a = int(side_a)
                if 1 <= side_a <= 999:
                    side_b = input("How long is side B of your triangle."
                                   "\n Enter a numerical value 1-999. ")
                    side_b = int(side_b)
                    input_a = False
                    if 1 <= side_b <= 999:
                        angle_c = input("How many degrees centigrade is your angle C?"
                                        "\n Enter a value between 1 -179 ")
                        angle_c = float(angle_c)
                        if 0 < angle_c < 180:
                            triangle_leg(side_a, side_b, angle_c)
                else:
                    input_a = True
        elif menu_choice.upper() == "E":
            print("You have chosen e")
            radius = input("Enter the radius of the cylinder: ")
            radius = int(radius)
            height = input("Enter the height of the cylinder: ")
            height = int(height)
            volume(radius, height)
        elif menu_choice.upper() == "F":
            print("You have chosen to exit the program.\n"
                  "Thank you for choosing Marks Regular service menu\n"
                  "Good bye!!")
            operational_menu = False
        else:
            print("Invalid entry try again.")


menu()
