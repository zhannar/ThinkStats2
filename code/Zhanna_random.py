# -*- coding: utf-8 -*-
"""

"""

##### Step 1: Import the required datasets.

import thinkplot
import thinkstats2
import chap01soln
resp = chap01soln.ReadFemResp()

##### Step 2: Construct the actual distribution of the number of children 
# under 18 in the household.


kids_hh = resp.numkdhh
actual_dist = thinkstats2.Pmf(kids_hh, label='actual')


##### Step 3: Construct the biased distribution if we sampled the children.

# Define function for converting from actual to biased/observed distribution
# (From book)

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


biased_dist = BiasPmf(actual_dist, label='observed')

##### Step 4: Plot the two distributions together

thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_dist, biased_dist])
thinkplot.Show()

##### Step 5: Calculate the means of the two distributions.

print actual_dist.Mean()
print biased_dist.Mean()

