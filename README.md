# V-Damage-Sentinel
**V-Damage Sentinel** is an AI-driven triage agent designed for independent car rental hosts (like those on Turo) and delivery drivers. The software acts as a first-line diagnostic tool when a vehicle is returned with new damage.

## The Vision
As an Information Systems student at KSU and a fleet manager, I am building this to bridge the gap between physical vehicle incidents and digital insurance processing. I want to build a system that doesn't just record data, but actively "thinks" through a triage process to assist a host in their most stressful moments.

## Key Features
* **Interactive Triage:** Asks specific questions about damage location and severity.
* **Severity Scoring:** Assigns a level (Low, Medium, High) based on logic.
* **Actionable Checklists:** Tells the user exactly what photos and documents are needed for a claim.
* **Cost Estimation:** References a data file to provide preliminary repair budget estimates.
* **Persistent Logging: Stores multiple damage assessments during a single session and generates a final summary report upon exit.

## Research & Sources
1. [Turo Damage Reporting Guide](https://support.turo.com/hc/en-us/articles/203990840-Reporting-damage) - Logic for triage questions.
2. [W3Schools Python If...Else](https://www.w3schools.com/python/python_conditions.asp) - Documentation for the conditional logic used in the damage assessment engine.
3. [Your Mechanic - Repair Costs](https://www.yourmechanic.com/services) - Source for my external data file population.