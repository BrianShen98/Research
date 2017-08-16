# Selective Naive Bayes Classifier with feature selection process(wrapper approach)

## Introduction

An implementation of Gaussian Naive Bayes classifier with a wrapper approach feature selection process proposed by Marc Boulle 
in the paper "compression-based averaging of selective Naive Bayes Classifier" 


## Methods


Methods   | Description
-----------|----------------------------------------------
train(X,Y) | select feature subsets using MS(FFWBW) algorithm and fit Gaussian Naive Bayes classifier according to X,Y
predict(X) | Perform classification on an array of test vector X
predict_proba(X) | Return probability estimates for the test vector X.
predict_log_proba(X) | Return log-probability estimates for the test vector X.
score(X,Y) | Returns the mean accuracy on the given test data and labels.



## Notice

Currently, I did not implement the discretization process to discretize the data, but use Gaussian Bayesian Classifier in sklearn module to process the data. The accuracy on the cloth-folding dataset using 5-fold cross validation is 85%. I think there is still space to
further improve it and that's what I am gonna do in the following few days. I will do it ASAP



# VEIL Dataset

## Content

1. A formatted VEIL dataset
2. all the programs wrote to format the dataset
3. The final dataset is in "finalVersion" directory, which is obtained from the programs and files in "progRefined" directory.
   "progRefined" made some changes on "progRefinedCopy", which is the backup for the original "progRefined" directory.  


## Things Accomplished

1. Replace propositions that start with (state ...) with two-object proposition e.g. (state Cup1 water)  ->  (Cup1 HasWater)

2. Edit verb clause to present more precise division and relation along with args mapping

3. Format the verb clause to be a more formal structure:

  Obj1:
  Obj2:
  Obj3:
  ...
  Verb:
  Rel12:
  Rel13:
  Rel23:


4. Modified some environment changes to make them more accurate(a copy of original mapping is also posted in the repo)

