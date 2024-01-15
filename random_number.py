import random

def generate_random_numbers():
    # Step 1: Generate a list of numbers from 1 to 100
    numbers = list(range(1, 36)) # + 1 above maximum number

    # Step 2: Shuffle the list to get a random order
    random.shuffle(numbers)

    # Step 3: Return the shuffled list
    return numbers

def main():
    # Step 4: Get the shuffled numbers by calling the generate_random_numbers function
    shuffled_numbers = generate_random_numbers()

    # Step 5: Print each number in the shuffled list
    for number in shuffled_numbers:
        print(number)

# Step 6: Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Step 7: Call the main function to execute the main part of the script
    main()