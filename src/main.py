from components.nfa import NFA
import tests

def main():
    # create NFA object and parse automaton definition
    nfa = NFA()
    try:
        with open("src/automata/orderNfa.txt", "r") as file:
            nfa.parse_input_to_nfa(file.read())
    except FileNotFoundError:
        print("Error: Automaton definition file 'orderNfa.txt' not found.")
        return
    except Exception as e:
        print(f"Error parsing automaton: {e}")
        return

    # welcome message
    print("-----------------------------------------------------------")
    print("Welcome to the Chipotle! Please order when you are ready.")
    print("To order, enter inputs that match the menu below.")
    print("Valid inputs include bases (B, R), proteins (C, S), and toppings (N, G, L, V, E, Q).")
    print("Type '0' to exit.")

    # testing loop to get input
    while True:
        test = input("\nWhat would you like to order? (or '0' to quit): ").strip()
        if test == "0":
            print("Exiting the program. Thank you!")
            break
        # test the string and print the result
        result = tests.accept(nfa, test)
        print(f"Your order '{test}' has been {result}")

if __name__ == "__main__":
    main()
