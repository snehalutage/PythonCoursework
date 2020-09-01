#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 6                       #
# Due Date       : 03/24/2020              #
############################################

#############################################################################################
# File        : prog6.py                                                                    #
# Usage       : prog6.py                                                                    #
# Description : This program is to implement the simulation a typical grocery store by      #
#               generating clock events using random number generator                       #
# Inputs      : NA                                                                          #
# Module      : Inbuilt - random , to get the random number from provided range             #
#               User defined - header6 - decalred the below constant values used in program #
#               SEED,SIMTIME,MIN_INT_ARR,MAX_INT_ARR,MIN_PICK,MAX_PICK,MIN_SERV,MAX_SERV    #             
#############################################################################################
from random import seed, randrange
from header6 import *

############################################################
# Function Name   : rng                                    #
# Description     : To generate and return random numbers  #
#                   within the specified range(low,high)   #
# Input           : low, high - Range for numbers          #
############################################################
def rng(low,high):
    return randrange(low,high+1)

############################################################
# Function Name   : update_clock                           #
# Description     : To find the minimum value from the     #
#                   events and return respective valueevent#
# Input           : next_arr,next_pick,next_dept           #
#                   - arrival, pickup and departure times  #
############################################################
def update_clock(next_arr,next_pick,next_dept):
    #Depending on the times of next_arr,next_pick,next_dept, find minimum and return
    #that events value to main()
    if next_pick == None and next_dept == None:
        return next_arr
    elif next_pick == None:
        return min(next_arr,next_dept)
    elif next_dept == None:
        return min(next_arr,next_pick)
    elif (next_arr == next_pick):
        return min(next_arr,next_dept)
    elif (next_arr == next_dept):
        return min(next_arr,next_pick)
    elif (next_pick == next_dept):
        return min(next_arr,next_pick)
    elif (next_arr == next_pick == next_dept):
        return next_arr
    else:
        return min(next_arr,next_pick,next_dept)

############################################################
# Function Name   : Arrival                                #
# Description     : Function called when a new customer    #
#                   arrives to the store. Returns the next #
#                   customers arrival time and the next    #
#                   minimum pickup value                   #
# Input           : clock - Simulation clock               #
#                   picking - List of customer dictioneries#
############################################################
def Arrival(clock,picking):
    #Generate random numbers for calculting next arrival time and current customer picking time
    arr=rng(MIN_INT_ARR,MAX_INT_ARR)
    pick=rng(MIN_PICK,MAX_PICK)
    next_arr=arr+clock
    ptime=pick+clock
    #Create a dictionary for the current customer with the keys - atime,ptime,wtime and dtime
    cust={'atime':clock,'ptime':ptime,'wtime':None,'dtime':None}
    #Append the customer dictinory to picking list
    picking.append(cust)
    #Get the minimum picking time from the picking list
    picktime=min([t['ptime'] for t in picking])
    return (next_arr,picktime)

############################################################
# Function Name   : Shopping                               #
# Description     : Function called when picking grocery is#
#                   done and ready to checkout, returns the#
#                   the updated status of picking and      #
#                   checkout lists                         #
# Input           : clock - Simulation clock time          #
#                   picking,checkout - lists               #
############################################################
def Shopping(clock,picking,checkout):
    #Remove the minimum picking time customer dictionary from the picking list
    picktime=min([t['ptime'] for t in picking])
    ind=[picking.index(t) for t in picking if t['ptime'] == picktime ]
    to_checkout=picking.pop(ind[0])
    #If the checkout list is empty add the departure time and the wait time for the
    #first customer
    if len(checkout) == 0:
        #Generate the random number to get the departing time
        next_depart=rng(MIN_SERV,MAX_SERV)
        dtime=clock+next_depart
        wtime=0
        to_checkout['dtime']=dtime
        to_checkout['wtime']=wtime
    #Add the customer to the checkout list
    checkout.append(to_checkout)
    return picking,checkout

