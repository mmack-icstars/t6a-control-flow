# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start
Total_time = 150 #total 
for minutes in range (15, Total_time + 1, 15): #range
        print(f"check {minutes // 15}: {minutes} minutes after shift start") #label
    


