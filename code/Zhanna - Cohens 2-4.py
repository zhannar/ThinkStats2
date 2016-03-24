# -*- coding: utf-8 -*-
"""
[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

*"Exercise 4   Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?"*

#### A. Communicate the problem: 
This problem wants to answer whether the weight of the baby is effected by whether it was first or not (i.e. if it is generally lighter or heavier). 

#### B. How you solved it: 

I solved this problem by looking at the two distributions and calculating Cohen's distances.

#### C. Solution 


"""

##### Step 1: Import the required datasets.
import nsfg
import thinkstats2
import math

##### Step 2: Clean and extract the time series of interest.

#Extract out all pregrenency records.
preg = nsfg.ReadFemPreg()

#Focus on thos pregrencies which led to live births.
live = preg[preg.outcome == 1]

#Separate all live births into those which are first borns and those which aren't.

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

##### Step 3: Defining *Cohen's Distance Function*.
 

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    print d
    return d

##### Step 4: Run and view your results.

"""
# Create and run the histograms:
first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
other_hist = thinkstats2.Hist(others.totalwgt_lb)

width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
thinkplot.Show(xlabel='weeks', ylabel='frequency')
"""

# Running Cohen's D:
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

##### Step 5: Analyze the results