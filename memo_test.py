#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:01:57 2018

this is one excercise to learn python
rename of files and split with pdftk


@author: abocci
"""
#---- methods

#Lets define a method to remove leading and trailing space(s)
# this already exists, it is the strtip functions
def remove_space(ss, leading=1, trailing=1):
    print("dentro",ss[0])
    if leading: # remove the leading space
        while ss[0] == ' ': ss = ss[1:]
    print("dentro",ss[0])
        
    if trailing: # remove the trailing spaces
        print("dentro2",ss[:-1])
        while ss[-1] == ' ': ss = ss[:-1]
        print("dentro2",ss[-1])
    return ss

#--- 

#--- code


import os

file_a = open("data/Memo.audiolist.txt","r")
file_b = open("data/Memo.ebooklist.txt","r")
file_w = open("data/comm.sh","w")

print("Start...")

title_list = []
# now make a list with the tile of the lecture

for line in file_a:
    tt = line.split("-")
    print(tt)
    #remove the trailing space. Let's assume we don't know how many
#    for i in tt:
#        if i
    
#    title_list.append(remove_space(tt[1]))
    title_list.append(tt[1].strip())
#   break 

print(title_list)
#- Problem of duplication

#- this is the command to make a set (remove duplicate)
#- however I loose the order
#print(set(title_list))

#let's try with comprehension

#- Attempt 1: this does not work, since the new_list does not exist
#- and cannot be used to define itself
#new_list = [ ele for ele in title_list if ele not in new_list]

#- let's try to use the index of the original list as conditional
#- THIS WORKS!!!
new_list = [ title_list[i] for i in range(len(title_list)) if title_list[i] != title_list[i-1]]

print(len(new_list))
print(new_list)

L= file_b.readlines()

arr = [[17, 27, 43, 59, 75, 91, 107, 123, 139, 155, 171],
       [1, 17, 33, 49, 65, 81, 97, 113, 129],
       [1, 17, 33, 49, 65, 81, 97, 113, 129, 145],
       [3, 15, 31, 47, 63, 79, 95, 111, 127],
       [3, 15, 31, 47, 63, 79, 95, 111, 127],
       [3, 15, 31, 47, 63, 79, 95, 111, 127, 143, 159, 175]]

print(len(arr))
lez=0
#loop over the files, with index to match the array with page-breaks
for i,ff in enumerate(L):
    if i>len(arr)-1: break
    ff=ff.strip()
    line_breaks = arr[i]
    for j,pp in enumerate(line_breaks):
        #define line breaks syntax xx-yy
        pp_range = "{}-{}".format(pp,"end")
        if j<len(line_breaks)-1:
            pp_range = "{}-{}".format(pp,line_breaks[j+1])
        
        lez += 1 #starting from 1
#        print(i,j,lez)
        if lez>len(new_list): 
            print ("something wrong here",lez, len(new_list))
        else:
            comm = 'pdftk "{}" cat {} output "split/Lezione.{:02}.{}.pdf"\n'.format(ff,pp_range,lez,new_list[lez-1])
        print(comm)
        file_w.write(comm)


#array with the linebreaks





file_a.close()
file_b.close()
file_w.close()
