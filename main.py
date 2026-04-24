# V-Damage Sentinel: Sprint 2 - Core Logic Engine (Updated)
# Purpose: Triage vehicle damage and log results for a final report

def run_triage():
    # This list will store all our assessments for the final report
    damage_log = []
    
    print("--- V-Damage Sentinel: Triage Assistant ---")
    print("Type 'quit' at any time to exit and view the report summary.\n")

    while True:
        part = input("Which part of the vehicle is damaged? (e.g. Bumper, Windshield): ").strip().lower()
        if part == 'quit':
            break

        # Triage Logic
        if part == "windshield":
            size = input("Is the crack larger than a dollar bill? (yes/no): ").strip().lower()
            severity = "HIGH" if size == "yes" else "LOW"
            description = "Replacement required" if size == "yes" else "Chip repair eligible"

        elif part == "bumper":
            type_dmg = input("Is the bumper dented or just scratched? (dent/scratch): ").strip().lower()
            severity = "MEDIUM" if type_dmg == "dent" else "LOW"
            description = "Structural/Body work" if type_dmg == "dent" else "Surface cosmetic"

        elif part == "tire":
            flat = input("Is the tire holding air? (yes/no): ").strip().lower()
            severity = "HIGH" if flat == "no" else "MEDIUM"
            description = "Do not drive / Swap tire" if flat == "no" else "Monitor pressure"

        else:
            severity = "UNKNOWN"
            description = "Manual inspection and photos required"

        # Save the result to our log
        assessment = f"{part.title()}: [{severity}] - {description}"
        damage_log.append(assessment)
        print(f"\n[CURRENT ASSESSMENT]: {severity} severity logged.")
        print("-" * 40)

    # FINAL REPORT SUMMARY
    print("\n" + "="*30)
    print("FINAL DAMAGE SUMMARY REPORT")
    print("="*30)
    if not damage_log:
        print("No damage reported.")
    else:
        for entry in damage_log:
            print(f"- {entry}")
    print("="*30)

if __name__ == "__main__":
    run_triage()