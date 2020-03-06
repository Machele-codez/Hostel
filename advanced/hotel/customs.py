# -*- coding: utf-8 -*-
"""
So the model consists of a number of rooms
we want to view all the rooms in a well arranged manner such as a bootstrap4 striped table
this table should have six columns 
the number of rows is determined by the number of rooms 
  So if there are 50 rooms then number of rows should be:
    50/6 = 8.2 -> 9 rows

we want a script that;
   will create a table and put in all of the rooms from our database
   each group_name of the table should have 6 rooms except the last one which may have less


PSEUDO CODE
get number of rooms
create subsets of 6 from the rooms
    dictionary to hold groups
        keys as group names and values as rooms in group
    
for each subset create a group_name    


"""
from hotel.models import Room

def create_groupings(per_row):
    # todo: changing all rooms queryset to list
    rooms = [] #list of all rooms
    for room in Room.objects.all().order_by('pk'):
        rooms.append(room)
        
    # todo: determining number of rows    
    total = len(rooms) # number of rooms
    groups = {} # dictionary of groups to hold rooms as values
    # determining number of groups
    #?per_row -> number of rooms per row
    if total%per_row != 0: 
        row_count = total//per_row + 1
    elif total%per_row == 0:
        row_count = total//per_row
        
    #todo: creating empty room-holder keys in dictionary
    #* group_name -> each name of groups holding rooms
    for group_name in range(1,row_count+1):
        groups[group_name] = []

    #todo: populating dictionary with rooms
    for group_name in range(1, row_count+1):
        if group_name == row_count:    #? when iteration has reached last group_name 
            for room in rooms:
                groups[group_name].append(room)
        else:                          #? iteration for all other rooms
            #? while group_name is not filled up to limit number of rooms
            while len(groups[group_name]) < per_row: 
                groups[group_name].append(rooms[0])
                rooms.remove(rooms[0])    
    return groups
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
