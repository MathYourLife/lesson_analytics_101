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
1. What happens after the analysis? (Repeatable?, destined for "real-time" monitoring?, ...)

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

Your boss has just provided you with the following data set (columns A and B of sample data set) with the direction to determine a model of given A, predict B.

Data used here was created with function of the form
$B = \left(m * A + b \right) + \left(c * e^{A/k} \right) + w$
where
$w ~ N(0, 1)$

**Pass 1 - Rough modeling**

With a extremely limited quantity of time, create a reasonable model of the system.

1. Students spend ~5 min investigating data from columns A and B
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
1. Allow students another ~5-10 min to revisit their model.
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

**Pass 1 - Investigate the data**

6 Sigma - Control Charts Checks

CL = x_bar
UCL = CL + 3 sigma
LCL = CL - 3 sigma

* If 1 point > 3 sigma

TODO: expand this section

Concepts:

* Process control
* Statistical significance
* Steady vs diurnal

****

### Unsupervised Clustering

Problem:

Data sets may sometimes contain multiple subgroups.  Under these conditions two approaches are generally taken.

1. User predefines groups based on current knowledge of the system and allocates data points to the groups.
1. User defines a method for grouping, and the groups are generated to best conform to the rules.

TODO: expand this section

Concepts:

* Unsupervised learning
* KMeans clustering (concept and algorithm)
* Principle Component Analysis
* Model Assessment


