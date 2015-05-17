#!/usr/bin/python

import sys
from collections import defaultdict
import pandas as pd

infile="hes_apc_national_procedure_2013_14.csv"

df = pd.read_csv(infile)

data = defaultdict(list)
header = defaultdict(list)

for i, row in enumerate(df.values):
        date = df.index[i]
        Year,Summary_Name,DimensionCode,DimensionDescription,ActivityType,\
                AggregationType,MeasureCategory,MeasureSubCategory,MeasureValue,Suppressed,GenderDQ = row
    
        if len(DimensionCode) != 2:
            continue

        DimensionDescription = DimensionDescription.replace(",","")
    
        h = "_".join([ActivityType,AggregationType,MeasureCategory,MeasureSubCategory])
        header[DimensionDescription].append(h)

        data[DimensionDescription].append(MeasureValue)

done = False
for k in header:
    if done:
        continue
    v = ','.join(header[k])
    print v
    done=True

for k in data:
    v = ",".join(data[k])
    print k,",",v

#print "Collected ",len(data.keys())

