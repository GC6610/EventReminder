from datetime import date
from datetime import datetime
from playsound import playsound
import webbrowser


def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    result = (day + (int((13 * (month - 2)) / 5)) + year + (int(year / 4)) - (int(year / 100)) - (int(year / 400))) % 7
    return int(result) + 1


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Check your Schedule file"
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Check your Schedule file"
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Check your Schedule file"
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Check your Schedule file"
        else:
            return "ok"


today = date.today()
d1 = today.strftime("%Y%m%d")
yr = int(d1[:4])
mn = int(d1[4:6])
dy = int(d1[6:])
week_days = ["NULL", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
week_num = day_of_week(yr, mn, dy)
weekday = week_days[week_num]
myweekschedule = {'Monday': [[], [], []], 'Tuesday': [[], [], []], 'Wednesday': [[], [], []], 'Thursday': [[], [], []],
                  'Friday': [[], [], []], 'Saturday': [[], [], []], 'Sunday': [[], [], []]}

with open("schedule.txt") as myfile:
    for line in myfile:
        d = (line.strip()).split('?')
        if d[0] == '':
            break

        myweekschedule[d[0]][0].append(d[1])
        myweekschedule[d[0]][1].append(d[2])
        myweekschedule[d[0]][2].append(d[3])
todaysschedule = myweekschedule[weekday][0]
eventnum = 0
print("Today's events list :")

for i in range(len(myweekschedule[weekday][0])):
    print(myweekschedule[weekday][1][i], 'at', myweekschedule[weekday][0][i])
for i in todaysschedule:
    alarm_time = i

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)


    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()
    nm=0
    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")




        if alarm_hour == '12':
            alarm_hour = '0'
        if current_hour == '0':
            current_hour = '0'

        if current_period > alarm_period:
            print(myweekschedule[weekday][1][eventnum])
            print("The above event is already over")
            eventnum = eventnum + 1

            break



        else:
            if current_hour > alarm_hour:
                print(myweekschedule[weekday][1][eventnum])
                print("The above event is already over")
                eventnum = eventnum + 1
                break
            elif current_hour == alarm_hour:
                if current_min > alarm_min:
                    print(myweekschedule[weekday][1][eventnum])
                    print("The above event is already over")
                    eventnum = eventnum + 1
                    break
                elif current_min == alarm_min:
                    if current_sec > alarm_sec:
                        print(myweekschedule[weekday][1][eventnum])
                        print("The above event is already over")
                        eventnum = eventnum + 1
                        break
        if nm==0:
            print(f"Upcoming Event at {alarm_time}...")
            print(myweekschedule[weekday][1][eventnum])
            nm=1

        if alarm_period == current_period and alarm_hour == current_hour and alarm_min == current_min:
            if alarm_sec == current_sec:

                webbrowser.open(myweekschedule[weekday][2][eventnum])
                eventnum = eventnum + 1
                playsound('blue_monday-freemobi.mp3')
                break
