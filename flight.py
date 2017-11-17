tailnumbers=['T1','T2','T3','T4','T5','T6']

src_des_time = {'hou dal':65,
                     'hou aus':45,
                     'dal hou':65,
                     'aus hou':45,
                     'aus dal':50,
                     'dal aus':50}

gd_time = {'houton_g2':35,
           'austin_g1':25,
           'dallas_g1':30,
           'dallas_g2':30,
           'houton_g1':35,
           'houton_g3':35}

#printing the airport names from gate names
def city_name (Gate):
    if Gate[:1] == 'a':
        Loc = 'aus'
        return Loc;
    elif Gate[:1] == 'd':
        Loc = 'dal'
        return Loc;
    elif Gate[:1] == 'h':
        Loc = 'hou'
        return Loc;
startairportT1='houton_g1'
startairportT2='austin_g1'
startairportT3='houton_g2'
startairportT4='houton_g3'
startairportT5='dallas_g1'
startairportT6='dallas_g2'

finalairportT1='austin_g1'
finalairportT2='houton_g1'
finalairportT3='dallas_g1'
finalairportT4='dallas_g2'
finalairportT5='houton_g2'
finalairportT6='houton_g3'

#zero padding to tome
def converttime (Time):
    
    Time = ('{:04}'.format(Time))
    return Time;

Dep_Now_T1 = 600
Dep_Now_T2 = 600
Dep_Now_T3 = 600
Dep_Now_T4 = 600
Dep_Now_T5 = 600
Dep_Now_T6 = 600


Arr_Now_T1 = 645
Arr_Now_T2 = 645
Arr_Now_T3 = 705
Arr_Now_T4 = 705
Arr_Now_T5 = 705
Arr_Now_T6 = 705

Dep_Now_T1_ini = converttime (Dep_Now_T1)
Dep_Now_T2_ini = converttime (Dep_Now_T2)
Dep_Now_T3_ini = converttime (Dep_Now_T3)
Dep_Now_T4_ini = converttime (Dep_Now_T4)
Dep_Now_T5_ini = converttime (Dep_Now_T5)
Dep_Now_T6_ini = converttime (Dep_Now_T6)


Arr_Now_T1_ini = converttime (Arr_Now_T1)
Arr_Now_T2_ini = converttime (Arr_Now_T2)
Arr_Now_T3_ini = converttime (Arr_Now_T3)
Arr_Now_T4_ini = converttime (Arr_Now_T4)
Arr_Now_T5_ini = converttime (Arr_Now_T5)
Arr_Now_T6_ini = converttime (Arr_Now_T6)

def timeconvertion_midtomilitart(time):
    time1=str('{:02}'.format(time//60))+('{:02}'.format(time%60))
    return time1;


def timeconvertion_militartomid(time1):
    ZeroPadTime=('{:04}'.format(time1))
    time=(int(str(ZeroPadTime)[:2])*60)+(int(str(ZeroPadTime)[2:]))
    return time
    
arrival_t1=austin_g1=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T1)+src_des_time[startairportT1[:3]+' '+finalairportT1[:3]]))
arrival_t2=houton_g1=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T2)+src_des_time[startairportT2[:3]+' '+finalairportT2[:3]]))
arrival_t3=dallas_g1=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T3)+src_des_time[startairportT3[:3]+' '+finalairportT3[:3]]))
arrival_t4=dallas_g2=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T4)+src_des_time[startairportT4[:3]+' '+finalairportT4[:3]]))
arrival_t5=houton_g2=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T5)+src_des_time[startairportT5[:3]+' '+finalairportT5[:3]]))
arrival_t6=houton_g3=int(timeconvertion_midtomilitart(timeconvertion_militartomid(Dep_Now_T6)+src_des_time[startairportT6[:3]+' '+finalairportT6[:3]]))

