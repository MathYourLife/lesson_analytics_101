# Analytics 101

A introduction to exploring a simple data set.

## Key Concepts

* Analytics is a widely used term.
* Are there differences to analytical techniques when working on small or x-large data sets?
* Explore a small subset of techniques for investigating a series of small data sets with varied underlying structures

## Goals

At the end of the lesson, students should be able to answer the following questions and/or

1. What is analytics?
1. Understand the math behind the methods.
1. Is the analysis repeatable? (by someone else)
1. Are there limitations to the model's use?

## Lesson Plan

### Intro

**Rough assessment of math literacy**

Starting at 3 go around the room adding 7.

**Intro**

1. What is analytics?
    * Establish a baseline for this question to follow up at the end of class
1. What types of data are there?
1. What experiences do students have with analyzing data?
1. Discuss calculations such as mean, median and discuss if special considerations would need to be made once the data is too large for a single machine.



****

### Linearized Models

Problem:

Your boss presents you with something that you determine is a data set which calls for the predication of column B based on column A.

Questions to pose:

* Is there a time/sequence dependency?
* Is there a simple model that can reasonably predict column B given column A?
* For a random point A, how close does your model get to the point B?
* Is there a limitation to the input or your model?
* Could the model be improved?
* What could be added to the model to improve it's accuracy?
* Why are linearized models more prevalent?


Data used here was created with function of the form
$B = \left(m * A + b \right) + \left(c * e^{A/k} \right) + w$
where
$w ~ N(0, 1)$

**Pass 1 - Rough modeling**

With a extremely limited quantity of time, create a reasonable model of the system.

1. Students spend ~5-10 min investigating data from columns A and B
1. Little to no information is provided about the source or underlying structure.
1. Circulate through the groups and

**Discussion of Preliminary Findings**

1. Group discussion on findings
1. Possible Models
    * Simple arithmetic mean (geometric mean?)
    * Piecewise mean
    * Linear model
    * Nearest answer (Decision Tree)
1. Demonstration of data_hacks command line utils as a first pass

```bash
# Histogram of column A
cat data.csv | cut -d ',' -f 1 | sort -n | histogram -b 15
# Histogram of column B
cat data.csv | cut -d ',' -f 2 | sort -n | histogram -b 15
```

Characteristics of column A

* Fairly uniform distribution for x > 0
* Spacing between steps is ~ uniform with mean ~= 1

Characteristics of column B

* Mostly uniform for values x < 25
* Lower density when values x > 25

Combined model

$B = \left(-0.5 * A + 42 \right) + \left(c * e^{A/-10} \right) + w$

**Pass 2 - Model Refinement**

With additional insight, can you upgrade your current model to provide a more accurate prediction?

1. If groups have a variety of models, ask them to try to incorporate another groups approach.
1. Allow students another ~10-15 min to revisit their model.
1. Regroup
    * Discuss additions to models
    * Provide validation points
    * Discussion Questions
        * How do you determine how good your model is?
        * How do you measure the model error?
        * Model limitations (linearized systems)

****

### Gaussian Distributions

Problem:

Given steady time series data in column C, can you determine if the process is functioning properly?

Questions to pose:

* What does the data look like?
* Would you consider the process to be "in control"?
* What rules could you use to detect if a process is out of control?
* Would you consider the variablity to be normally distributed? (∼N(μ,σ2))
* How can you determine how close to normally distributed it is
* What does normally distributed data look like?

**Pass 1 - Investigate the data**

6 Sigma - Control Charts Checks

CL = x_bar
UCL = CL + 3 sigma
LCL = CL - 3 sigma

```
cat data.csv | cut -d ',' -f 3 | histogram
cat data.csv | cut -d ',' -f 3 | python3 control_chart.py -m -2.964333 -s 0.563121
```

**Control Tests**

* [x] is < 3 sigma
* [x] is > 3 sigma
* [..] is 2/3 points > 2 sigma
* [..] is 2/3 points < 2 sigma
* [..] is 4/5 points > 1 sigma
* [..] is 4/5 points < 1 sigma
* [..] is 8/8 points > centerline
* [..] is 8/8 points < centerline

**Centerline Shift Tests**

* [..] is 10/11 points > centerline
* [..] is 10/11 points < centerline
* [..] is 12/14 points > centerline
* [..] is 12/14 points < centerline
* [..] is 14/17 points > centerline
* [..] is 14/17 points < centerline
* [..] is 16/20 points > centerline
* [..] is 16/20 points < centerline

**See IPython notebook for details on this section**

****

### Unsupervised Clustering

Problem:

Data sets may sometimes contain multiple subgroups.  Under these conditions two approaches are generally taken.

1. User predefines groups based on current knowledge of the system and allocates data points to the groups.
1. User defines a method for grouping, and the groups are generated to best conform to the rules.

Questions to pose:

* Are there subgroups to the data?
* How confident are you in you conclusion?
* If so how many subgroups do you think?
* How would you quantify the difference between subgroups?
* Do all data points in the sample conform to the group separation?
* To the group separations for each column agree?
* Do subgroups according to column 4 agree with column groupings for 5 and 6?
* Can all the data be represented in a single chart?
* Can we choose an objective method of creating the clusters?
* Can the algorithm find additional subgroups?
* Why does K-Means clustering group along a major axis?
* Is there something we can do to improve the algorithm's ability to find subgroups?
* How can we represent an n-dimensional data in less than an n dimensional space?
* What methods can we use to reduce the complexity of the data?
* What are the advantages and/or disadvantages to using dimensionality reduction?
* How could you quantify any loss of fidelity?

**Concepts**

* Unsupervised learning
* KMeans clustering (concept and algorithm)
* Principle Component Analysis
* Model Assessment

**See IPython notebook for details on this section**
