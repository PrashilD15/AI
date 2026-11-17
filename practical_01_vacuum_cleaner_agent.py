# Practical 1: Vacuum Cleaner Agent
# Architecture: Simple Reflex Agent
# Environment: Two rooms (A and B), each can be Dirty or Clean


def vacuum_reflex_agent(location, status):
    """Reflex agent function to determine action based on current percept."""
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


if __name__ == "__main__":
    room = {
        "A": input("Enter status of Room A (Dirty/Clean): ").strip().capitalize(),
        "B": input("Enter status of Room B (Dirty/Clean): ").strip().capitalize()
    }
    location = input("Enter starting location (A/B): ").strip().upper()

    print("\n--- Vacuum Cleaner Simulation ---")
    while True:
        print("\nCurrent Location:", location)
        print("Room Status:", room)
        action = vacuum_reflex_agent(location, room[location])
        print("Action:", action)

        if action == "Suck":
            room[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        elif action == "Move Left":
            location = "A"

        if room["A"] == "Clean" and room["B"] == "Clean":
            print("\nBoth rooms are clean!")
            print("Agent stops.")
            break
