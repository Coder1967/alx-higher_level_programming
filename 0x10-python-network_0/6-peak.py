#!/usr/bin/python3
""" finds the peak from a list of numbers"""
def find_peak(list_of_integers):
	i = 0
	length = len(list_of_integers)
	while i < length:
		if i >0 and i < length - 1:
			if list_of_integers[i] >= list_of_integers[i-1]:
				if list_of_integers[i] >= list_of_integers[i + 1]:
					return list_of_integers[i]
		i += 1
