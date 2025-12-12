from src.helpers.turing_machine import TuringMachineSimulator


# ==========================================
# PROGRAM 1: Nondeterministic TM [cite: 137]
# ==========================================
class NTM_Tracer(TuringMachineSimulator):
    def run(self, input_string, max_depth):
        """
        Performs a Breadth-First Search (BFS) trace of the NTM.
        Ref: Section 4.1 "Trees as List of Lists" [cite: 146]
        """
        #print("\n=== DEBUGGING TRANSITIONS ===")
        #print(f"Looking for key: ('{self.start_state}', '{input_string[0]}')")
        #print("Existing Keys in self.transitions:")
        #for key in self.transitions:
        #    print(f"  {repr(key)} -> {self.transitions[key]}") 
        #print("===============================\n")
        # --- DEBUG END ---

        print(f"Tracing NTM: {self.machine_name} on input '{input_string}'")

        # Initial Configuration: ["", start_state, input_string]
        # Note: Represent configuration as triples (left, state, right) [cite: 156]
        initial_config = ["", self.start_state, input_string]

        # The tree is a list of lists of configurations
        tree = [[initial_config]]
        visited = set()



        depth = 0
        accepted = False

        while depth < max_depth and not accepted:
            current_level = tree[-1]
            next_level = []
            all_rejected = True

            # TODO: STUDENT IMPLEMENTATION NEEDED
            # 1. Iterate through every config in current_level.
            # 2. Check if config is Accept (Stop and print success) [cite: 179]
            # 3. Check if config is Reject (Stop this branch only) [cite: 181]
            # 4. If not Accept/Reject, find valid transitions in self.transitions.
            # 5. If no explicit transition exists, treat as implicit Reject.
            # 6. Generate children configurations and append to next_level[cite: 148].

            # Print the current level and configurations to terminal
            print(f"Level {depth + 1}")
            print(current_level)
            #1. Iterate through every config in current_level.
            #print(f"current level configs: {len(current_level)}")
            for config in current_level:
                #Take only the first 3 elements (left, state, right)
                #Note for later - make sure this works for the root (len 3) AND children (len 4)
                left, state, right = config[:3]
                #print(f"Current config: Left='{left}', State='{state}', Right='{right}'")

                #2. Accept
                if state == self.accept_state:
                    print(f"String accepted in {depth} steps.")
                    self.print_trace_path(config)
                    accepted = True
                    return

                #3. Reject - stop this branch only
                if state == self.reject_state:
                    #print("rejecting this branch")
                    continue
                
                #4. If not Accept/Reject, find valid transitions
                
                #What's the symbol under the head
                if len(right) > 0:
                    symbol = right[0]
                else:
                    symbol = "_" 

                possible_moves = []
                
                #Get all rules for the current state - default = empty list if state not found
                state_rules = self.transitions.get(state, [])

                #Iterate through rules to find matches for the current symbol
                for rule in state_rules:
                    read_symbol = rule['read'][0]
                    
                    if read_symbol == symbol:
                        # Extract details from the dict
                        next_st = rule['next']        #This is a string
                        write_ch = rule['write'][0]   #This is a tuple ('a',) so take [0]
                        dir_mv = rule['move'][0]      #Same thing
                        
                        #Add to possible moves as a tuple
                        possible_moves.append((next_st, write_ch, dir_mv))

                #5. If no explicit transition exists, treat as implicit Reject
                if not possible_moves:
                    #print("No valid moves, rejecting this branch")
                    continue
                
                #If we are here, we have valid moves, so the tree is still alive YAY
                all_rejected = False
                #print(f"possible moves: {possible_moves}")
                #6. Generate children configurations and append to next_level
                for move in possible_moves:
                    next_state, write_char, direction = move
                    
                    #Prepare the new tape strings
                    #NOTE: right includes the character currently under the head at index 0
                    
                    if direction == 'R':
                        # Move Right:
                        #1. The current head position is written with write_char and becomes part of the left tape.
                        #2. The head moves to the next character in 'right'.
                        new_left = left + write_char
                        if len(right) > 0:
                            new_right = right[1:]
                        else:
                            #If we moved right into a blank area, the new head sees empty
                            new_right = ""
                            
                    elif direction == 'L':
                        # Move Left:
                        if len(left) > 0:
                            #1. The character to the immediate left (left[-1]) becomes the new head.
                            #2. The old head position is written with write_char and moves to the right side.
                            new_head_char = left[-1]
                            rest_of_right = right[1:] if len(right) > 0 else ""
                            
                            new_right = new_head_char + write_char + rest_of_right
                            new_left = left[:-1]
                        else:
                            #Edge Case: Attempting to move Left at the start of the tape.
                            #Normally the head stays put but the write still happens.
                            rest_of_right = right[1:] if len(right) > 0 else ""
                            new_right = write_char + rest_of_right
                            new_left = ""

                    #Create the new configuration and add to the next level
                    new_config = [new_left, next_state, new_right, config]
                    next_level.append(new_config)

                    #My extra steps:
                    #7. Prepare for next iteration
            
            #If no valid moves were found for ANY configuration in this level machine halts and rejects.
            if all_rejected:
                print(f"String rejected in {depth} steps.")
                break
            
            #Otherwise add the generated children to the tree and proceed
            tree.append(next_level)
            depth += 1

        #8. Handle Timeout / Max Depth Exceeded
        if not accepted and depth >= max_depth:
            print(f"Execution stopped after {max_depth} steps.")
                


    def print_trace_path(self, final_node):
        """
        Backtrack and print the path from start to accept.
        Assignment format: 
        Level k
        left state head rest
        
        # ---- DEBUGGING CODE ----
        print("\n--- DEBUGGING TRACE PATH ---")
        print(f"Type of final_node: {type(final_node)}")
        print(f"Value of final_node: {final_node}")
        # --------------------
        """

        path = []
        current = final_node
        
        #1. Backtrack 
        #Check if current has 4 elements (meaning it has a parent)
        #The root node ["", start, input] only has 3 elements, so we stop there.
        while len(current) == 4:
            path.append(current)
            current = current[3] # The parent is stored at index 3
        
        #Append the root node (which has no parent)
        path.append(current)
        
        #2. Reverse
        path.reverse()
        
        #3. Print
        for k, node in enumerate(path):
            print(f"Level {k}")
            left = node[0]
            state = node[1]
            
            #Helper to get head/rest from the right tape
            right_tape = node[2]
            head = right_tape[0] if len(right_tape) > 0 else "_"
            rest = right_tape[1:] if len(right_tape) > 1 else ""

            print(f"{left} {state} {head} {rest}")
