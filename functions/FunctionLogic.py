work_hours=[('abc',486),('bca',233),('cab',645),('dws',432)]

def find_best_emp(workhours):
    current_max=0
    current_best_emp=''
    for emp,hr in workhours:
        if hr>current_max:
            current_max=hr
            current_best_emp=emp
        else:
            pass

    return (current_best_emp,current_max)

print(find_best_emp(work_hours))