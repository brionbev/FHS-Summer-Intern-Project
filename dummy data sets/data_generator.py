import random
import datetime
from fhs_utility.handle_dates import date_parse as dp

def generate_id():
    '''
    generates a random participant id in the FHS_ESxxxxx format
    '''
    fhs_id = str(random.randint(0, 99999))
    fhs_id = ((5 - len(fhs_id)) * "0") + str(fhs_id) 
    dummy_id = "FHS_ES" + fhs_id
    return dummy_id

def generate_cohort():
    '''
    generates a random cohort data 
    '''
    generation_list = ["Generation One", "Generation Two", "Generation Three"]
    gen_idx = random.randint(0, 2)
    generation = generation_list[gen_idx]
    return generation

def generate_dates(start, end):
    '''
    generates a random date between the specified date
    '''
    start_date = dp.get_dt_obj(start)
    end_date = dp.get_dt_obj(end)

    time_delta = end_date - start_date
    time_delta = time_delta.days
    rand_date = random.randrange(time_delta)
    random_date = start_date + datetime.timedelta(days=rand_date)

    fin_date = str(random_date).replace("-","")
    return fin_date[:8]

def generate_apoe():
    '''
    generates a random apoe value for apoe script
    '''
    apoe = str(random.randint(10,50))
    return [apoe, 'apoe']

def generate_dvoice_data():
    '''
    generates a random set of dvoice_data
    '''
    num_dict = random.randint(1, 5)
    temp_list = []
    for i in range(num_dict):
        date = generate_dates("20200101", "20220101")
        temp_list.append(date)
    
    temp_list.sort()
    temp_dict = {date:{} for date in temp_list}
    dates = temp_dict

    return [dates, 'dvoice_data']

def generate_edu_data():
    '''
    generates a random set of edu_data
    '''
    num_dict = random.randint(1,8)
    educ_list = [str(i) for i in range(16)]
    educ_list.insert(0,"")

    dates_list = []
    temp_dict = {}
    for i in range(num_dict):

        date = generate_dates("20200101", "20220101")
        idx = [random.randint(0,16), random.randint(0,16), random.randint(0,4), random.randint(2,4)]
        
        educ_data ={"education_b1":educ_list[idx[0]], "education_b2":educ_list[idx[1]],
        "Educg":educ_list[idx[2]], 'date':date, "handedness":educ_list[idx[3]]}
        dates_list.append(date)
        temp_dict[date] = educ_data
        
    dates_list.sort()
    sorted_dict = {}
    for date in dates_list:
        sorted_dict[date] = temp_dict[date]
    fin_dict = sorted_dict

    return [fin_dict, 'edu_data']

def generate_scan_mod():
    '''
    generates a random scanner model for PIB and TAU data set
    '''
    models = ["HR", "GE"]
    return models[random.randint(0,1)]

def generate_race_sex():
    '''
    generates random race and sex data for race_sex data set
    '''
    race_list = ["b'white'", "b'asian'", "b'more1'", "b'hispa'", "b'black'", "b'unkno'", "b'paci'", "b'am in'"]
    race = race_list[random.randint(0, len(race_list)-1)]
    sex = str(random.randint(1, 2))
    
    return [race, sex]










