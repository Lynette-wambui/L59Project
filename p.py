def myfunction1(n):
    if n <= 0:
        return
    message = input(f"myfunction1 called with n = {int(n)}. Type something interesting like;😁☺️ : ")
    for i in range(0, int(n) + 1):
        print(message)
    # Recursive calls
    myfunction1(n // 2)
    myfunction1(n // 3)

def myfunction2(n):
    if n <= 1:
        return
    message = input(f"myfunction2 called with n = {n}. Enter something interesting: ")
    print(message)
    myfunction2(n - 1)

# Main user prompt
try:
    num = int(input("Enter a positive integer: "))
    print("\n--- Output from myfunction1 ---")
    myfunction1(num)

    print("\n--- Output from myfunction2 ---")
    myfunction2(num)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")






def space(n):
    if n == 0:
        print("🌌🌌 Reached the end! Time to go back up!")
        return
    print(f"Going deeper... Level {n}")

    space(n - 1)

    print(f"Coming back... Level  {n}")

# Start the journey
levels = int(input("Enter how many levels  deep we should go"))
space(levels)
    





def build_pyramid(n, current=1):
    if current > n:
        return
    # Print spaces and stars
    spaces = ' ' * (n - current)
    stars = '*' * (2 * current - 1)
    print(spaces + stars)

    # Recursive call for next level
    build_pyramid(n, current + 1)

# Example: Build a pyramid with 5 levels
levels = int(input("Enter the number of levels for the pyramid: "))
print("\nHere is your pyramid:\n")
build_pyramid(levels)