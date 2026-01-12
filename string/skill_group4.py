# Use the .replace() method to replace part of a string.
# Use the len() function to get the number of index positions in a string.
# Slice a string at a specific index position.

def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):

        p = len(old_date)

        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
        return new_schedule

    return schedule

print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
print(replace_date("In April, the CEO will hold a conference", "April", "May"))