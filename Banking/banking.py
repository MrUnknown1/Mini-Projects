from decimal import Decimal, InvalidOperation

def print_header():
    print("\n" + "="*40)
    print("💰  Welcome to Secure Bank  💰".center(40))
    print("="*40)

def showbalance(balance):
    print("\n📢 Your Current Balance: 💵 ₹{:.2f}".format(balance))

def deposit():
    while True:
        try:
            amount = Decimal(input("\n💵 Enter deposit amount: ₹"))
            if amount <= 0:
                print("❌ Invalid amount! Deposit must be greater than ₹0.")
                continue  # Ask again
            elif amount > Decimal('1000000'):  # Prevent large abuse deposits
                print("⚠️ Deposit limit exceeded! Maximum ₹1,000,000 per transaction.")
                continue
            print(f"✅ Successfully Deposited ₹{amount:.2f} 🏦")
            return amount
        except InvalidOperation:  # Catch non-numeric input
            print("❌ Invalid input! Please enter a valid number.")

def withdraw(balance):
    while True:
        try:
            amount = Decimal(input("\n💳 Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("❌ Invalid amount! Withdrawal must be greater than ₹0.")
                continue
            elif amount > balance:
                print("⚠️ Insufficient funds! You only have ₹{:.2f}".format(balance))
                continue
            elif amount > Decimal('50000'):  # Withdrawal limit for security
                print("⚠️ Withdrawal limit exceeded! Maximum ₹50,000 per transaction.")
                continue
            print(f"✅ Successfully Withdrawn ₹{amount:.2f} 🏧")
            return amount
        except InvalidOperation:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    balance = Decimal('0.00')  # Use Decimal for security
    is_running = True

    print_header()

    while is_running:
        print("\n🔹  Main Menu  🔹")
        print("1️⃣  Show Balance")
        print("2️⃣  Deposit Money")
        print("3️⃣  Withdraw Money")
        print("4️⃣  Exit")
        print("-"*40)
        
        try:
            user_input = int(input("📝 Enter your choice (1-4): "))
            
            if user_input == 1:
                showbalance(balance)

            elif user_input == 2:
                balance += deposit()

            elif user_input == 3:
                balance -= withdraw(balance)

            elif user_input == 4:
                is_running = False
                print("\n🔚 Thank you for banking with us! 🎉 Have a great day. 😊")
                print("="*40)

            else:
                print("❌ Invalid choice! Please enter a number from 1 to 4.")

        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()