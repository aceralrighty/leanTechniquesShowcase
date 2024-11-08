# takes in the amount from the user
def user_amount():
    while True:
        try:
            amount = float(input("Enter a dollar amount: "))
            if amount < 0:
                print("Please enter a positive dollar amount (e.g 19.99): ")
            else:
                return amount
        except ValueError as e:
            print(f"Please enter a positive dollar amount (e.g 19.99): \n{e}")


# takes in an amount from user and multiplies it by 100
def convert_to_cents(amount):
    return int(amount * 100)


# figuring out that python has some built-in features like too longer than i'd like to admit
def change_for_user(cents):
    ten_bill = cents // 1000
    cents %= 1000

    five_bill = cents // 500
    cents %= 500

    one_bill = cents // 100
    cents %= 100

    dime = cents // 10
    cents %= 10

    quarter = cents // 25
    cents %= 25

    nickel = cents // 10
    cents %= 10

    penny = cents

    return ten_bill, five_bill, one_bill, dime, nickel, penny, quarter


def give_user_change(amount, ten_bill, five_bill, one_bill, dime, nickel, penny, quarter):
    print(f"You gave me ${amount:.2f} dollars.")
    print("You will get: ")

    if ten_bill > 0:
        print(f"\t{ten_bill} - 10 dollar bills")
    else:
        print(f"\t{ten_bill} - 10 dollar bills")

    if five_bill > 0:
        print(f"\t{five_bill} - 5 dollar bills")
    else:
        print(f"$\t{five_bill} - 5 dollar bills")

    if one_bill > 0:
        print(f"\t{one_bill} - 1 dollar bills")
    else:
        print(f"$\t{one_bill} - 1 dollar bills")

    if dime > 0:
        print(f"\t{dime} - dimes")
    else:
        print(f"\n{dime} - dimes")

    if nickel > 0:
        print(f"\t{nickel} - nickels")
    else:
        print(f"\t{nickel} - nickels")

    if quarter > 0:
        print(f"\t{quarter} - quarters")
    else:
        print(f"\t{quarter} - quarters")

    if penny > 0:
        print(f"\t{penny} - pennies")
    else:
        print(f"\t{penny} - pennies")


# added this main because it was shadowing outer scope stuff
def main():
    amount = user_amount()
    cents = convert_to_cents(amount)
    ten_bill, five_bill, one_bill, dime, nickel, penny, quarter = change_for_user(cents)
    give_user_change(amount, ten_bill, five_bill, one_bill, dime, nickel, penny, quarter)


main()
