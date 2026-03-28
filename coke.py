
def main():
    amount_due = 50

    while amount_due > 0:
        print(f'amount due: {amount_due} ')
        coin = int(input('insert coin: '))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
        else:
            print("Invalid coin. Please insert 25, 10, or 5 cents.")
    change = abs(amount_due)
    print(f'Change Owed: {change}')
main()
