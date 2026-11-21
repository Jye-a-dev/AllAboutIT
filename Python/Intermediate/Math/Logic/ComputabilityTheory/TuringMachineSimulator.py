# Previous input
tape = input("Enter initial tape content (e.g. '1011'): ").strip()

# Process
def simulate_Turing_Machine(tape, transitions, start_state, accept_states, blank='_', max_steps=1000):
    tape_dict = {i: ch for i, ch in enumerate(tape)} if tape else {0: blank}
    head = 0
    state = start_state
    steps = 0
    while steps < max_steps and state not in accept_states:
        curr_sym = tape_dict.get(head, blank)
        key = (state, curr_sym)
        if key not in transitions:
            break
        new_state, write_sym, direction = transitions[key]
        tape_dict[head] = write_sym
        state = new_state
        if direction == 'R':
            head += 1
        elif direction == 'L':
            head -= 1
        steps += 1
    min_idx = min(tape_dict.keys()) if tape_dict else 0
    max_idx = max(tape_dict.keys()) if tape_dict else 0
    final_tape = "".join(tape_dict.get(i, blank) for i in range(min_idx, max_idx + 1))
    return {
        "tape": final_tape,
        "head": head,
        "state": state,
        "accepted": state in accept_states,
        "steps": steps
    }

# Post process
print("Turing Machine simulation result:", simulate_Turing_Machine(tape, {('q0', '1'): ('q0', '1', 'R'), ('q0', '0'): ('q0', '0', 'R'), ('q0', '_'): ('q_accept', '_', 'N')}, 'q0', {'q_accept'}))
