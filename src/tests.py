from components.nfa import NFA

# accept function to see if NFA accepts the input string
def accept(A: NFA, w: str) -> str:
    return "accepted" if A.run(w) else "rejected"

# test cases for the Chipotle Order Language
strings = [
    "B",           # Base only -> reject
    "R",           # Base only -> reject 
    "BC",          # Base + Protein -> accept
    "RC",          # Base + Protein -> accept
    "BCG",         # Base + Protein + Topping -> accept
    "RCG",         # Base + Protein + Topping -> accept
    "BCGLV",       # Full valid sequence -> accept
    "RCGLV",       # Full valid sequence -> accept
    "BCBnL",       # Invalid topping repetition -> reject
    "RR",          # Repeated base -> reject
    "BS",          # Base + Protein -> accept
    "RS",          # Base + Protein -> accept
    "RSGG",        # Double topping -> accepted
    "",            # Empty input -> reject
]


# run test cases
def run_tests():
    # initialize NFA
    nfa = NFA()
    file = open("src/automata/orderNfa.txt", "r").read()
    nfa.parse_input_to_nfa(file)

    # run every test case
    for test in strings:
        result = accept(nfa, test)
        # format output
        max_length = max(len(s) for s in strings)
        formatted_string = f"{test:<{max_length + 2}}"
        print(f"{formatted_string}: {result}")

if __name__ == "__main__":
    run_tests()
