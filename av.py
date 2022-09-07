from datetime import datetime
import time
from db import ava, insert_av

def available(S_time,E_time,db_name):#Check if the time of the meeting if possiblr with unix time stamp 
    # converions :
    E_time=time.mktime(datetime(int(E_time[slice(4)]), int(E_time[slice(5,7)]),int(E_time[slice(8,10)]), int(E_time[slice(11,13)]), int(E_time[slice(14,16)]), int(E_time[slice(5,7)]), 00).timetuple())
    S_time=time.mktime(datetime(int(S_time[slice(4)]), int(S_time[slice(5,7)]),int(S_time[slice(8,10)]), int(S_time[slice(11,13)]), int(S_time[slice(14,16)]), int(S_time[slice(5,7)]), 00).timetuple())
    L= ava(db_name)
    c=len(L)//2
    for i in range(c):# for each line of availibilities
        S=time.mktime(L[i*2].timetuple())
        E=time.mktime(L[i*2+1].timetuple())
        a=S <S_time and E_time< E
        if i<c-1 and a:
            L[i*2+1]=datetime. fromtimestamp(S_time)
            L[i*2+2]=datetime. fromtimestamp(E_time)
            insert_av(L,db_name)
            return(True)
        if i==c-1 and a :#last line
            L[i*2+1]=datetime. fromtimestamp(S_time)
            L.append(datetime. fromtimestamp(E_time))
            L.append(datetime(2050, 9,8,00,00))
            insert_av(L,db_name)
            return(True)
    return (False)
