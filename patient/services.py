from datetime import datetime, timedelta
import time


def get_slots(time1, time2):

    time1 = datetime.strptime(time1, '%H:%M')
    time2 = datetime.strptime(time2, '%H:%M')
    continue_iter = True
    slots = []
    t = time1
    format1 = '%I:%M %p'
    slots.append(t.time().strftime(format1))
    while continue_iter:
        t1 = t + timedelta(minutes=10)
        
        temp1 = t1.time().strftime(format1)
        temp2 = time2.time().strftime(format1)
        print(temp1)
        slots.append(temp1)

        if temp1 == temp2:
            continue_iter = False

        t = t1

    print(slots)
    return slots


# print(get_slots('10:00','11:00'))


def create_slots(query_set):
    
     
    session_count=1
    available_session = {}
    slot_arr = []
    available_slots = []
    for i in query_set :
        available_session ={}
        key = 'session'+ str(session_count)
        session_time  = i.time.split(' - ')
        slot = get_slots(session_time[0],session_time[1])

        # print('slot iss', slot) 

        available_session[key] = slot

        available_slots.append(available_session)
        # print('sample is ',sample)
        session_count +=1

    # print('session isssss',available_session)
    slot_arr.append(available_session)
     
    return  available_slots
   
 