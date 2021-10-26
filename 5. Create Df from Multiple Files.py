import random
import datetime
import pandas as pd
import os
from glob import glob
from pandas_profiling import ProfileReport


randomtime = str(random.randint(1000,9999))
list_column_names = [
    'Name', 'Address', 'City', 'State',
    'Zip Code', 'Rural/Urban',
    'Hubzone', 'Labor Market Information',
    'Business Age Description', 'Jobs Reported',
    'NAICS', 'Business Type', 'Race',
    'Gender', 'Veteran', 'Unanswered', 'Loan Number',
    'Date Approved', 'Loan Status', 'Loan Status Date',
    'Term', 'Lender', 'Initial Approval Amount',
    'Current Approval Amount', 'Undisburse Amount',
    'Payroll Proceed']

print(datetime.datetime.now())
df = pd.concat((
    pd.read_csv(
        file,low_memory=False,
        names=['Name'])
    for file in glob('output/4/*.csv'))).drop_duplicates()
print(datetime.datetime.now())

if not os.path.exists('output/5/'): os.makedirs('output/5/')
df.to_csv('output/5/'+str(
    random.randint(1000,9999))+'_output.csv',index=True)


def prof(frame):
    print(datetime.datetime.now())
    print('Report Profiles:')
    frame = frame.sample(1000000)
    report_pandas = ProfileReport(frame)
    report_pandas.to_file('Visuals/Profile_'+randomtime+'.html')
    print(datetime.datetime.now())
    print()
##prof(df)    


# Build a Logistic Regression model
