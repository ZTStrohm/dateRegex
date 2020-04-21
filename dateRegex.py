#=============================================================
#	dateRegex.py
# 	Z. Strohm
#	20 April 2020
#	Rev 0.01
# Contains several functions related to date regex searches
#=============================================================

import re

#	Name: dateSearch
#	Desc: Searches for dates with mm/dd/yyyy or dd/mm/yyyy format
#	Params: _searchString [str]: Text to search, mode [int]: Specifies date format
#	Returns: months [list], days [list], years [list]

def dateSearch(_searchString,mode = 0):
	# Gets search string and casts it to string type
	searchString = str(_searchString)

	# Creates date regex based on mode (MM/DD/YYYY for mode 1, or default)
	if(mode == 0):
		dateRegex = re.compile(r'([0-1][0-9])\/([0-3][0-9])\/(\d{4})')	# MM/DD/YYYY
	if(mode == 1):		
		dateRegex = re.compile(r'(([0-3][0-9])\/[0-1][0-9])\/(\d{4})')	# DD/MM/YYYY
	
	# Search input string for regex matches
	mo = dateRegex.findall(searchString)

	# Create lists to store months, days, and years.
	months = []
	days = []
	years = []

	# Read the results, and parse them to months, days, and years lists.
	for i in range(0,len(mo)):
		months.append(mo[i][0])
	for i in range(0,len(mo)):
		days.append(mo[i][1])
	for i in range(0,len(mo)):
		years.append(mo[i][2])

	# Return results
	return months,days,years
	
search = 'The date is 10/04/1945 or 06/04/1986 .'

M,D,Y = dateSearch(search,0)















