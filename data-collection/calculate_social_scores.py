import csv
import math

def calculate_social_score(csv_file):
    """
    Calculate engagement-weighted severity score from CSV data.
    
    Formula:
    1. Each video contributes: severity_weight × log10(views + 1)
    2. Severity weights: L1=0.33, L2=0.67, L3=1.0
    3. Normalize to 0-100 scale
    """
    
    severity_weights = {
        'LEVEL_1_AWARE': 0.33,
        'LEVEL_2_STRUGGLING': 0.67,
        'LEVEL_2_FRUSTRATED': 0.67,  # Same as struggling
        'LEVEL_3_CRISIS': 1.0
    }
    
    total_weighted_score = 0
    total_engagement = 0
    
    level_counts = {'L1': 0, 'L2': 0, 'L3': 0}
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            category = row['category']
            view_count = int(row['view_count'])
            
            # Count levels
            if 'LEVEL_1' in category:
                level_counts['L1'] += 1
            elif 'LEVEL_2' in category:
                level_counts['L2'] += 1
            elif 'LEVEL_3' in category:
                level_counts['L3'] += 1
            
            # Get severity weight
            severity = severity_weights.get(category, 0.33)
            
            # Calculate engagement weight (logarithmic)
            engagement = math.log10(view_count + 1)
            
            # Add contribution
            total_weighted_score += severity * engagement
            total_engagement += engagement
    
    # Calculate final score (0-100 scale)
    if total_engagement == 0:
        social_score = 0
    else:
        social_score = (total_weighted_score / total_engagement) * 100
    
    return social_score, level_counts

# Test on Healthcare
print("=" * 80)
print("CALCULATING SOCIAL SCORES (Engagement-Weighted Severity)")
print("=" * 80)
print()

# Healthcare
healthcare_score, hc_levels = calculate_social_score('collected-data/healthcare_youtube_20251220_010458.csv')
print("Healthcare (What Healthcare?):")
print(f"  Level 1: {hc_levels['L1']}")
print(f"  Level 2: {hc_levels['L2']}")
print(f"  Level 3: {hc_levels['L3']}")
print(f"  Social Score: {healthcare_score:.2f}")
print()

# Subscription Overload
sub_score, sub_levels = calculate_social_score('collected-data/subscription_overload_youtube_20251220_010342.csv')
print("Subscription Overload:")
print(f"  Level 1: {sub_levels['L1']}")
print(f"  Level 2: {sub_levels['L2']}")
print(f"  Level 3: {sub_levels['L3']}")
print(f"  Social Score: {sub_score:.2f}")
print()

print("=" * 80)
print("FORMULA TEST: (Official × 0.4) + (Social × 0.6)")
print("=" * 80)
print()

# Healthcare final score
hc_official = 36.17
hc_final = (hc_official * 0.4) + (healthcare_score * 0.6)
print(f"Healthcare: ({hc_official} × 0.4) + ({healthcare_score:.2f} × 0.6) = {hc_final:.2f}")

# Subscription final score
sub_official = 45.2
sub_final = (sub_official * 0.4) + (sub_score * 0.6)
print(f"Subscription: ({sub_official} × 0.4) + ({sub_score:.2f} × 0.6) = {sub_final:.2f}")
print()

