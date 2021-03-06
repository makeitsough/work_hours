#!usr/bin/env python3

# To run this program:
# $ python3 workhours2.py

import datetime as dt
from datetime import timedelta
import numpy as np
import unittest
import pandas as pd
import pdb

clock_in_time = dt.datetime(1, 1, 1, 10)
clock_out_time = dt.datetime(1, 1, 1, 18)

seconds_per_hour = 3600
hours_per_day = 8

# The "algorithm" is:
# - Find the number of hours on the start day
# - Find the number of hours on the end day
# - Find the number of hours in between those days
# - Add all three.

# Input cases to cover:
# Case 1: There is at least one whole day between start and end.
# Example: Start on Monday, and end on Wednesday.
# 
# Case 2: The start and end days are the same.
# Example: Start and end are both on Monday (the same day).
#
# Case 3: The start and end days are "adjacent".
# Example: start on Monday and end the next day (Tuesday); OR
# start on Friday, and end the following Monday

def dt_median(original_dt):
	dt_mod = dt.datetime(1, 1, 1, original_dt.hour)
	if dt_mod <= clock_in_time:
		return clock_in_time
	if dt_mod >= clock_out_time:
		return clock_out_time
	return dt.datetime(1, 1, 1, original_dt.hour)

#Converts bus_count into timedelta object 
def time_between_days(start, end): 
	#start = (dt.strptime(start))
	#end = (dt.strptime(end))
	day_count = np.busday_count(start, end)
	day_count = int(day_count)
	day_count = max(0, day_count - 1)
	second_count = day_count * seconds_per_hour * hours_per_day
	second_count_dt = timedelta(seconds = second_count)
	return second_count_dt

def start_d_hours(dt_in, dt_out):
	in_time = dt.datetime(1, 1, 1, dt_in.hour)
	out_time = dt.datetime(1, 1, 1, dt_out.hour)
	in_biz = dt_median(in_time)
	out_biz = dt_median(out_time)
	if out_biz >= in_biz:
		start_day_hours = out_biz - in_biz
		return start_day_hours
	if out_biz < in_biz:
 		return dt.timedelta(0)

def end_d_hours(dt_in, dt_out):
	in_time = dt.datetime(1, 1, 1, dt_in.hour)
	out_time = dt.datetime(1, 1, 1, dt_out.hour)
	in_biz = dt_median(in_time)
	out_biz = dt_median(out_time)
	if out_biz >= in_biz:
		end_day_hours = out_biz - in_biz
		return end_day_hours
	if out_biz < in_biz:
 		return dt.timedelta(0)

def work_hours(start, end):
	s_d_h = start_d_hours(start, end)
	e_d_h = end_d_hours(start, end)
	h_b_d = time_between_days(start, end)
	return s_d_h + e_d_h + h_b_d

class TestWorkHours(unittest.TestCase):
	def test_start_m10_m16(self):
		s = dt.datetime(2022, 7, 11, 10)
		e = dt.datetime(2022, 7, 11, 16)
		self.assertEqual(dt.timedelta(seconds=21600), work_hours(s, e), "Should be dt.timedelta(seconds=21600)")

# When writing in a function. Is test class the best way to test,
# or should I test it outside of the function and then compose the function after? 

# class TestEndHours(unittest.TestCase):
# 	#i, o = in and out
# 	#p, m, a = prior, middle, and after with respect to the working hour range
# 	def test_ip_op(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be datetime.timedelta(0)") 

# 	def test_ip_om(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(seconds=7200), end_d_hours(i, o), "Should be datetime.timedelta(seconds=7200)") 

# 	def test_io_oa(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(seconds=28800), end_d_hours(i, o), "Should be datetime.timedelta(seconds=28800)") 

# 	def test_im_op(self): # 
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_im_om(self):
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be datetime.timedelta(0)") 

# 	def test_im_oa(self): 
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(seconds=21600), end_d_hours(i, o), "Should be datetime.timedelta(seconds=21600)") 

# 	def test_ia_op(self): #
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_ia_om(self): # 
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_ia_oa(self):
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(0), end_d_hours(i, o), "Should be datetime.timedelta(0)") 

# class TestStartHours(unittest.TestCase):
# 	#i, o = in and out
# 	#p, m, a = prior, middle, and after with respect to the working hour range
# 	def test_ip_op(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be datetime.timedelta(0)") 

