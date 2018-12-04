from pprint import pprint
import numpy as np

entries = []
with open('input.txt') as f:
    for line in f:
        entries.append((line[:18], line[19:-1]))

entries.sort(key=lambda x: x[0])

grouped = []
tmp = []
for l in entries:
    if l[1][0] == 'G':
        if tmp != []:
            grouped.append(tmp)
        tmp = []
        tmp.append(l)
    else:
        tmp.append(l)

guards = {}

for day in grouped:
    asleep = np.zeros((60))
    guard = day[0]
    guard_id = guard[1].split(' ')[1][1:]
    moments = len(day[1:])
    events = int(moments/2)
    for i in range(events):
        entry = 2*i+1
        sleep = day[entry]
        wakeup = day[entry+1]
        sleeptime = int(sleep[0][15:17])
        wakeuptime = int(wakeup[0][15:17])
        asleep[sleeptime:wakeuptime] = 1
    
    try:
        guards[guard_id] += asleep
    except:
        guards[guard_id] = asleep

best_guard = 0
best_minute = 0
highest = 0

for key, value in guards.items():
    if np.max(value) > highest:
        highest = np.max(value)
        best_minute = np.argmax(value)
        best_guard = key

print(int(best_guard) * int(best_minute))

