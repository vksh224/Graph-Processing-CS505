# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:15:28 2018

@author: Sajjad Fouladvand
"""
import os
import pdb

records=[]
fn=os.path.join(os.path.dirname(__file__), 'dataset.txt')
#pdb.set_trace()
with open(fn) as record_email:  
    for line in record_email:
        line_record=line.split()
        line_drug = [records.append(i) for i in line_record]

unique_names=set(records)

codes=0

index_file=os.path.join(os.path.dirname(__file__), 'people_to_code.txt')
people_dictunary={}
with open(index_file, 'w') as f_index_file:
    for i in range(len(unique_names)):
        people_temp=str(unique_names.pop())
        f_index_file.write(people_temp)
        f_index_file.write(",")
        f_index_file.write(str(i))
        f_index_file.write("\n")
        people_dictunary[people_temp]=i

emails=[]        
fn=os.path.join(os.path.dirname(__file__), 'dataset.txt')
#pdb.set_trace()
with open(fn) as record_email:  
    for line in record_email:
        line_record=line.split()
        #pdb.set_trace()
        line_record_coded=[people_dictunary[i] for i in line_record]
        emails.append(line_record_coded)
#for i in range(len(emails)):
coded_file=os.path.join(os.path.dirname(__file__), 'dataset_coded.txt')
with open(coded_file, 'w') as f_coded_file:
    for i in range(len(emails)):
        f_coded_file.write(' '.join(map(repr, emails[i])))
        f_coded_file.write("\n")
#pdb.set_trace()