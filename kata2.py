# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

for days in range(1, 31): #range
    if days % 3 == 0 and days % 5 == 0:
        print(f"Day {days}: FULL AUDIT") #complete audit test
    elif days % 3 == 0:
        print(f"Day {days}: Cycle count") #cycle count
    elif days % 5 == 0:
        print(f"Day {days}: Scanner audit") #scanner testing
    else:
        print(f"Day {days}: Normal operations") #regular scheduled days