def date_to_days(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 2:
        leap_years = (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    else:
        leap_years = year // 4 - year // 100 + year // 400
    total_days = year * 365 + leap_years + sum(days_in_month[:month]) + day
    return total_days

def calculate_time_ranges(birth_date, death_date):
    birth_d, birth_m, birth_y = birth_date
    death_d, death_m, death_y = death_date

    adulthood_d = birth_d
    adulthood_m = birth_m
    adulthood_y = birth_y + 18

    senior_d = birth_d
    senior_m = birth_m
    senior_y = birth_y + 80

    start = date_to_days(adulthood_d, adulthood_m, adulthood_y)
    end = date_to_days(senior_d, senior_m, senior_y)

    if end < start or date_to_days(death_d, death_m, death_y) < start:
        return None
    if date_to_days(death_d, death_m, death_y) < end:
        end = date_to_days(death_d, death_m, death_y)

    return start, end

def max_contemporaries(n, people_data):
    time_ranges = []

    for person in people_data:
        birth_date = person[:3]
        death_date = person[3:]
        time_range = calculate_time_ranges(birth_date, death_date)
        if time_range:
            time_ranges.append(time_range)
    time_ranges.sort()

    max_count = 0
    end_times = []

    for start, end in time_ranges:
        end_times = [end for end in end_times if end > start]
        end_times.append(end)
        max_count = max(max_count, len(end_times))

    return max_count

print(max_contemporaries(3, [[2, 5, 1980, 13, 11, 2055], [1, 1, 1982, 1, 1, 2030], [2, 1, 1920, 2, 1, 2000]]))