# 	def test_ip_om(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(seconds=7200), start_d_hours(i, o), "Should be datetime.timedelta(seconds=7200)") 

# 	def test_io_oa(self):
# 		i = dt.datetime(1, 1, 1, 1)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(seconds=28800), start_d_hours(i, o), "Should be datetime.timedelta(seconds=28800)") 

# 	def test_im_op(self): # 
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_im_om(self):
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be datetime.timedelta(0)") 

# 	def test_im_oa(self): 
# 		i = dt.datetime(1, 1, 1, 12)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(seconds=21600), start_d_hours(i, o), "Should be datetime.timedelta(seconds=21600)") 

# 	def test_ia_op(self): #
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_ia_om(self): # 
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be dt.timedelta(0)") 

# 	def test_ia_oa(self):
# 		i = dt.datetime(1, 1, 1, 20)
# 		o = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.timedelta(0), start_d_hours(i, o), "Should be datetime.timedelta(0)") 


# class TestMedianAlg(unittest.TestCase):
	
# 	def test_in(self): #TODO lookup self 
# 		# Event_time is hour 1
# 		event = dt.datetime(1, 1, 1, 1)
# 		self.assertEqual(dt.datetime(1, 1, 1, 10), dt_median(event), "Should be 01/01/01 10:00")

# 	def test_event(self): #TODO lookup self 
# 		# Event_time is hour 1
# 		event = dt.datetime(1, 1, 1, 12)
# 		self.assertEqual(dt.datetime(1, 1, 1, 12), dt_median(event), "Should be 01/01/01 12:00")

# 	def test__end(self): #TODO lookup self 
# 		# Event_time is hour 1
# 		event = dt.datetime(1, 1, 1, 20)
# 		self.assertEqual(dt.datetime(1, 1, 1, 18), dt_median(event), "Should be 01/01/01 20:00")


# class TestWorkDays(unittest.TestCase):

# 	# TODO: In one test case, loop over an entire month
# 	def test_start_m_end_m(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 11)
# 		self.assertEqual(0, work_days(s, e), "Should be 0")

# 	def test_start_m_end_t(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 12)
# 		self.assertEqual(0, work_days(s, e), "Should be 0")

# 	def test_start_m_end_w(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 13)
# 		self.assertEqual(1, work_days(s, e), "Should be 1")

# 	def test_start_f_end_m(self):
# 		s = dt.date(2022, 7, 15)
# 		e = dt.date(2022, 7, 18)
# 		self.assertEqual(0, work_days(s, e), "Should be 0")


# class TestTimeBetweenDays(unittest.TestCase):
# 	def test_start_m_end_w(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 13)
# 		self.assertEqual(dt.timedelta(seconds=28800), time_between_days(s, e), "Should be dt.timedelta(seconds=28800)") 

# 	def test_start_m_end_t(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 12)
# 		self.assertEqual(dt.timedelta(seconds=0), time_between_days(s, e), "Should be dt.timedelta(seconds=0)")

# 	def test_start_m_end_m(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 11)
# 		self.assertEqual(dt.timedelta(seconds=0), time_between_days(s, e), "Should be dt.timedelta(seconds=0)")

# 	def test_start_f_end_m(self):
# 		s = dt.date(2022, 7, 15)
# 		e = dt.date(2022, 7, 18)
# 		self.assertEqual(dt.timedelta(seconds=0), time_between_days(s, e), "Should be dt.timedelta(seconds=0)")

# 	def test_start_m_end_f(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 15)
# 		self.assertEqual(dt.timedelta(seconds=86400), time_between_days(s, e), "Should be dt.timedelta(seconds=86400)") 

# 	def test_start_m_end_m(self):
# 		s = dt.date(2022, 7, 11)
# 		e = dt.date(2022, 7, 18)
# 		self.assertEqual(dt.timedelta(seconds=115200), time_between_days(s, e), "Should be dt.timedelta(seconds=115200)") 



if __name__ == '__main__':
	unittest.main()

#pdb.set_trace()

# Customer does a trade
# Amount that we calculate, that we owe the customer is 0.005000023 BTC
# Amount that we actually send to the customer, is      0.005 BTC
# Amount that we store in our system, is                0.000000023 BTC

# ItBit sends 5.432 USD to Coinbase 

# 1 BTC = 21,000 USD
# 1 USD = 0.000047 BTC
# ? USD = 0.00000001 BTC
