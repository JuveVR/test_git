# Classes are held on Mondays and Thursdays at 19:15
#
# The first lesson took place on April 11, 2024.
#
# Print a list of all classes in the format below (number of lecture are aligned to the right):

from datetime import datetime, timedelta


first_date = datetime(2024, 4, 11, 19, 15)
lesson_days = [0, 3]                         # Monday and Thursday
lesson_dates = []

# Calculate dates until 32 lesson reached. Not sure about 32 lessons, maybe I should count lesson until now?
current_date = first_date
lecture_count = 1

while lecture_count <= 32:
    if current_date.weekday() in lesson_days:
        lesson_dates.append(current_date)
        lecture_count += 1
    current_date += timedelta(days=1)


for lesson, lesson_date in enumerate(lesson_dates, 1):
    print(f"Lecture {lesson:2}: {lesson_date.strftime('%d %b %Y %H:%M')}")