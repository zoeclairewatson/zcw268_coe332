import jobs
from jobs import q, rd1, rd
import datetime
import redis
import matplotlib.pyplot as plt

@q.worker
def execute_job(jid):
    
    data = jobs.get_job_data(jid)

    job_type = jobs.get_job_type(jid)
 
    #analysis: plot total number of outcomes for each day in date range

    if (job_type == 'dates'):
        
        start = jobs.get_job_start(jid)
        end = jobs.get_job_end(jid)
        start_date = datetime.datetime.strptime( start, "%m-%d-%Y")
        end_date = datetime.datetime.strptime( end, '%m-%d-%Y')

        consecutive_dates = [start_date+datetime.timedelta(days=x) for x in range((end_date-start_date).days+1)]

        list_of_all_dates = []
        
        for key in rd1.keys():

            key_time_temp = rd1.hget(key,'Date_of_Entry').decode('utf-8').split()[0]
            key_time = datetime.datetime.strptime(key_time_temp, '%m-%d-%Y')
            list_of_all_dates.append(key_time)
 
        list_of_outcomes_of_the_day = [0] * len(consecutive_dates)

        x_labeler = []

        for i in range(len(consecutive_dates)):
            list_of_outcomes_of_the_day[i] = list_of_all_dates.count(consecutive_dates[i])
            x_labeler.append(i)
       
        #consecutive_date_strings = []

        #for item in consecutive_dates:
        #    consecutive_date_strings.append(item.strftime("%m-%d-%Y"))
         

        plt.clf()
        plt.bar(x_labeler, list_of_outcomes_of_the_day, color='green')
        plt.xlabel('Days since Start')
        plt.ylabel('# Outcomes per Day')
        plt.title('Outcome Occurences by Day \n' + start + ' - ' + end )
       
        plt.savefig('/outcomes_by_animal_type.png')

        with open('/outcomes_by_animal_type.png', 'rb') as f:
            img = f.read()

        rd.hset(f'job.{jid}', 'result', img)

        jobs.update_job_status(jid, 'complete')

    #analysis: plot total # of outcomes by type of animal in date range
    if (job_type == 'animal_type'):

        #jobs.update_job_status(jid, 'it has entered the for loop')

        animal_types = ['Bird', 'Cat', 'Dog', 'Livestock', 'Other']
        animal_counts = [0, 0, 0, 0, 0]

        for key in rd1.keys():

            #jobs.update_job_status(jid, str(key))#'it has entered the for loop')

            this_animal_type = str(rd1.hget(key, 'Animal_Type'))[1:]

            #jobs.update_job_status(jid, str(this_animal_type))

            if this_animal_type == "'Bird'":
                animal_counts[0] += 1
            elif this_animal_type == "'Cat'":
                animal_counts[1] += 1
            elif this_animal_type == "'Dog'":
                animal_counts[2] += 1
            elif this_animal_type == "'Livestock'":
                animal_counts[3] += 1
            elif this_animal_type == "'Other'":
                animal_counts[4] += 1

        #jobs.update_job_status(jid, str(animal_counts))

        plt.clf()
        plt.bar(animal_types, animal_counts, color='green')
        plt.xlabel('Animal Type')
        plt.ylabel('Frequency')
        plt.title('Outcomes by Animal Type')
       
        plt.savefig('/outcomes_by_animal_type.png')

        with open('/outcomes_by_animal_type.png', 'rb') as f:
            img = f.read()

        rd.hset(f'job.{jid}', 'result', img)
             
        jobs.update_job_status(jid, 'complete')

#https://isp-proxy.tacc.utexas.edu/zcw268/download/job.<jid>

execute_job()
