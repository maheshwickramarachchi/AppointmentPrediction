import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Medical_No_Shows.csv',index_col=None, header=0,delim_whitespace=False,delimiter='\s+|\t+|,',engine='python',usecols=['PatientID','AppointmentID','Gender','ScheduledDay','AppointmentDay','Age','LocationID','MedicaidIND','Hypertension','Diabetes','Alcoholism','Disability','SMS_received','No-show'])

print(data.loc[data['No-show'] == 'Yes'].head())


