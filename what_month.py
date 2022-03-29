#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a integer, positive, negative, or zero program


def main():

    # input
    month_number = int(input("Enter your number here! : "))

    # process & output
    if month_number == 1:
        print("\nYour month is January, since you wrote {0}!".format(month_number))
    elif month_number == 2:
        print("\nYour month is February, since you wrote {0}!".format(month_number))
    elif month_number == 3:
        print("\nYour month is March, since you wrote {0}!".format(month_number))
    elif month_number == 4:
        print("\nYour month is April, since you wrote {0}!".format(month_number))
    elif month_number == 5:
        print("\nYour month is May, since you wrote {0}!".format(month_number))
    elif month_number == 6:
        print("\nYour month is June, since you wrote {0}!".format(month_number))
    elif month_number == 7:
        print("\nYour month is July, since you wrote {0}!".format(month_number))
    elif month_number == 8:
        print("\nYour month is August, since you wrote {0}!".format(month_number))
    elif month_number == 9:
        print("\nYour month is September, since you wrote {0}!".format(month_number))
    elif month_number == 10:
        print("\nYour month is October, since you wrote {0}!".format(month_number))
    elif month_number == 11:
        print("\nYour month is November, since you wrote {0}!".format(month_number))
    elif month_number == 12:
        print("\nYour month is December, since you wrote {0}!".format(month_number))
    else:
        print("\nThat is not a month, since you wrote {0}!".format(month_number))
    print("\nDone!")


if __name__ == "__main__":
    main()
