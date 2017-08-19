#!/usr/bin/python

"""
An implementation of Gaussian Naive Bayes classifier with a wrapper
approach feature selection process proposed by Marc Boulle 
in the paper "compression-based averaging of selective Naive Bayes Classifier"

This program is a free software

"""

from sklearn.naive_bayes import GaussianNB
from scipy.special import comb
import numpy as np
import pandas as pd
import math

INIT_COST = 0

class SNBMAP:
    def __init__(self):
        
        #all the feature values
        self.fVals = None
        #all the class labels
        self.Y = None
        #num of features
        self.fNum = None
        #num of instances
        self.N = None
        #array of feature indexes for fast forward/backward selection
        self.fIndex = None
        self.bestSet = None
        self.NB = None

        
    def load(self,data,cls):
        self.fVals = pd.DataFrame.as_matrix(pd.read_csv(data,header=None))
        self.Y = np.ravel(pd.DataFrame.as_matrix(pd.read_csv(cls,header=None)))
        self.fNum = self.fVals.shape[1]
        self.N = self.fVals.shape[0]
        self.fIndex = np.arange(self.fNum)

    def train(self,data,cls,sample_weight = None):
        self.load(data,cls)
        upperBd = int(math.ceil(math.log(self.fNum * self.N,2)))
        print(upperBd)
        maxIter = 5
        bestSet = np.empty(0,dtype=int)
        Bcost = 0
        bestNB = None
        for i in range(1,upperBd):
            print("{} round\n".format(i))
            #S:the selected feature subsets, initially empty
            S = np.empty(0,dtype=int)
            Iter = 0
            Scost = INIT_COST
            varPool = self.fIndex
            prevScost = INIT_COST
            localBestNB = None
            
            while Iter < maxIter:
                #randomly reorder the variable to add
                np.random.shuffle(varPool)
                print(varPool)

                #fast forward
                result = self.fast_forward(S,varPool,Scost,localBestNB,sample_weight)
                S = result["S"]
                varPool = S
                Scost = result["Scost"]
                localBestNB = result["bestNB"]
                print("selected set:{}, Scost: {}".format(S,Scost))
                print("fast forward ends!\n")

                #fast backward
                np.random.shuffle(varPool)
                result = self.fast_backward(S,varPool,Scost,localBestNB,sample_weight)
                S = np.sort(result["S"])
                Scost = result["Scost"]
                localBestNB = result["bestNB"]
                print("selected set:{}, Scost: {}".format(S,Scost))
                print("fast backward ends!\n")

                #if no improvement, end the iteration
                if prevScost == 0:
                    prevScost = INIT_COST
                if prevScost <= Scost:
                    break
                
                prevScost = Scost
                varPool = np.setdiff1d(self.fIndex,S,assume_unique = True)
                Iter += 1

            if Bcost == 0:
                Bcost = INIT_COST
            if Scost < Bcost:
                bestSet = S
                Bcost = Scost
                bestNB = localBestNB
            print("Best set:{}, best cost: {}\n".format(bestSet,Bcost))
            
        self.bestSet = bestSet
        self.NB = bestNB
        print(self.bestSet)
    
    def fast_forward(self, S, varPool, Scost,bestNB,sample_weight):
        print("fast forward begins!")
        for each in varPool:
            clf = GaussianNB()
            #add one variable and compute the cost
            testSet = np.sort(np.append(S,each))
            print(testSet)
            testX = self.fVals[:,testSet]
            clf.fit(testX,self.Y,sample_weight)
            testCost = self.cost(clf,testX)

            #compute the cost for empty feature set
            global INIT_COST
            if INIT_COST == 0:
                modelLH = 0
                for i in range(self.N):
                    modelLH += math.log(clf.class_prior_[self.Y[i]])
                modelLH = -modelLH
                prior = math.log(self.fNum+1) + 1
                Scost = modelLH + prior
                INIT_COST = Scost
                print(INIT_COST)
                        
            #if cost is less, add the feature to current set
            if testCost < Scost:
                S = testSet
                Scost = testCost   
                bestNB = clf
            print(testCost)

        return {"S": S, "Scost": Scost,"bestNB":bestNB}

    def fast_backward(self,S,varPool,Scost,bestNB,sample_weight):        
        print("fast backward begins!")
        offset = 0
        for i in range(len(varPool)):
            #delete one from the current set
            clf = GaussianNB()
            testSet = np.sort(np.delete(S,i-offset))
            print (testSet)
            testX = self.fVals[:,testSet]
            clf.fit(testX,self.Y,sample_weight)
            testCost = self.cost(clf,testX)

            if testCost < Scost:
                S = testSet
                Scost = testCost
                offset += 1
                bestNB = clf
            print(testCost)
                
        return {"S":S, "Scost":Scost,"bestNB":bestNB}

    
    def cost(self,clf,testX):
        #the model likelihood
        modelLH = 0
        logProb = clf.predict_log_proba(testX)
        for i in range(self.N):
            modelLH += logProb[i,self.Y[i]]
        modelLH = -modelLH

        #prior for the model(code length)
        selCount = testX.shape[1]
        prior = math.log(self.fNum + 1) + math.log(comb(self.fNum + selCount - 1, selCount,exact = True))
        
        return modelLH + prior

    
    #Returns the mean accuracy on the given test data and labels.
    def score(self,data,cls,sample_weight = None):
        X = pd.DataFrame.as_matrix(pd.read_csv(data,header=None))
        Y = np.ravel(pd.DataFrame.as_matrix(pd.read_csv(cls,header=None)))
       
        print(self.bestSet)
        return self.NB.score(X[:,self.bestSet],Y,sample_weight)

    #Perform classification on an array of test vector X
    def predict(self,data):
        X = pd.DataFrame.as_matrix(pd.read_csv(data,header=None))
        return self.NB.predict(X[:,self.bestSet])

    def predict_log_proba(self,data):
        X = pd.DataFrame.as_matrix(pd.read_csv(data,header=None))
        return self.NB.predict_log_proba(X[:,self.bestSet])

    def predict_proba(self,data):
        X = pd.DataFrame.as_matrix(pd.read_csv(data,header=None))
        return self.NB.predict_proba(X[:,self.bestSet])

def main():
    SNB = SNBMAP()
    SNB.train('value_train_refined.csv','value_label.txt')
    print(SNB.score('value_train_refined.csv','value_label.txt'))
    print(SNB.predict('value_train_refined.csv'))
    print(SNB.predict_log_proba('value_train_refined.csv'))
    print(SNB.predict_proba('value_train_refined.csv'))

if __name__ == "__main__":
    main()
        
