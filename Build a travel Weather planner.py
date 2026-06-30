distance_mi = 5
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

# Sabse pehle check karein agar distance zero
if not distance_mi:
    print(False)

# Agar distance 1 mile ya usse kam hai
elif distance_mi <=1:
    if not is_raining:
        print(True)
    else:
        print(False) 

# agar distance 1 se 6 mile ke beech me ho

elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# agar distance 6 mile se zyada ho
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)