Flight_Schedule=[['T1','HOU','AUS','0600','0645'],
                ['T2','AUS','HOU','0600','0645'],
                ['T3','HOU','DAL','0600','0705'],
                ['T4','HOU','DAL','0600','0705'],
                ['T5','DAL','HOU','0600','0705'],
                ['T6','DAL','HOU','0600','0705']]





def changedeptime(ori, dest, arrival_next):
    arrival_next = int(arrival_next)
    arrival_next = timeconvertion_militartomid (arrival_next)
    if((ori=='hou' and dest=='aus')or(ori=='aus' and dest=='hou')):
        nxtdpt = arrival_next - src_des_time[ori[:3]+' '+dest]
        nxtdpt = timeconvertion_midtomilitart(nxtdpt)
        return nxtdpt;
    elif((ori=='dal' and dest=='aus')or(ori=='aus' and dest=='dal')):
        nxtdpt = arrival_next - src_des_time[ori[:3]+' '+dest]
        nxtdpt = timeconvertion_midtomilitart(nxtdpt)
        return nxtdpt;
    elif((ori=='dal' and dest=='hou')or(ori=='hou' and dest=='dal')):
        nxtdpt = arrival_next - src_des_time[ori[:3]+' '+dest]
        nxtdpt = timeconvertion_midtomilitart(nxtdpt)
        return nxtdpt;


def PrintFlightSchedule(fn, csv_hdr, flt_sched): 
    with open(fn,'wt') as f:
        print(csv_hdr, file=f) 
        for s in flt_sched:
            print(','.join(s), file=f)
def nextdeparture_time (T,Arrival,destination):
    gd_time = {'dallas_g1':30,'dallas_g2':30,'houton_g1':35,'houton_g2':35,'houton_g3':35,'austin_g1':25}
    if T == 'T1':
        next_depart_t1=Arrival+gd_time[destination]
        return next_depart_t1;
    if T == 'T2':
        next_depart_t2=Arrival+gd_time[destination]
        return next_depart_t2;
    if T == 'T3':
        next_depart_t3=Arrival+gd_time[destination]
        return next_depart_t3;
    if T == 'T4':
        next_depart_t4=Arrival+gd_time[destination]
        return next_depart_t4;
    if T == 'T5':
        next_depart_t5=Arrival+gd_time[destination]
        return next_depart_t5;
    if T == 'T6':
        next_depart_t6=Arrival+gd_time[destination]
        return next_depart_t6;   


def nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, nxtdpt, Origin):
    nxtdpt = int(nxtdpt)
    nxtdpt = timeconvertion_militartomid(nxtdpt)
    MaxGrndTime=36
    austin_g1 = timeconvertion_militartomid(austin_g1)
    dallas_g1 = timeconvertion_militartomid(dallas_g1)
    dallas_g2 = timeconvertion_militartomid(dallas_g2)
    houton_g1 = timeconvertion_militartomid(houton_g1)
    houton_g2 = timeconvertion_militartomid(houton_g2)
    houton_g3 = timeconvertion_militartomid(houton_g3)
    if T == 'T1':
        if Origin[:1] == 'a':
            increment = 1
            while (increment<36):
                if nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t1 = nxtdpt + 50 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'dallas_g1'
                    return military_nextarrivaltime_t1_Dest; 
                elif nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t1 = nxtdpt + 45 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g3'
                    return military_nextarrivaltime_t1_Dest; 
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t1 = nxtdpt + 45 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g1'
                    return military_nextarrivaltime_t1_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t1 = nxtdpt + 45 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g2'
                    return military_nextarrivaltime_t1_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t1 = nxtdpt + 50 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'dallas_g2'
                    return military_nextarrivaltime_t1_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while (increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t1 = nxtdpt + 50 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'austin_g1'
                    return military_nextarrivaltime_t1_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t1 = nxtdpt + 65 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g1'
                    return military_nextarrivaltime_t1_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t1 = nxtdpt + 65 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g2'
                    return military_nextarrivaltime_t1_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t1 = nxtdpt + 65 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'houton_g3'
                    return military_nextarrivaltime_t1_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        else:
            increment = 1
            while (increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t1 = nxtdpt + 45 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'austin_g1'
                    return military_nextarrivaltime_t1_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t1 = nxtdpt + 65 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'dallas_g1'
                    return military_nextarrivaltime_t1_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t1 = nxtdpt + 65 
                    military_nextarrivaltime_t1 = timeconvertion_midtomilitart(midnight_next_arrival_t1)
                    military_nextarrivaltime_t1_Dest = military_nextarrivaltime_t1 + 'dallas_g2'
                    return military_nextarrivaltime_t1_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
    elif T == 'T2':
        if Origin[:1] == 'a':
            increment = 1
            while (increment<36):
                if nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t2 = nxtdpt + 45 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g3'
                    return military_nextarrivaltime_t2_Dest;
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t2 = nxtdpt + 45 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g1'
                    return military_nextarrivaltime_t2_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t2 = nxtdpt + 45 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g2'
                    return military_nextarrivaltime_t2_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t2 = nxtdpt + 50 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'dallas_g2'
                    return military_nextarrivaltime_t2_Dest;
                elif nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t2 = nxtdpt + 50 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'dallas_g1'
                    return military_nextarrivaltime_t2_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while (increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t2 = nxtdpt + 50 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'austin_g1'
                    return military_nextarrivaltime_t2_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t2 = nxtdpt + 65 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g1'
                    return military_nextarrivaltime_t2_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t2 = nxtdpt + 65 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g2'
                    return military_nextarrivaltime_t2_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t2 = nxtdpt + 65 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'houton_g3'
                    return military_nextarrivaltime_t2_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        else:
            increment = 1
            while (increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t2 = nxtdpt + 45 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'austin_g1'
                    return military_nextarrivaltime_t2_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t2 = nxtdpt + 65 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'dallas_g1'
                    return military_nextarrivaltime_t2_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t2 = nxtdpt + 65 
                    military_nextarrivaltime_t2 = timeconvertion_midtomilitart(midnight_next_arrival_t2)
                    military_nextarrivaltime_t2_Dest = military_nextarrivaltime_t2 + 'dallas_g2'
                    return military_nextarrivaltime_t2_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
    elif T == 'T3':
        if Origin[:1] == 'a':
            increment = 1
            while(increment<36):
                if nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t3 = nxtdpt + 50 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'dallas_g1'
                    return military_nextarrivaltime_t3_Dest; 
                elif nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t3 = nxtdpt + 45 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g3'
                    return military_nextarrivaltime_t3_Dest;
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t3 = nxtdpt + 45 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g1'
                    return military_nextarrivaltime_t3_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t3 = nxtdpt + 45 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g2'
                    return military_nextarrivaltime_t3_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t3 = nxtdpt + 50 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'dallas_g2'
                    return military_nextarrivaltime_t3_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while (increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t3 = nxtdpt + 50 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'austin_g1'
                    return military_nextarrivaltime_t3_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t3 = nxtdpt + 65 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g1'
                    return military_nextarrivaltime_t3_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t3 = nxtdpt + 65 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g2'
                    return military_nextarrivaltime_t3_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t3 = nxtdpt + 65 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'houton_g3'
                    return military_nextarrivaltime_t3_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        else:
            increment = 1
            while(increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t3 = nxtdpt + 45 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'austin_g1'
                    return military_nextarrivaltime_t3_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t3 = nxtdpt + 65 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'dallas_g1'
                    return military_nextarrivaltime_t3_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t3 = nxtdpt + 65 
                    military_nextarrivaltime_t3 = timeconvertion_midtomilitart(midnight_next_arrival_t3)
                    military_nextarrivaltime_t3_Dest = military_nextarrivaltime_t3 + 'dallas_g2'
                    return military_nextarrivaltime_t3_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
    elif T == 'T4':
        if Origin[:1] == 'a':
            increment = 1
            while(increment<36):
                if nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t4 = nxtdpt + 45 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g3'
                    return military_nextarrivaltime_t4_Dest;
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t4 = nxtdpt + 45 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g1'
                    return military_nextarrivaltime_t4_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t4 = nxtdpt + 45 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g2'
                    return military_nextarrivaltime_t4_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t4 = nxtdpt + 50 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'dallas_g2'
                    return military_nextarrivaltime_t4_Dest;
                elif nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t4 = nxtdpt + 50 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'dallas_g1'
                    return military_nextarrivaltime_t4_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while(increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t4 = nxtdpt + 50 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'austin_g1'
                    return military_nextarrivaltime_t4_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t4 = nxtdpt + 65 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g1'
                    return military_nextarrivaltime_t4_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t4 = nxtdpt + 65 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g2'
                    return military_nextarrivaltime_t4_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t4 = nxtdpt + 65 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'houton_g3'
                    return military_nextarrivaltime_t4_Dest;  
        else:
            increment = 1
            while (increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t4 = nxtdpt + 45 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'austin_g1'
                    return military_nextarrivaltime_t4_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t4 = nxtdpt + 65 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'dallas_g1'
                    return military_nextarrivaltime_t4_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t4 = nxtdpt + 65 
                    military_nextarrivaltime_t4 = timeconvertion_midtomilitart(midnight_next_arrival_t4)
                    military_nextarrivaltime_t4_Dest = military_nextarrivaltime_t4 + 'dallas_g2'
                    return military_nextarrivaltime_t4_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
    elif T == 'T5':
        if Origin[:1] == 'a':
            increment = 1
            while(increment<36):
                if nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t5 = nxtdpt + 50 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'dallas_g1'
                    return military_nextarrivaltime_t5_Dest; 
                elif nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t5 = nxtdpt + 45 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g3'
                    return military_nextarrivaltime_t5_Dest;
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t5 = nxtdpt + 45 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g1'
                    return military_nextarrivaltime_t5_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t5 = nxtdpt + 45 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g2'
                    return military_nextarrivaltime_t5_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t5 = nxtdpt + 50 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'dallas_g2'
                    return military_nextarrivaltime_t5_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while(increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t5 = nxtdpt + 50 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'austin_g1'
                    return military_nextarrivaltime_t5_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t5 = nxtdpt + 65 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g1'
                    return military_nextarrivaltime_t5_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t5 = nxtdpt + 65 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g2'
                    return military_nextarrivaltime_t5_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t5 = nxtdpt + 65 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'houton_g3'
                    return military_nextarrivaltime_t5_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        else:
            increment = 1
            while(increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t5 = nxtdpt + 45 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'austin_g1'
                    return military_nextarrivaltime_t5_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t5 = nxtdpt + 65 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'dallas_g1'
                    return military_nextarrivaltime_t5_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t5 = nxtdpt + 65 
                    military_nextarrivaltime_t5 = timeconvertion_midtomilitart(midnight_next_arrival_t5)
                    military_nextarrivaltime_t5_Dest = military_nextarrivaltime_t5 + 'dallas_g2'
                    return military_nextarrivaltime_t5_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
    else:
        if Origin[:1] == 'a':
            increment = 1
            while(increment<36):
                if nxtdpt+45 > houton_g3+35:
                    midnight_next_arrival_t6 = nxtdpt + 45 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g3'
                    return military_nextarrivaltime_t6_Dest;
                elif nxtdpt+45 > houton_g1+35:
                    midnight_next_arrival_t6 = nxtdpt + 45 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g1'
                    return military_nextarrivaltime_t6_Dest;
                elif nxtdpt+45 > houton_g2+35:
                    midnight_next_arrival_t6 = nxtdpt + 45 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g2'
                    return military_nextarrivaltime_t6_Dest; 
                elif nxtdpt+50 > dallas_g2+30:
                    midnight_next_arrival_t6 = nxtdpt + 50 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'dallas_g2'
                    return military_nextarrivaltime_t6_Dest;
                elif nxtdpt+50 > dallas_g1+30:
                    midnight_next_arrival_t6 = nxtdpt + 50 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'dallas_g1'
                    return military_nextarrivaltime_t6_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        elif Origin[:1] == 'd':
            increment = 1
            while(increment<36):
                if nxtdpt+50 > austin_g1+25:
                    midnight_next_arrival_t6 = nxtdpt + 50 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'austin_g1'
                    return military_nextarrivaltime_t6_Dest;  
                elif nxtdpt+65 > houton_g1+35:
                    midnight_next_arrival_t6 = nxtdpt + 65 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g1'
                    return military_nextarrivaltime_t6_Dest;  
                elif nxtdpt+65 > houton_g2+35:
                    midnight_next_arrival_t6 = nxtdpt + 65 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g2'
                    return military_nextarrivaltime_t6_Dest;  
                elif nxtdpt+65 > houton_g3+35:
                    midnight_next_arrival_t6 = nxtdpt + 65 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'houton_g3'
                    return military_nextarrivaltime_t6_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1
        else:
            increment = 1
            while(increment<31):
                if nxtdpt+45 > austin_g1+25:
                    midnight_next_arrival_t6 = nxtdpt + 45 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'austin_g1'
                    return military_nextarrivaltime_t6_Dest;  
                elif nxtdpt+65 > dallas_g1+30:
                    midnight_next_arrival_t6 = nxtdpt + 65 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'dallas_g1'
                    return military_nextarrivaltime_t6_Dest;  
                elif nxtdpt+65 > dallas_g2+30:
                    midnight_next_arrival_t6 = nxtdpt + 65 
                    military_nextarrivaltime_t6 = timeconvertion_midtomilitart(midnight_next_arrival_t6)
                    military_nextarrivaltime_t6_Dest = military_nextarrivaltime_t6 + 'dallas_g2'
                    return military_nextarrivaltime_t6_Dest;
                else:
                    nxtdpt = nxtdpt + 1
                    increment = increment + 1





loop=1
while (loop<11):
    for T in tailnumbers:
        if T == 'T1':
            midnightarrivaltime_t1 = timeconvertion_militartomid (arrival_t1)
            nxtdptTimeMid_T1 = nextdeparture_time(T, midnightarrivaltime_t1, finalairportT1)
            next_depart_t1 = timeconvertion_midtomilitart(nxtdptTimeMid_T1)
            startairportT1 = finalairportT1
            military_nextarrivaltime_t1_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t1, startairportT1)
            military_nextarrivaltime_t1 = military_nextarrivaltime_t1_Dest[0:4]
            UpdatedDestination_T1 = military_nextarrivaltime_t1_Dest[4:]
            finalairportT1 = UpdatedDestination_T1
            arrival_t1 = int(military_nextarrivaltime_t1)
            if UpdatedDestination_T1 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t1)
            elif UpdatedDestination_T1 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t1)
            elif UpdatedDestination_T1 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t1)
            elif UpdatedDestination_T1 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t1)
            elif UpdatedDestination_T1 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t1)
            else:
                houton_g3 = int(military_nextarrivaltime_t1)
            Origin_T1 = city_name(startairportT1)
            Destination_T1 = city_name(finalairportT1)
            next_depart_t1 = changedeptime(Origin_T1, Destination_T1, military_nextarrivaltime_t1)
            Schedule_T1 = [T, Origin_T1, Destination_T1, next_depart_t1, military_nextarrivaltime_t1]
        elif T == 'T2':
            midnightarrivaltime_t2 = timeconvertion_militartomid (arrival_t2)
            nxtdptTimeMid_T2 = nextdeparture_time(T, midnightarrivaltime_t2, finalairportT2)
            next_depart_t2 = timeconvertion_midtomilitart(nxtdptTimeMid_T2)
            startairportT2 = finalairportT2
            military_nextarrivaltime_t2_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t2, startairportT2)
            military_nextarrivaltime_t2 = military_nextarrivaltime_t2_Dest[0:4]
            UpdatedDestination_T2 = military_nextarrivaltime_t2_Dest[4:]
            finalairportT2 = UpdatedDestination_T2
            arrival_t2 = int(military_nextarrivaltime_t2)
            if UpdatedDestination_T2 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t2)
            elif UpdatedDestination_T2 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t2)
            elif UpdatedDestination_T2 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t2)
            elif UpdatedDestination_T2 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t2)
            elif UpdatedDestination_T2 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t2)
            else:
                houton_g3 = int(military_nextarrivaltime_t2)
            Origin_T2 = city_name(startairportT2)
            Destination_T2 = city_name(finalairportT2)
            next_depart_t2 = changedeptime(Origin_T2, Destination_T2, military_nextarrivaltime_t2)
            Schedule_T2 = [T, Origin_T2, Destination_T2, next_depart_t2, military_nextarrivaltime_t2]
        elif T == 'T3':
            midnightarrivaltime_t3 = timeconvertion_militartomid (arrival_t3)
            nxtdptTimeMid_T3 = nextdeparture_time(T, midnightarrivaltime_t3, finalairportT3)
            next_depart_t3 = timeconvertion_midtomilitart(nxtdptTimeMid_T3)
            startairportT3 = finalairportT3
            military_nextarrivaltime_t3_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t3, startairportT3)
            military_nextarrivaltime_t3 = military_nextarrivaltime_t3_Dest[0:4]
            UpdatedDestination_T3 = military_nextarrivaltime_t3_Dest[4:]
            finalairportT3 = UpdatedDestination_T3
            arrival_t3 = int(military_nextarrivaltime_t3)
            if UpdatedDestination_T3 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t3)
            elif UpdatedDestination_T3 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t3)
            elif UpdatedDestination_T3 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t3)
            elif UpdatedDestination_T3 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t3)
            elif UpdatedDestination_T3 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t3)
            else:
                houton_g3 = int(military_nextarrivaltime_t3)
            Origin_T3 = city_name(startairportT3)
            Destination_T3 = city_name(finalairportT3)
            next_depart_t3 = changedeptime(Origin_T3, Destination_T3, military_nextarrivaltime_t3)
            Schedule_T3 = [T, Origin_T3, Destination_T3, next_depart_t3, military_nextarrivaltime_t3]
        elif T == 'T4':
            midnightarrivaltime_t4 = timeconvertion_militartomid (arrival_t4)
            nxtdptTimeMid_T4 = nextdeparture_time(T, midnightarrivaltime_t4, finalairportT4)
            next_depart_t4 = timeconvertion_midtomilitart(nxtdptTimeMid_T4)
            startairportT4 = finalairportT4
            military_nextarrivaltime_t4_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t4, startairportT4)
            military_nextarrivaltime_t4 = military_nextarrivaltime_t4_Dest[0:4]
            UpdatedDestination_T4 = military_nextarrivaltime_t4_Dest[4:]
            finalairportT4 = UpdatedDestination_T4
            arrival_t4 = int(military_nextarrivaltime_t4)
            if UpdatedDestination_T4 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t4)
            elif UpdatedDestination_T4 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t4)
            elif UpdatedDestination_T4 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t4)
            elif UpdatedDestination_T4 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t4)
            elif UpdatedDestination_T4 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t4)
            else:
                houton_g3 = int(military_nextarrivaltime_t4)
            Origin_T4 = city_name(startairportT4)
            Destination_T4 = city_name(finalairportT4)
            next_depart_t4 = changedeptime(Origin_T4, Destination_T4, military_nextarrivaltime_t4)
            Schedule_T4 = [T, Origin_T4, Destination_T4, next_depart_t4, military_nextarrivaltime_t4]
        elif T == 'T5':
            midnightarrivaltime_t5 = timeconvertion_militartomid (arrival_t5)
            nxtdptTimeMid_T5 = nextdeparture_time(T, midnightarrivaltime_t5, finalairportT5)
            next_depart_t5 = timeconvertion_midtomilitart(nxtdptTimeMid_T5)
            startairportT5 = finalairportT5
            military_nextarrivaltime_t5_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t5, startairportT5)
            military_nextarrivaltime_t5 = military_nextarrivaltime_t5_Dest[0:4]
            UpdatedDestination_T5 = military_nextarrivaltime_t5_Dest[4:]
            finalairportT5 = UpdatedDestination_T5
            arrival_t5 = int(military_nextarrivaltime_t5)
            if UpdatedDestination_T5 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t5)
            elif UpdatedDestination_T5 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t5)
            elif UpdatedDestination_T5 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t5)
            elif UpdatedDestination_T5 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t5)
            elif UpdatedDestination_T5 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t5)
            else:
                houton_g3 = int(military_nextarrivaltime_t5)
            Origin_T5 = city_name(startairportT5)
            Destination_T5 = city_name(finalairportT5)
            next_depart_t5 = changedeptime(Origin_T5, Destination_T5, military_nextarrivaltime_t5)
            Schedule_T5 = [T, Origin_T5, Destination_T5, next_depart_t5, military_nextarrivaltime_t5]
        else:
            midnightarrivaltime_t6 = timeconvertion_militartomid (arrival_t6)
            nxtdptTimeMid_T6 = nextdeparture_time(T, midnightarrivaltime_t6, finalairportT6)
            next_depart_t6 = timeconvertion_midtomilitart(nxtdptTimeMid_T6)
            startairportT6 = finalairportT6
            military_nextarrivaltime_t6_Dest = nextarr_time (T, austin_g1, dallas_g1, dallas_g2, houton_g1, houton_g2, houton_g3, next_depart_t6, startairportT6)
            military_nextarrivaltime_t6 = military_nextarrivaltime_t6_Dest[0:4]
            UpdatedDestination_T6 = military_nextarrivaltime_t6_Dest[4:]
            finalairportT6 = UpdatedDestination_T6
            arrival_t6 = int(military_nextarrivaltime_t6)
            if UpdatedDestination_T6 == 'austin_g1':
                austin_g1 = int(military_nextarrivaltime_t6)
            elif UpdatedDestination_T6 == 'dallas_g1':
                dallas_g1 = int(military_nextarrivaltime_t6)
            elif UpdatedDestination_T6 == 'dallas_g2':
                dallas_g2 = int(military_nextarrivaltime_t6)
            elif UpdatedDestination_T6 == 'houton_g1':
                houton_g1 = int(military_nextarrivaltime_t6)
            elif UpdatedDestination_T6 == 'houton_g2':
                houton_g2 = int(military_nextarrivaltime_t6)
            else:
                houton_g3 = int(military_nextarrivaltime_t6)
            Origin_T6 = city_name(startairportT6)
            Destination_T6 = city_name(finalairportT6)
            next_depart_t6 = changedeptime(Origin_T6, Destination_T6, military_nextarrivaltime_t6)
            Schedule_T6 = [T, Origin_T6, Destination_T6, next_depart_t6, military_nextarrivaltime_t6]
    loop = loop + 1
    Schedule = [[x.upper() for x in Schedule_T1], [x.upper() for x in Schedule_T2], [x.upper() for x in Schedule_T3], [x.upper() for x in Schedule_T4], [x.upper() for x in Schedule_T5], [x.upper() for x in Schedule_T6]]
    Flight_Schedule = Flight_Schedule + Schedule
    print(Flight_Schedule)
    csv_header = 'tail_number,origin,destination,departure_time,arrival_time'
    file_name = 'flight_schedule.csv'
    Flight_Schedule = sorted(Flight_Schedule, key = lambda x: x[0] + x[3])
    PrintFlightSchedule(file_name, csv_header, Flight_Schedule)
