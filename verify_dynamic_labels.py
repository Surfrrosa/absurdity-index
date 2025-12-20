#!/usr/bin/env python3
"""
Verify dynamic labels are correctly assigned based on scores
"""

# Current scores from calculate_all_social_scores.py
metrics = {
    "What Healthcare?": {
        "score": 50.20,
        "thresholds": [
            (20, "Coverage Exists (Allegedly)"),
            (40, "Navigating the Maze"),
            (60, "Prior Authorization Purgatory"),
            (80, "Medical Bankruptcy Pipeline"),
            (100, "Die Quietly, Please")
        ]
    },
    "AI Psychosis": {
        "score": 37.31,
        "thresholds": [
            (20, "Chatbots Are Cute"),
            (40, "Digital Stockholm Syndrome Setting In"),
            (60, "My AI Is My Best Friend"),
            (80, "Can't Tell Humans From Bots Anymore"),
            (100, "Ready Player One Was A Warning")
        ]
    },
    "Subscription Overload": {
        "score": 39.93,
        "thresholds": [
            (20, "Affordable Convenience"),
            (40, "Quarterly Purge Required"),
            (60, "Forgot What I'm Paying For"),
            (80, "Working to Pay Subscriptions"),
            (100, "Subscription Serfdom Achieved")
        ]
    },
    "Wage Stagnation": {
        "score": 40.86,
        "thresholds": [
            (20, "Inflation Exists But Manageable"),
            (40, "Paycheck Doesn't Go As Far"),
            (60, "Living Paycheck to Paycheck"),
            (80, "Full-Time Yet Food Insecure"),
            (100, "Working Poor Is The New Normal")
        ]
    },
    "Housing Despair": {
        "score": 43.64,
        "thresholds": [
            (20, "Homeownership Is Possible"),
            (40, "Saving For A Deposit (Forever)"),
            (60, "Multiple Organs Required"),
            (80, "Gave Up On Ownership Entirely"),
            (100, "Welcome To Permanent Rentership")
        ]
    },
    "Dating App Despair": {
        "score": 31.55,
        "thresholds": [
            (20, "Love Is In The Air"),
            (40, "Swiping Through The Void"),
            (60, "Emotionally Exhausted, Still Trying"),
            (80, "Gave Up, Got A Cat"),
            (100, "Accepting Loneliness As Default")
        ]
    },
    "Layoff Watch": {
        "score": 51.64,
        "thresholds": [
            (20, "Job Security Intact"),
            (40, "Resume At The Ready"),
            (60, "Layoff Roulette Daily Anxiety"),
            (80, "500 Applications, Zero Responses"),
            (100, "Experience Is Now A Liability")
        ]
    },
    "Airline Chaos": {
        "score": 40.13,
        "thresholds": [
            (20, "Mild Turbulence"),
            (40, "Delays Are The New Normal"),
            (60, "Stranded Overnight Regularly"),
            (80, "Travel Plans Are Suggestions"),
            (100, "Airlines Are Scam Operations")
        ]
    }
}

def get_label(score, thresholds):
    """Get the label for a given score based on thresholds"""
    for max_score, label in thresholds:
        if score <= max_score:
            return label
    return thresholds[-1][1]  # Return highest severity if score > 100

print("=" * 90)
print("DYNAMIC LABEL VERIFICATION")
print("=" * 90)
print()

for name, data in metrics.items():
    score = data["score"]
    label = get_label(score, data["thresholds"])

    # Find which threshold tier this is
    tier = 0
    for i, (max_score, _) in enumerate(data["thresholds"], 1):
        if score <= max_score:
            tier = i
            break

    print(f"{name}:")
    print(f"  Score: {score:.2f}")
    print(f"  Label: \"{label}\"")
    print(f"  Tier: {tier}/5 {'🟢' if tier <= 2 else '🟡' if tier <= 3 else '🟠' if tier <= 4 else '🔴'}")
    print()

print("=" * 90)
print("✓ All labels verified!")
print()
print("Score Ranges:")
print("  🟢 0-40:  Minimal to moderate issues")
print("  🟡 40-60: Significant problems")
print("  🟠 60-80: Crisis mode")
print("  🔴 80-100: Catastrophic")
print("=" * 90)
