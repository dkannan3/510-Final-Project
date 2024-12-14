from components.state import State

class NFA:

    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initialState = None
        self.finalStates = []

    def __str__(self):
        return (
            f"Initial state: {self.initialState}, "
            f"Final states: {self.finalStates}, "
            f"States: {self.states}, "
            f"Transitions: {[(state.name, state.transitions) for state in self.states]}"
        )

    def add_state(self, state: State):
        self.states.append(state)

    def set_initial_state(self, state: State):
        self.initialState = state

    def add_final_state(self, state: State):
        self.finalStates.append(state)

    def run(self, input_string: str) -> bool:
        # start with the initial state
        current_states = [self.initialState]
        if not self.initialState:
            raise ValueError("initial state is not set.")

        # split input string into symbols based on alphabet
        symbol_list = []
        buffer = ""
        for char in input_string:
            buffer += char
            if buffer in self.alphabet:
                symbol_list.append(buffer)
                # reset buffer after valid symbol parsed
                buffer = ""
        # if buffer isn't empty/contains invalid symbols, reject
        if buffer:
            return False

        # process each symbol in the input string
        for symbol in symbol_list:
            next_states = []
            for state in current_states:
                # handle empty transitions
                if "ε" in state.transitions:
                    empty_state = state.next_state("ε")
                    if empty_state and empty_state not in next_states:
                        next_states.append(empty_state)

                # handle regular transitions
                next_state = state.next_state(symbol)
                if next_state and next_state not in next_states:
                    next_states.append(next_state)

            # no valid transitions
            if not next_states: 
                return False
            # update current states
            current_states = next_states 

        # check final states after processing all symbols
        final_states = []
        for state in current_states:
            if "ε" in state.transitions:
                empty_state = state.next_state("ε")
                if empty_state and empty_state not in final_states:
                    final_states.append(empty_state)
            final_states.append(state)

        # check if any final states are accepting
        return any(state in self.finalStates for state in final_states)

    def parse_input_to_nfa(self, input_string: str):
        lines = input_string.strip().split("\n")
        if len(lines) < 4:
            raise ValueError("input string must contain at least 4 lines: states, alphabet, initial state, and final states.")

        input_states = lines[0].split()
        input_alphabet = lines[1].split()
        input_initial_state = lines[2].strip()
        input_final_states = lines[3].split()

        for state_name in input_states:
            self.add_state(State(state_name))

        self.alphabet = input_alphabet

        for line in lines[4:]:
            state_name, symbol, next_state_name = line.split()
            current_state = next((s for s in self.states if s.name == state_name), None)
            next_state = next((s for s in self.states if s.name == next_state_name), None)
            if not current_state or not next_state or (symbol not in self.alphabet and symbol != 'ε'):
                raise ValueError(f"invalid transition: {line}")
            current_state.add_transition(symbol, next_state)

        self.initialState = next((s for s in self.states if s.name == input_initial_state), None)
        if not self.initialState:
            raise ValueError("initial state is not in the list of states.")

        for final_state_name in input_final_states:
            final_state = next((s for s in self.states if s.name == final_state_name), None)
            if not final_state:
                raise ValueError(f"final state '{final_state_name}' is not in the list of states.")
            self.add_final_state(final_state)

        return self
