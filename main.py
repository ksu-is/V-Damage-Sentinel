# V-Damage Sentinel: Sprint 3 - Data Integration
# Purpose: Read repair costs from an external file to provide budget estimates

def load_costs():
    """Reads repair_costs.txt and returns a dictionary of parts and prices."""
    costs = {}
    try:
        with open("repair_costs.txt", "r") as file:
            for line in file:
                part, price = line.strip().split(",")
                costs[part] = int(price)
    except FileNotFoundError:
        print("Warning: repair_costs.txt not found. Estimates will be unavailable.")
    return costs

def run_triage():
    prices = load_costs()
    damage_log = []
    
    print("--- V-Damage Sentinel: Sprint 3 Claims Assistant ---")
    print("Type 'quit' at any time to exit.\n")

    while True:
        part = input("Which part is damaged? (Bumper, Windshield, Tire, Mirror, Headlight): ").strip().lower()
        if part == 'quit':
            break

        # Check if we have a price for this part
        estimated_cost = prices.get(part, 0)

        # Triage Logic
        if part == "windshield":
            size = input("Is the crack larger than a dollar bill? (yes/no): ").strip().lower()
            severity = "HIGH" if size == "yes" else "LOW"
            description = f"Replacement required. Est: ${estimated_cost}"
        elif part == "bumper":
            type_dmg = input("Is the bumper dented or just scratched? (dent/scratch): ").strip().lower()
            severity = "MEDIUM" if type_dmg == "dent" else "LOW"
            description = f"Body work needed. Est: ${estimated_cost}"
        else:
            severity = "UNKNOWN"
            description = f"Manual inspection required. Est: ${estimated_cost}"

        assessment = f"{part.title()}: [{severity}] - {description}"
        damage_log.append(assessment)
        print(f"\n[LOGGED]: {assessment}\n")

    # Final Summary
    print("\n" + "="*40)
    print("V-DAMAGE SENTINEL FINAL REPORT")
    print("="*40)
    total_est = 0
    for entry in damage_log:
        print(f"- {entry}")
        # Extract price from entry string for the total
        if "$" in entry:
            total_est += int(entry.split("$")[-1])
            
    print("-" * 40)
    print(f"TOTAL PRELIMINARY ESTIMATE: ${total_est}")
    print("="*40)

if __name__ == "__main__":
    run_triage()