############################################################
# Function Name   : print_stat                             #
# Description     : Prints the overall statistics          #
# Input           : total - Dictionary with the accumulativ#
#                   times                                  #
############################################################
def print_stat(total):
    print("Num of customers shopped  = {:,}".format(total['num']))
    print("Avg grocery pick time     =  {:>.3f}".format(total['pick']/total['num']))
    print("Avg wait time in checkout =  {:>.3f}".format(total['wait']/total['num']))
    print("Avg serv time in checkout =  {:>.3f}".format(total['serv']/total['num']))
    print("Avg time in store         =  {:>.3f}".format(total['shop']/total['num']))

############################################################
# Function Name   : update_stat                            #
# Description     : To update the total dictionary with the#
#                   time difference for pick,serv,num,wait #
#                   and shop times                         #
# Input           : cust - Customer dictionary who is      #
#                   departing                              #
#                   total - total stats dictionary         #
############################################################
def update_stat(cust,total):
    #Get the respective customers time values and add the respective values to total dictionary
    total['num']=total.get('num')+1
    total['pick']=total.get('pick')+(cust['ptime']-cust['atime'])
    if cust['wtime'] != 0:
        total['wait']=total.get('wait')+(cust['wtime']-cust['ptime'])
        total['serv']=total.get('serv')+(cust['dtime']-cust['wtime'])
    else:
        total['wait']=total.get('wait')+cust['wtime']
        total['serv']=total.get('serv')+(cust['dtime']-cust['ptime'])
    total['shop']=total.get('shop')+(cust['dtime']-cust['atime'])

############################################################
# Function Name   : Departing                              #
# Description     : Function called when customer departs  #
#                   from the store. Calls the update_stat &#
#                   returns the next departure value       #
# Input           : clock - Simulation clock time          #
#                   checkout - list of customers dict      #
#                   total - dict of total stats            #
############################################################
def Departing(clock,checkout,total):
    #Remove the first customer from the checkout list
    #Call update_stats to update the total stats
    cust=checkout.pop(0)
    update_stat(cust,total)
    #Update the wtime and dtime for the next customer in queue
    if len(checkout) != 0:
        checkout[0]['wtime']=clock
        num=rng(MIN_SERV,MAX_SERV)
        checkout[0]['dtime']=clock+num
        next_depart=checkout[0]['dtime']
        return next_depart
    else:
        return None

#main() function definition
def main():
    #To initialise the RNG
    seed(SEED)

    #Initialise the events and the picking,checkout lists, total stats dictionary
    #N=0 for printing only the values till number of customers departed is 10
    clock=0
    next_arr=0
    next_pick=None
    next_serv=None
    next_dept=None
    N=0
    picking=[]
    checkout=[]
    total={'num':0,'pick':0,'wait':0,'serv':0,'shop':0}
    print("")

    #Execute till the simulation time SIMTIME=30*24*60
    while clock <= SIMTIME:
        #Check the events and call the respective event function
        if clock == next_arr:
            if N < 10:
                print("Arriving to Store:   ",clock)
            next_arr,next_pick=Arrival(clock,picking)
        elif clock == next_pick:
            prev_len=len(picking)
            if N<10:
                print("Picking Grocery Done:",clock)
            picking,checkout=Shopping(clock,picking,checkout)
            if len(picking) == 0:
                next_pick =None
            elif len(picking) != prev_len:
                next_pick=min([t['ptime'] for t in picking])
            if len(checkout) == 1:
                next_dept=checkout[0]['dtime']
        elif clock == next_dept:
            if N<10:
                print("Departing from Store:",clock,"\n")
            next_dept=Departing(clock,checkout,total)
            N+=1
        #Update the clock to get the next event
        clock=update_clock(next_arr,next_pick,next_dept)

    #Print the total statistics for the simulation
    print_stat(total)

#Call to main() function
main()
