import random

# /usr/bin/python3 /Users/chyannemckeller/DealorNoDeal/dealOrNoDeal.py

class DealOrNoDeal(object): 
    def __init__(self):
        print('\n\n')
        print('*' * 30, '\n\n')
        print(('Welcome to Deal or No Deal!').upper(), end='\n\n')
        print('*' * 30, '\n\n')

    def generateCasesContents(self):
        cases = list(range(1, 27))
        case_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

# Have the players choose an initial briefcase
        print("There are 26 cases labeled 1-26. Each case has a certain amount of money. Here are the amounts in each briefcase:")
        print(case_amounts)   

# Shuffles the briefcase amounts and assigns them to the briefcases
        random.shuffle(case_amounts)
        self.briefcaseStack = dict(zip(cases, case_amounts))   

    def chooseInitialCase(self):   
        while True:
            try:
                choice = int(input("Choose a case number between 1 and 26: "))
                if 1 <= choice <= 26:
                    print(f"You have chosen case number {choice}.")
                    self.player_case = choice
                    self.player_case_value = self.briefcaseStack[self.player_case]
                    print("Let's start the first round!")

                # Delete the chosen briefcase in the list of all the briefcases
                    del self.briefcaseStack[choice]
                    break

                else:
                    print('Error! Out of range.', end='\n\n')
                    continue
            except ValueError:
                print('Error! Invalid input.', end='\n\n')
                continue

    
    def playRound(self, round_number, cases_to_open):
        print(f"Round {round_number}: {len(self.briefcaseStack)} cases remaining.")
        print(f"Open {cases_to_open} cases.")

        for i in range(cases_to_open):
            while True:
                try:
                    choice = int(input("Choose a case number to open: "))
                    if choice in self.briefcaseStack:
                        print(f"Case number {choice} contains ${self.briefcaseStack[choice]}.")
                        del self.briefcaseStack[choice]
                        break
                    else:
                        print('You have already opened this case!', end='\n\n')
                    
                except ValueError:
                    print('Error! Invalid input.', end='\n\n')

        print(f"\nRemaining case amount: {sorted(self.briefcaseStack.values())}")
        print(f"\nRemaining briefcases: {sorted(self.briefcaseStack.keys())}")


    def bankersOffer(self):
        print("The banker is making an offer. . .")
        avg = sum(self.briefcaseStack.values()) / len(self.briefcaseStack)
        offer = round(avg * 0.75, 0)
        print(f"The banker's offer is ${offer:,.0f}")

        decision = input("Deal or No Deal? (D/N): ").strip().upper()
        if decision == "D":
            print(f"Congratulations! You have won ${offer:,.0f}!")
            print(f"The amount in your case was ${self.player_case_value:,.0f}")
            exit()

        else:
            print("No deal! Let's continue")


    def playGame(self):
        self.chooseInitialCase()
    
        # Define rounds
        rounds = [6, 5, 4, 3, 2, 1, 1, 1, 1]  # Number of cases to open per round
    
        for round_number, cases in enumerate(rounds, start=1):
            self.playRound(round_number, cases)
            self.bankersOffer()
    
    # Final two cases
        print("\nOnly two cases remain!")
        print(f"Your case: {self.player_case}")
        remaining_cases = list(self.briefcaseStack.keys())
        print(f"Other case: {remaining_cases[0]}")
    
        swap = input("Do you want to switch your case? (Y/N): ").strip().upper()
        if swap == "Y":
            self.player_case = remaining_cases[0]
    
    # Reveal final case value
        print(f"\nYour final prize: ${self.player_case_value:,.0f}")


if __name__ == "__main__":
    game = DealOrNoDeal()  # Create an instance of the class
    game.generateCasesContents()  # Call the method to generate and print cases
    game.playGame()  # Call the method
