def agent_program(percept):
    """
    Agent function for the vacuum cleaner agent.

    Args:
        percept: The state of the current cell (0 for Clean, 1 for Dirty).

    Returns:
        The action to be taken ('Suck' or 'Move').
    """

    # Table-driven agent
    action_table = {
        0: 'Move',  # Clean: Move to another square
        1: 'Suck'   # Dirty: Clean the current square
    }

    # Lookup the action in the table
    action = action_table[percept]

    return action

