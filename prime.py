def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    N = int(input("Enter a number (N): "))
    
    print(f"Prime numbers between 2 and {N} are:")
    for num in range(2, N + 1):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    main()
