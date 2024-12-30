def save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year1, month1, day1, year2, month2, day2):
    minor_date_list[0]['year'] = year1
    minor_date_list[1]['month'] = month1
    minor_date_list[2]['day'] = day1

    greater_date_list[0]['year'] = year2
    greater_date_list[1]['month'] = month2
    greater_date_list[2]['day'] = day2
    return

def get_minor_date(year1, month1, day1, year2, month2, day2):

    minor_date_tuple = ({'year': 0},{'month':0},{'day':0})
    greater_date_tuple = ({'year': 0},{'month':0},{'day':0})
    minor_date_list = list(minor_date_tuple)
    greater_date_list = list(greater_date_tuple)

    if year1 < year2:
        # date 1 is less than date 2
        save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year1, month1, day1, year2, month2, day2)
    elif year1 > year2:
        # date 1 is greater than date 2
        save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year2, month2, day2, year1, month1, day1)
    else:
        # The years are the same
        if month1 < month2:
            # date 1 is less than date 2
            save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year1, month1, day1, year2, month2, day2)
        elif month1 > month2:
            # date 1 is greater than date 2
            save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year2, month2, day2, year1, month1, day1)
        else:
            # the months are the same 
            if day1 < day2:
                # date 1 is less than date 2
                save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year1, month1, day1, year2, month2, day2)
            elif day1 >= day2:
                # date 1 is greater than date 2
                save_dates_in_tuple_in_ascending_order(minor_date_list, greater_date_list, year2, month2, day2, year1, month1, day1)

    result = [minor_date_list, greater_date_list]
    return result

def check_leap_day(year):
    if year % 100 == 0:
        if year % 400:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    # 1st: get minor date
    minor_date_tuple = get_minor_date(year1, month1, day1, year2, month2, day2)
    months_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    delta_days = 0
    while minor_date_tuple[0][0]['year'] != minor_date_tuple[1][0]['year'] or \
        minor_date_tuple[0][1]['month'] != minor_date_tuple[1][1]['month'] or \
        minor_date_tuple[0][2]['day'] != minor_date_tuple[1][2]['day']:
        # advance only days
        if minor_date_tuple[0][0]['year'] == minor_date_tuple[1][0]['year'] and \
            minor_date_tuple[0][1]['month'] == minor_date_tuple[1][1]['month']:
            delta_days += minor_date_tuple[1][2]['day'] - minor_date_tuple[0][2]['day']
            minor_date_tuple[0][2]['day'] = minor_date_tuple[1][2]['day']
        # advance month
        else:
            # calculation of special case of February
            if minor_date_tuple[0][1]['month'] == 2:
                # check if leap month is in effect
                months_day[2] = 29 if check_leap_day(minor_date_tuple[0][0]['year']) else 28

            delta_days += months_day[minor_date_tuple[0][1]['month']] - minor_date_tuple[0][2]['day']
            
            # advance month and possibly year as well
            minor_date_tuple[0][1]['month'] +=1
            if minor_date_tuple[0][1]['month'] == 13:
                minor_date_tuple[0][1]['month'] = 1
                minor_date_tuple[0][0]['year'] +=1
            # reset day of the month
            minor_date_tuple[0][2]['day'] = 1
            delta_days +=1
            
    return delta_days

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()