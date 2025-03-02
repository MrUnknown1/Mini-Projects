import random as rd
import time

# 🎲 Symbols and their multipliers
SYMBOLS = ['🍒', '🍉', '🍋', '🔔', '⭐']
PAYOUTS = {
    '🍒': 5,
    '🍉': 10,
    '🍋': 20,
    '🔔': 30,
    '⭐': 50
}

# 🎰 Special Bonus & Jackpot
JACKPOT_MULTIPLIER = 100  # ⭐⭐⭐ gives 100x
BONUS_MULTIPLIER = 2      # 🍉🍉🔔 gives double payout

def print_header():
    print("\n" + "="*45)
    print("🎰✨ Welcome to the Ultimate Slot Machine! ✨🎰".center(45))
    print("="*45)

def spin_row():
    return [rd.choice(SYMBOLS) for _ in range(3)]

def print_row(row):
    print("\n🎡 Spinning... 🎡\n")
    time.sleep(1)  # Simulate slot machine delay
    print(" | ".join(row))  # Neatly prints the slot row
    print("="*45)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Regular winning condition
        if row[0] == '⭐':  # Jackpot Condition (⭐⭐⭐)
            return bet * JACKPOT_MULTIPLIER
        return bet * PAYOUTS.get(row[0], 0)
    
    # 🎁 Special Bonus Condition (🍉🍉🔔 gives double)
    if row == ['🍉', '🍉', '🔔']:
        return bet * BONUS_MULTIPLIER

    return 0  # No win

def main():
    balance = 100  # 🎯 Starting balance

    print_header()

    while balance > 0:
        print(f"\n💰 Your Current Balance: ₹{balance:,.2f}")
        bet = input("🎲 Enter your bet amount (or type 'q' to cash out): ₹")

        if bet.lower() == 'q':
            print(f"\n🏆 You cashed out with ₹{balance:,.2f}! Thanks for playing! 🎉")
            break

        if not bet.isdigit() or int(bet) <= 0:
            print("❌ Invalid bet! Please enter a positive number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("⚠️ Insufficient funds! Lower your bet.")
            continue

        balance -= bet
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            if payout == bet * JACKPOT_MULTIPLIER:
                print("🎉🎰 JACKPOT WIN! ⭐⭐⭐ 🎰🎉")
                print(f"🔥 You won a whopping ₹{payout:,.2f}! 🔥")
            elif payout == bet * BONUS_MULTIPLIER:
                print("🎁 BONUS WIN! 🍉🍉🔔 🎁")
                print(f"✨ You doubled your bet and won ₹{payout:,.2f}! ✨")
            else:
                print(f"🎉 You won ₹{payout:,.2f}! Congrats! 🏆")
        else:
            print("💔 Sorry, you lost this round.")

        balance += payout

    print(f"\n🔚 Game Over! Your final balance is ₹{balance:,.2f}. Thanks for playing! 🎰")

if __name__ == '__main__':
    main()
