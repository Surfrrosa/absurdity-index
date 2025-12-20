"""
Recalculate Healthcare Official Score with Uninsured Rate
"""

# Current official metrics
premium_increase_yoy = 7.0  # %
denial_rate = 18.0  # %
medical_debt_pct = 41.0  # % of adults
medical_bankruptcies = 66.5  # % of bankruptcies caused by medical debt
uninsured_rate = 8.0  # % of Americans (~26 million)

print("=" * 80)
print("HEALTHCARE OFFICIAL SCORE CALCULATION")
print("=" * 80)
print()

print("RAW METRICS:")
print(f"  Premium increase YoY: {premium_increase_yoy}%")
print(f"  Initial denial rate: {denial_rate}%")
print(f"  Adults with medical debt: {medical_debt_pct}%")
print(f"  Medical bankruptcies: {medical_bankruptcies}%")
print(f"  Uninsured rate: {uninsured_rate}%")
print()

# Normalize each metric to 0-100 scale
# Based on reasonable worst-case scenarios
premium_score = min(100, (premium_increase_yoy / 15.0) * 100)  # 15% = worst
denial_score = min(100, (denial_rate / 30.0) * 100)  # 30% = worst
debt_score = min(100, (medical_debt_pct / 60.0) * 100)  # 60% = worst
bankruptcy_score = medical_bankruptcies  # Already 0-100
uninsured_score = min(100, (uninsured_rate / 20.0) * 100)  # 20% = worst (universal coverage = 0%)

print("NORMALIZED SCORES (0-100):")
print(f"  Premium increase: {premium_score:.2f}")
print(f"  Denial rate: {denial_score:.2f}")
print(f"  Medical debt: {debt_score:.2f}")
print(f"  Bankruptcies: {bankruptcy_score:.2f}")
print(f"  Uninsured: {uninsured_score:.2f}")
print()

# Calculate official score (equal weighting across metrics)
official_score = (premium_score + denial_score + debt_score + bankruptcy_score + uninsured_score) / 5

print("OFFICIAL SCORE (average of all metrics):")
print(f"  {official_score:.2f}")
print()

print("PREVIOUS OFFICIAL SCORE: 36.17")
print(f"NEW OFFICIAL SCORE: {official_score:.2f}")
print(f"CHANGE: {official_score - 36.17:+.2f}")
print()
print("=" * 80)
