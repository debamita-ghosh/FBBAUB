#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the libraries
import os
import numpy as np
import math
from tqdm import tqdm
import matplotlib.pyplot as plt


# In[2]:


###################### GENERATING SAMPLES ########################
def mean_reward(mean, sigma, samples):
    reward = np.random.normal(mean, sigma, samples)
    return reward


# In[10]:


#################################### SR ######################################
def CC(K):
    C = 0.5
    for i in range(2, K+1):
        C = C + 1/i
    return C

def SR(mean, sigma, T):
    K = len(mean)
    #initialization
    G = [i for i in range(K)]
    C = CC(K)
    n = [np.ceil(((T-K)/(C*(K-r)))) for r in range(K-1)]
    n.insert(0,0)
  
    #Algo starts here
    for r in range(K-1):
        Z = [np.mean(mean_reward(mean[G[i]], sigma[G[i]], int(n[r+1]-n[r])) if n[r+1]-n[r]>0 else 1 ) for i in range(len(G))]
        del G[Z.index(min(Z))]
  
    return G[0]


# In[14]:


Expt = 1
K = 80
mean_rewards1 = np.loadtxt('D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\unimodal expt\\Unimodal_Expt'+str(Expt)+'_K_'+str(K)+'.txt')
max_arm = np.argmax(mean_rewards1)
print("max_arm:", max_arm)
tinv = 1.9623
runs = 50
sigma = [5]*len(mean_rewards1)


# In[13]:


T1= np.array([50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])

prob_err_SR = np.zeros(len(T1))
uconf_prob_err_SR = np.zeros(len(T1))
lconf_prob_err_SR = np.zeros(len(T1))

for t in tqdm(range(len(T1))):
    err_SR = np.zeros(runs)

    for r in range(runs):
        arm_SR = SR(mean_rewards1, sigma, T1[t])            
        if arm_SR==max_arm:
            err_SR[r] = 0
        else:
            err_SR[r] = 1
    
    prob_err_SR[t] = np.sum(err_SR)/runs
    uconf_prob_err_SR[t] = prob_err_SR[t] + ((tinv*np.std(err_SR))/np.sqrt(runs-1))
    lconf_prob_err_SR[t] = prob_err_SR[t] - ((tinv*np.std(err_SR))/np.sqrt(runs-1))

np.savetxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt"+str(Expt)+'_K_'+str(K)+'.txt', prob_err_SR)
np.savetxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt"+str(Expt)+'_K_'+str(K)+'.txt', uconf_prob_err_SR)
np.savetxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt"+str(Expt)+'_K_'+str(K)+'.txt', lconf_prob_err_SR)


# In[ ]:




