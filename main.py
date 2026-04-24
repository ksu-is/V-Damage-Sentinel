# V-Damage Sentinel: Sprint 2 - Core Logic Engine
# Purpose: Triage vehicle damage based on user input

def run_triage():
    print("--- V-Damage Sentinel: Triage Assistant ---")
    print("Type 'quit' at any time to exit.\n")

    while True:
        # 1. Get initial damage location
        part = input("Which part of the vehicle is damaged? (e.g. Bumper, Windshield): ").strip().lower()
        if part == 'quit':
            break

        # 2. Specific Triage Logic (The "Brain")
        if part == "windshield":
            size = input("Is the crack larger than a dollar bill? (yes/no): ").strip().lower()
            if size == "yes":
                severity = "HIGH - Immediate replacement required."
            else:
                severity = "LOW - Eligible for professional chip repair."

        elif part == "bumper":
            type_dmg = input("Is the bumper dented or just scratched? (dent/scratch): ").strip().lower()
            if type_dmg == "dent":
                severity = "MEDIUM - Requires body work and structural check."
            else:
                severity = "LOW - Surface level cosmetic damage."

        elif part == "tire":
            flat = input("Is the tire holding air? (yes/no): ").strip().lower()
            if flat == "no":
                severity = "HIGH - Do not drive. Swap with spare or tow."
            else:
                severity = "MEDIUM - Monitor pressure and check for sidewall damage."

        else:
            severity = "UNKNOWN - General inspection required. Please document with photos."

        # 3. Output the result
        print(f"\n[ASSESSMENT]: {severity}")
        print("-" * 40)

if __name__ == "__main__":
    run_triage()