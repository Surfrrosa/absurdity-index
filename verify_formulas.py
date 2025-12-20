import json

# Healthcare data
healthcare = {
    "score": 72.34,
    "officialScore": 36.17,
    "crisisRatio": 60.2,
    "level3": 198,
    "total": 366
}

# Wage Stagnation data
wage = {
    "score": 19.74,
    "officialScore": 38.4,
    "crisisRatio": 7.3,
    "level3": 7,
    "total": 96
}

# Subscription Overload
subscription = {
    "score": 58.99,
    "officialScore": 45.2,
    "crisisRatio": 23.1,
    "level3": 67,
    "total": 280
}

print("=== VERIFYING FORMULAS ===\n")

for name, data in [("Healthcare", healthcare), ("Wage Stagnation", wage), ("Subscription Overload", subscription)]:
    print(f"{name}:")
    print(f"  Reported score: {data['score']}")
    print(f"  Official score: {data['officialScore']}")
    print(f"  Crisis ratio: {data['crisisRatio']}%")
    
    # Test Formula 1: (official × 0.4) + (crisis × 0.6)
    calc1 = (data['officialScore'] * 0.4) + (data['crisisRatio'] * 0.6)
    print(f"  Formula (official×0.4 + crisis×0.6): {calc1:.2f}")
    
    # Test if crisis ratio matches level distribution
    calc_crisis = (data['level3'] / data['total']) * 100
    print(f"  Calculated crisis ratio: {calc_crisis:.1f}%")
    
    # Check if there's a different formula
    # Maybe it's weighted differently?
    # Try to reverse engineer
    if data['score'] != calc1:
        print(f"  MISMATCH! Difference: {abs(data['score'] - calc1):.2f}")
        
        # Try to find actual weighting
        # score = official * w1 + crisis * w2
        # Let's solve for w1, w2
        # Assume w1 + w2 = 1
        # score = official * w1 + crisis * (1 - w1)
        # w1 = (score - crisis) / (official - crisis)
        
        if data['officialScore'] != data['crisisRatio']:
            w1 = (data['score'] - data['crisisRatio']) / (data['officialScore'] - data['crisisRatio'])
            w2 = 1 - w1
            print(f"  Reverse engineered weights: official={w1:.2f}, crisis={w2:.2f}")
    else:
        print(f"  MATCH!")
    
    print()
