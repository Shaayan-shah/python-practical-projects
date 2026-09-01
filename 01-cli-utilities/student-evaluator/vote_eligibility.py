"""
Voter Eligibility & Age Verification System
Validates citizen registration status and statutory age criteria for voting.
"""


def check_eligibility(name: str, age: int, has_id: bool, is_registered: bool) -> dict:
    """Evaluate voting requirements based on statutory criteria."""
    eligible = (age >= 18) and has_id and is_registered
    reasons = []

    if age < 18:
        reasons.append(f"Underage (Requires minimum age of 18, current: {age})")
    if not has_id:
        reasons.append("Missing National ID / CNIC verification")
    if not is_registered:
        reasons.append("Not enrolled in voter registration electoral roll")

    return {
        "name": name,
        "eligible": eligible,
        "reasons": reasons
    }


def main():
    print("==================================================")
    print("           VOTER ELIGIBILITY VERIFIER             ")
    print("==================================================")

    name = input("Enter applicant name: ").strip() or "Citizen"
    try:
        age = int(input("Enter age: ").strip())
    except ValueError:
        print("[Error] Invalid numerical age.")
        return

    has_id = input("Do you possess a valid National ID / CNIC? (y/n): ").strip().lower() == "y"
    is_registered = input("Are you enrolled on the voter electoral roll? (y/n): ").strip().lower() == "y"

    result = check_eligibility(name, age, has_id, is_registered)

    print("\n--- Verification Result ---")
    if result["eligible"]:
        print(f"[ELIGIBLE] {result['name']} is qualified to cast their vote.")
    else:
        print(f"[INELIGIBLE] {result['name']} cannot vote due to:")
        for r in result["reasons"]:
            print(f"  - {r}")
    print("---------------------------")


if __name__ == "__main__":
    main()
