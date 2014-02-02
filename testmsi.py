import os
# output_file1,a,b,c,d
# output_file2,d,e,f,g

for line in open("input.txt").readlines():
  print "Read Line: %s" % (line)
#  line=line.strip()
#  output_file,value1,value2,value3,value4=line.split(',')

# os.system('msi-MVAR=%s<template.txt>%s'%(value1,))

