# The purpose is to create files in a directory 
# with a defined frequence. 
# the title of the will be log+currentdate 
# Python version is 3.

import time
import os
import csv 


from datetime import date


def create_file_name():
	return 'LogFiles-'+str(date.today())

#def record_data_into_csv():
#	file = /Data/temp_log.csv 

def read_data_into_csv():
	with open('temp_log.csv','r') as f:
		reader = csv.reader(f,delimiter=';')
		for row in reader:
			print(row)

def input_is_valid(input):

	validation = false 
	return validation

def write_data_into_csv(input):
	with open('temp_log.csv','a') as f:
		writer = csv.writer(f,delimiter=';')
		for row in writer:
			writer.writerow(input[0],input[1],input[2])


def main():
	input = ['2017-02-06-16:30','27','85']
	write_data_into_csv(input)
	read_data_into_csv()

main()

