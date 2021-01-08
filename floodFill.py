import pandas as pd
import numpy as np
import itertools

lookuplist = []
def floodFill(sourceDf, _groupNonZeros=False):

    regionNumber=1
    outputDf = np.zeros(shape=(len(sourceDf), len(sourceDf[0])))
    for col, row in itertools.product(range(len(sourceDf)), range(len(sourceDf[0]))):
        if (sourceDf[col, row]>0 and outputDf[col, row]==0):
            lookuplist.append((col, row))
            while lookuplist:
                (lulCol, lulRow)= lookuplist.pop()
                regionBuilder(sourceDf, outputDf, lulCol, lulRow, regionNumber, _groupNonZeros)
            regionNumber=regionNumber+1
    print(sourceDf)
    print(outputDf)
    return outputDf

def regionBuilder(sourceDf, outputDf, col, row, regionNumber, _groupNonZeros):
        value=sourceDf[col, row]
        maxCol = len(sourceDf)    -1
        maxRow = len(sourceDf[0]) -1
        if (col>0):
            if ((sourceDf[col-1,row]==value or (sourceDf[col-1,row]>0 and _groupNonZeros)) and outputDf[col-1, row]==0):
                lookuplist.append((col-1, row))
        if (row>0):
            if ((sourceDf[col,row-1]==value  or (sourceDf[col,row-1]>0 and _groupNonZeros)) and outputDf[col, row-1]==0):
                lookuplist.append((col, row-1))
        if (col<maxCol):
            if ((sourceDf[col+1,row]==value  or (sourceDf[col+1,row]>0 and _groupNonZeros)) and outputDf[col+1, row]==0):
                lookuplist.append((col+1, row))
        if (row<maxRow):
            if ((sourceDf[col,row+1]==value  or (sourceDf[col,row+1]>0 and _groupNonZeros)) and outputDf[col, row+1]==0):
                lookuplist.append((col, row+1))
        
        outputDf[col, row]=regionNumber

