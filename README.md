# Selective Naive Bayes Classifier with feature selection process(wrapper approach)

## Introduction

An implementation of Gaussian Naive Bayes classifier with a wrapper approach feature selection process proposed by Marc Boulle 
in the paper "compression-based averaging of selective Naive Bayes Classifier" 


## Methods


Methods   | Description
-----------|----------------------------------------------
train(X,Y) | select feature subsets using [MS(FFWBW)](#multi-start-fast-forward-backward-selection) algorithm and fit Gaussian Naive Bayes classifier according to X,Y
predict(X) | Perform classification on an array of test vector X
predict_proba(X) | Return probability estimates for the test vector X.
predict_log_proba(X) | Return log-probability estimates for the test vector X.
score(X,Y) | Returns the mean accuracy on the given test data and labels.


## Multi-start fast forward backward selection
>**Require:** X<-(X<sub>1</sub>,X,<sub>2</sub>,...,X<sub>k</sub>) {Set of input variables}  
>**Ensure:** B {Best subset of variables}  

>B <- ∅ {Start with an empty subset of variables}  
>**for** Step = 1 to log<sub>2</sub><sup>KN</sup> **do**  
>>{Fast forward backward selection}  
>>S <- ∅ {Initialize an empty subset of variables}  
>>Iter <- 0  
>>**repeat**  
>>>Iter <- Iter + 1  
>>>X' <- Shuffle(X){Randomly reorder the variables to add}  
        
>>>{Fast forward selection}  
>>>**for** X<sub>k</sub> ∈ X' **do**  
>>>>**if** cost(S ∪ {X<sub>k</sub>}) < cost(S) **then**  
>>>>>S <- S ∪ {X<sub>k</sub>}  
>>>>**end if**  
>>>**end for**  
>>>X' <- Shuffle(X) {Randomly reorder the variables to remove}  
      
>>>{Fast backward selection}  
>>>**for** X<sub>k</sub> ∈ X' **do**  
>>>>**if** cost(S - X<sub>k</sub>) < cost(S) **then**  
>>>>>S <- S - {X<sub>k</sub>}  
>>>>**end if**  
>>>**end for**  
>>**until** no improvement or Iter > MaxIter  
>>{Update best subset of variables}  
>>**if** cost(S) < cost(B) **then**  
>>>B <- S  
>>**end if**  
>**end for**  
      
## Notice

Currently, I did not implement the discretization process to discretize the data, but use Gaussian Bayesian Classifier  
in sklearn module to process the data. The accuracy on the cloth-folding dataset using 5-fold cross validation is 85%.  
I think there is still space to further improve it and that's what I am gonna do in the following few days. I will do it ASAP  



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

