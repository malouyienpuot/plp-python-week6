def main():
    while True:
        try:
            number = int(input("Enter a positive whole number: "))
        except ValueError:
            print("That is not a whole number. Please try again.")
            continue

        if number <= 0:
            print("That number is valid, but it must be greater than zero.")
            continue

        print(f"Thanks! You entered {number}.")
        return


if __name__ == "__main__":
    main()
