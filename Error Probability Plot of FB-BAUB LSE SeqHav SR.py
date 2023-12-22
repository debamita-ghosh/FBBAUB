#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import os


# In[29]:


#=================================== Experiment 1  ==========================================


conf_prob_our_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt1_K_80.txt", delimiter='\t')
lconf_prob_our_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt1_K_80.txt", delimiter='\t')
uconf_prob_our_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt1_K_80.txt", delimiter='\t')

conf_prob_LSE_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt1_K_80.txt", delimiter='\t')
lconf_prob_LSE_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt1_K_80.txt", delimiter='\t')
uconf_prob_LSE_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt1_K_80.txt", delimiter='\t')

conf_prob_SeqHav_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt1_K_80.txt", delimiter='\t')
lconf_prob_SeqHav_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt1_K_80.txt", delimiter='\t')
uconf_prob_SeqHav_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt1_K_80.txt", delimiter='\t')

conf_prob_SR_80_uni1 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt1_K_80.txt", delimiter='\t')
lconf_prob_SR_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt1_K_80.txt", delimiter='\t')
uconf_prob_SR_80_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt1_K_80.txt", delimiter='\t')

##################################
conf_prob_our_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt1_K_100.txt", delimiter='\t')
lconf_prob_our_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt1_K_100.txt", delimiter='\t')
uconf_prob_our_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt1_K_100.txt", delimiter='\t')

conf_prob_LSE_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt1_K_100.txt", delimiter='\t')
lconf_prob_LSE_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt1_K_100.txt", delimiter='\t')
uconf_prob_LSE_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt1_K_100.txt", delimiter='\t')

conf_prob_SeqHav_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt1_K_100.txt", delimiter='\t')
lconf_prob_SeqHav_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt1_K_100.txt", delimiter='\t')
uconf_prob_SeqHav_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt1_K_100.txt", delimiter='\t')

conf_prob_SR_100_uni1 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt1_K_100.txt", delimiter='\t')
lconf_prob_SR_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt1_K_100.txt", delimiter='\t')
uconf_prob_SR_100_uni1 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt1_K_100.txt", delimiter='\t')


# In[30]:


#=================================== Experiment 2  ==========================================


conf_prob_our_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt2_K_80.txt", delimiter='\t')
lconf_prob_our_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt2_K_80.txt", delimiter='\t')
uconf_prob_our_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt2_K_80.txt", delimiter='\t')

conf_prob_LSE_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt2_K_80.txt", delimiter='\t')
lconf_prob_LSE_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt2_K_80.txt", delimiter='\t')
uconf_prob_LSE_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt2_K_80.txt", delimiter='\t')

conf_prob_SeqHav_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt2_K_80.txt", delimiter='\t')
lconf_prob_SeqHav_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt2_K_80.txt", delimiter='\t')
uconf_prob_SeqHav_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt2_K_80.txt", delimiter='\t')

conf_prob_SR_80_uni2 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt2_K_80.txt", delimiter='\t')
lconf_prob_SR_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt2_K_80.txt", delimiter='\t')
uconf_prob_SR_80_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt2_K_80.txt", delimiter='\t')

##################################
conf_prob_our_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt2_K_100.txt", delimiter='\t')
lconf_prob_our_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt2_K_100.txt", delimiter='\t')
uconf_prob_our_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt2_K_100.txt", delimiter='\t')

conf_prob_LSE_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt2_K_100.txt", delimiter='\t')
lconf_prob_LSE_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt2_K_100.txt", delimiter='\t')
uconf_prob_LSE_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt2_K_100.txt", delimiter='\t')

conf_prob_SeqHav_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt2_K_100.txt", delimiter='\t')
lconf_prob_SeqHav_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt2_K_100.txt", delimiter='\t')
uconf_prob_SeqHav_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt2_K_100.txt", delimiter='\t')

conf_prob_SR_100_uni2 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt2_K_100.txt", delimiter='\t')
lconf_prob_SR_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt2_K_100.txt", delimiter='\t')
uconf_prob_SR_100_uni2 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt2_K_100.txt", delimiter='\t')


# In[31]:


#=================================== Experiment 3  ==========================================


conf_prob_our_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt3_K_80.txt", delimiter='\t')
lconf_prob_our_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt3_K_80.txt", delimiter='\t')
uconf_prob_our_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt3_K_80.txt", delimiter='\t')

conf_prob_LSE_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt3_K_80.txt", delimiter='\t')
lconf_prob_LSE_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt3_K_80.txt", delimiter='\t')
uconf_prob_LSE_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt3_K_80.txt", delimiter='\t')

conf_prob_SeqHav_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt3_K_80.txt", delimiter='\t')
lconf_prob_SeqHav_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt3_K_80.txt", delimiter='\t')
uconf_prob_SeqHav_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt3_K_80.txt", delimiter='\t')

conf_prob_SR_80_uni3 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt3_K_80.txt", delimiter='\t')
lconf_prob_SR_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt3_K_80.txt", delimiter='\t')
uconf_prob_SR_80_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt3_K_80.txt", delimiter='\t')

##################################
conf_prob_our_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt3_K_100.txt", delimiter='\t')
lconf_prob_our_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt3_K_100.txt", delimiter='\t')
uconf_prob_our_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt3_K_100.txt", delimiter='\t')

conf_prob_LSE_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt3_K_100.txt", delimiter='\t')
lconf_prob_LSE_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt3_K_100.txt", delimiter='\t')
uconf_prob_LSE_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt3_K_100.txt", delimiter='\t')

conf_prob_SeqHav_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt3_K_100.txt", delimiter='\t')
lconf_prob_SeqHav_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt3_K_100.txt", delimiter='\t')
uconf_prob_SeqHav_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt3_K_100.txt", delimiter='\t')

conf_prob_SR_100_uni3 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt3_K_100.txt", delimiter='\t')
lconf_prob_SR_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt3_K_100.txt", delimiter='\t')
uconf_prob_SR_100_uni3 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt3_K_100.txt", delimiter='\t')


# In[32]:


#=================================== Experiment 4  ==========================================


conf_prob_our_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt4_K_80.txt", delimiter='\t')
lconf_prob_our_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt4_K_80.txt", delimiter='\t')
uconf_prob_our_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt4_K_80.txt", delimiter='\t')

conf_prob_LSE_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt4_K_80.txt", delimiter='\t')
lconf_prob_LSE_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt4_K_80.txt", delimiter='\t')
uconf_prob_LSE_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt4_K_80.txt", delimiter='\t')

conf_prob_SeqHav_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt4_K_80.txt", delimiter='\t')
lconf_prob_SeqHav_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt4_K_80.txt", delimiter='\t')
uconf_prob_SeqHav_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt4_K_80.txt", delimiter='\t')

conf_prob_SR_80_uni4 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt4_K_80.txt", delimiter='\t')
lconf_prob_SR_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt4_K_80.txt", delimiter='\t')
uconf_prob_SR_80_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt4_K_80.txt", delimiter='\t')

##################################
conf_prob_our_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\conf_prob_our_Expt4_K_100.txt", delimiter='\t')
lconf_prob_our_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\lconf_prob_our_Expt4_K_100.txt", delimiter='\t')
uconf_prob_our_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\our\\uconf_prob_our_Expt4_K_100.txt", delimiter='\t')

conf_prob_LSE_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\conf_prob_LSE_Expt4_K_100.txt", delimiter='\t')
lconf_prob_LSE_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\lconf_prob_LSE_Expt4_K_100.txt", delimiter='\t')
uconf_prob_LSE_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\LSE\\uconf_prob_LSE_Expt4_K_100.txt", delimiter='\t')

conf_prob_SeqHav_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\conf_prob_SeqHav_Expt4_K_100.txt", delimiter='\t')
lconf_prob_SeqHav_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\lconf_prob_SeqHav_Expt4_K_100.txt", delimiter='\t')
uconf_prob_SeqHav_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SeqHav\\uconf_prob_SeqHav_Expt4_K_100.txt", delimiter='\t')

conf_prob_SR_100_uni4 =  np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\conf_prob_SR_Expt4_K_100.txt", delimiter='\t')
lconf_prob_SR_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\lconf_prob_SR_Expt4_K_100.txt", delimiter='\t')
uconf_prob_SR_100_uni4 = np.loadtxt("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\data\\proberr\\SR\\uconf_prob_SR_Expt4_K_100.txt", delimiter='\t')


# In[33]:


# =============================================================================
#############################################################################################
conf_prob_our_uni1 = np.array([conf_prob_our_80_uni1, conf_prob_our_100_uni1])
lconf_prob_our_uni1 = np.array([lconf_prob_our_80_uni1, lconf_prob_our_100_uni1])
uconf_prob_our_uni1 = np.array([uconf_prob_our_80_uni1, uconf_prob_our_100_uni1])

conf_prob_LSE_uni1 = np.array([conf_prob_LSE_80_uni1, conf_prob_LSE_100_uni1])
lconf_prob_LSE_uni1 = np.array([lconf_prob_LSE_80_uni1, lconf_prob_LSE_100_uni1])
uconf_prob_LSE_uni1 = np.array([uconf_prob_LSE_80_uni1, uconf_prob_LSE_100_uni1])

conf_prob_SeqHav_uni1 = np.array([conf_prob_SeqHav_80_uni1, conf_prob_SeqHav_100_uni1])
lconf_prob_SeqHav_uni1 = np.array([lconf_prob_SeqHav_80_uni1, lconf_prob_SeqHav_100_uni1])
uconf_prob_SeqHav_uni1 = np.array([uconf_prob_SeqHav_80_uni1, uconf_prob_SeqHav_100_uni1])

conf_prob_SR_uni1 = np.array([conf_prob_SR_80_uni1, conf_prob_SR_100_uni1])
lconf_prob_SR_uni1 = np.array([lconf_prob_SR_80_uni1, lconf_prob_SR_100_uni1])
uconf_prob_SR_uni1 = np.array([uconf_prob_SR_80_uni1, uconf_prob_SR_100_uni1])

#############################################################################################
conf_prob_our_uni2 = np.array([conf_prob_our_80_uni1, conf_prob_our_80_uni2])
lconf_prob_our_uni2 = np.array([lconf_prob_our_80_uni1, lconf_prob_our_80_uni2])
uconf_prob_our_uni2 = np.array([uconf_prob_our_80_uni1, uconf_prob_our_80_uni2])

conf_prob_LSE_uni2 = np.array([conf_prob_LSE_80_uni1, conf_prob_LSE_80_uni2])
lconf_prob_LSE_uni2 = np.array([lconf_prob_LSE_80_uni1, lconf_prob_LSE_80_uni2])
uconf_prob_LSE_uni2 = np.array([uconf_prob_LSE_80_uni1, uconf_prob_LSE_80_uni2])

conf_prob_SeqHav_uni2 = np.array([conf_prob_SeqHav_80_uni1, conf_prob_SeqHav_80_uni2])
lconf_prob_SeqHav_uni2 = np.array([lconf_prob_SeqHav_80_uni1, lconf_prob_SeqHav_80_uni2])
uconf_prob_SeqHav_uni2 = np.array([uconf_prob_SeqHav_80_uni1, uconf_prob_SeqHav_80_uni2])

conf_prob_SR_uni2 = np.array([conf_prob_SR_80_uni1, conf_prob_SR_80_uni2])
lconf_prob_SR_uni2 = np.array([lconf_prob_SR_80_uni1, lconf_prob_SR_80_uni2])
uconf_prob_SR_uni2 = np.array([uconf_prob_SR_80_uni1, uconf_prob_SR_80_uni2])

###############################################################################################
conf_prob_our_uni2_100 = np.array([conf_prob_our_100_uni1, conf_prob_our_100_uni2])
lconf_prob_our_uni2_100 = np.array([lconf_prob_our_100_uni1, lconf_prob_our_100_uni2])
uconf_prob_our_uni2_100 = np.array([uconf_prob_our_100_uni1, uconf_prob_our_100_uni2])

conf_prob_LSE_uni2_100 = np.array([conf_prob_LSE_100_uni1, conf_prob_LSE_100_uni2])
lconf_prob_LSE_uni2_100 = np.array([lconf_prob_LSE_100_uni1, lconf_prob_LSE_100_uni2])
uconf_prob_LSE_uni2_100 = np.array([uconf_prob_LSE_100_uni1, uconf_prob_LSE_100_uni2])

conf_prob_SeqHav_uni2_100 = np.array([conf_prob_SeqHav_100_uni1, conf_prob_SeqHav_100_uni2])
lconf_prob_SeqHav_uni2_100 = np.array([lconf_prob_SeqHav_100_uni1, lconf_prob_SeqHav_100_uni2])
uconf_prob_SeqHav_uni2_100 = np.array([uconf_prob_SeqHav_100_uni1, uconf_prob_SeqHav_100_uni2])

conf_prob_SR_uni2_100 = np.array([conf_prob_SR_100_uni1, conf_prob_SR_100_uni2])
lconf_prob_SR_uni2_100 = np.array([lconf_prob_SR_100_uni1, lconf_prob_SR_100_uni2])
uconf_prob_SR_uni2_100 = np.array([uconf_prob_SR_100_uni1, uconf_prob_SR_100_uni2])

#=============================================================================

conf_prob_our_uni3 = np.array([conf_prob_our_80_uni3, conf_prob_our_100_uni3])
lconf_prob_our_uni3 = np.array([lconf_prob_our_80_uni3, lconf_prob_our_100_uni3])
uconf_prob_our_uni3 = np.array([uconf_prob_our_80_uni3, uconf_prob_our_100_uni3])

conf_prob_LSE_uni3 = np.array([conf_prob_LSE_80_uni3, conf_prob_LSE_100_uni3])
lconf_prob_LSE_uni3 = np.array([lconf_prob_LSE_80_uni3, lconf_prob_LSE_100_uni3])
uconf_prob_LSE_uni3 = np.array([uconf_prob_LSE_80_uni3, uconf_prob_LSE_100_uni3])

conf_prob_SeqHav_uni3 = np.array([conf_prob_SeqHav_80_uni3, conf_prob_SeqHav_100_uni3])
lconf_prob_SeqHav_uni3 = np.array([lconf_prob_SeqHav_80_uni3, lconf_prob_SeqHav_100_uni3])
uconf_prob_SeqHav_uni3 = np.array([uconf_prob_SeqHav_80_uni3, uconf_prob_SeqHav_100_uni3])

conf_prob_SR_uni3 = np.array([conf_prob_SR_80_uni3, conf_prob_SR_100_uni3])
lconf_prob_SR_uni3 = np.array([lconf_prob_SR_80_uni3, lconf_prob_SR_100_uni3])
uconf_prob_SR_uni3 = np.array([uconf_prob_SR_80_uni3, uconf_prob_SR_100_uni3])

#=============================================================================

conf_prob_our_uni4 = np.array([conf_prob_our_80_uni4, conf_prob_our_100_uni4])
lconf_prob_our_uni4 = np.array([lconf_prob_our_80_uni4, lconf_prob_our_100_uni4])
uconf_prob_our_uni4 = np.array([uconf_prob_our_80_uni4, uconf_prob_our_100_uni4])

conf_prob_LSE_uni4 = np.array([conf_prob_LSE_80_uni4, conf_prob_LSE_100_uni4])
lconf_prob_LSE_uni4 = np.array([lconf_prob_LSE_80_uni4, lconf_prob_LSE_100_uni4])
uconf_prob_LSE_uni4 = np.array([uconf_prob_LSE_80_uni4, uconf_prob_LSE_100_uni4])

conf_prob_SeqHav_uni4 = np.array([conf_prob_SeqHav_80_uni4, conf_prob_SeqHav_100_uni4])
lconf_prob_SeqHav_uni4 = np.array([lconf_prob_SeqHav_80_uni4, lconf_prob_SeqHav_100_uni4])
uconf_prob_SeqHav_uni4 = np.array([uconf_prob_SeqHav_80_uni4, uconf_prob_SeqHav_100_uni4])

conf_prob_SR_uni4 = np.array([conf_prob_SR_80_uni4, conf_prob_SR_100_uni4])
lconf_prob_SR_uni4 = np.array([lconf_prob_SR_80_uni4, lconf_prob_SR_100_uni4])
uconf_prob_SR_uni4 = np.array([uconf_prob_SR_80_uni4, uconf_prob_SR_100_uni4])


# In[36]:


# ===================================== Experiment 3 (no of arms) (AP) ========================================

T1= np.array([50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])  

markers = ['*', 'o']
labels1 = ['FB-BAUB, K=80', 'FB-BAUB, K=100']
labels2 = ['LSE, K=80', 'LSE, K=100']
labels3 = ['Seq. Halv., K=80', 'Seq. Halv., K=100']
labels4 = ['SR, K=80', 'SR, K=100']
line_type = ['-', '-.']
plt.rcParams['pdf.fonttype'] = 42

for idx in range(conf_prob_our_uni3.shape[0]):
    for lower, upper, T in zip(lconf_prob_our_uni3[idx], uconf_prob_our_uni3[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'r', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'r', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'r', alpha = 0.4)
    
    plt.plot(T1, conf_prob_our_uni3[idx], 
              line_type[idx], 
              color = 'r', 
              marker = markers[idx], 
              label = labels1[idx])
    
    for lower, upper, T in zip(lconf_prob_LSE_uni3[idx], uconf_prob_LSE_uni3[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'b', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'b', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'b', alpha = 0.4)

    plt.plot(T1, conf_prob_LSE_uni3[idx], 
          line_type[idx], 
          color = 'b', 
          marker = markers[idx], 
          label = labels2[idx])
    
    for lower, upper, T in zip(lconf_prob_SeqHav_uni3[idx], uconf_prob_SeqHav_uni3[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'k', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'k', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'k', alpha = 0.4)

    plt.plot(T1, conf_prob_SeqHav_uni3[idx], 
          line_type[idx], 
          color = 'k', 
          marker = markers[idx], 
          label = labels3[idx])

    for lower, upper, T in zip(lconf_prob_SR_uni3[idx], uconf_prob_SR_uni3[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'forestgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'forestgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'forestgreen', alpha = 0.4)

    plt.plot(T1, conf_prob_SR_uni3[idx], 
          line_type[idx], 
          color = 'forestgreen',
          marker = markers[idx], 
          label = labels4[idx])

legend_properties = {'weight':'bold'}
plt.legend(loc='upper right', fontsize = 10, prop=legend_properties)
plt.xlabel('Budget (T)', fontsize=14, fontweight='bold')
plt.ylabel('Error Probability', fontsize=14, fontweight='bold')
#plt.yscale('log')
plt.ylim(0,0.7)
plt.grid()

plt.savefig(os.path.join("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\plots\\TMLR_prob_err_T_K_80_100_uni3.pdf"),bbox_inches="tight")


# In[37]:


# ===================================== Experiment 4 (no of arms) (GP) ========================================

T1= np.array([50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])  

markers = ['*', 'o']
labels1 = ['FB-BAUB, K=80', 'FB-BAUB, K=100']
labels2 = ['LSE, K=80', 'LSE, K=100']
labels3 = ['Seq. Halv., K=80', 'Seq. Halv., K=100']
labels4 = ['SR, K=80', 'SR, K=100']
line_type = ['-', '-.']
plt.rcParams['pdf.fonttype'] = 42

for idx in range(conf_prob_our_uni4.shape[0]):
    for lower, upper, T in zip(lconf_prob_our_uni4[idx], uconf_prob_our_uni4[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'r', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'r', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'r', alpha = 0.4)
    
    plt.plot(T1, conf_prob_our_uni4[idx], 
              line_type[idx], 
              color = 'r', 
              marker = markers[idx], 
              label = labels1[idx])
    
    for lower, upper, T in zip(lconf_prob_LSE_uni4[idx], uconf_prob_LSE_uni4[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'b', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'b', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'b', alpha = 0.4)

    plt.plot(T1, conf_prob_LSE_uni4[idx], 
          line_type[idx], 
          color = 'b', 
          marker = markers[idx], 
          label = labels2[idx])
    
    for lower, upper, T in zip(lconf_prob_SeqHav_uni4[idx], uconf_prob_SeqHav_uni4[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'k', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'k', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'k', alpha = 0.4)

    plt.plot(T1, conf_prob_SeqHav_uni4[idx], 
          line_type[idx], 
          color = 'k', 
          marker = markers[idx], 
          label = labels3[idx])

    for lower, upper, T in zip(lconf_prob_SR_uni4[idx], uconf_prob_SR_uni4[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'forestgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'forestgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'forestgreen', alpha = 0.4)

    plt.plot(T1, conf_prob_SR_uni4[idx], 
          line_type[idx], 
          color = 'forestgreen',
          marker = markers[idx],
          label = labels4[idx])


legend_properties = {'weight':'bold'}
plt.legend(loc='upper center', fontsize = 10, prop=legend_properties)
plt.xlabel('Budget (T)', fontsize=14, fontweight='bold')
plt.ylabel('Error Probability', fontsize=14, fontweight='bold')
#plt.yscale('log')
plt.ylim(0,0.7)
plt.grid()

plt.savefig(os.path.join("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\plots\\TMLR_prob_err_T_K_80_100_uni4.pdf"),bbox_inches="tight")


# In[40]:


# ===================================== Expt 1 and Expt 2 for K=80 ========================================

T1= np.array([50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
markers = ['*', 'o']
labels1 = ['FB-BAUB, K = 80, Experiment 1', 'FB-BAUB, K = 80, Experiment 2']
labels2 = ['LSE, K = 80, Experiment 1', 'LSE, K = 80, Experiment 2']
labels3 = ['Seq. Halv., K = 80, Experiment 1', 'Seq. Halv., K = 80, Experiment 2']
labels4 = ['SR, K = 80, Experiment 1', 'SR, K = 80, Experiment 2']
line_type = ['-', '-.']
plt.rcParams['pdf.fonttype'] = 42

for idx in range(conf_prob_our_uni2.shape[0]):
    for lower, upper, T in zip(lconf_prob_our_uni2[idx], uconf_prob_our_uni2[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'purple', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'purple', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'purple', alpha = 0.4)
    
    plt.plot(T1, conf_prob_our_uni2[idx], 
              line_type[idx], 
              color = 'purple', 
              marker = markers[idx], 
              label = labels1[idx])
    
    for lower, upper, T in zip(lconf_prob_LSE_uni2[idx], uconf_prob_LSE_uni2[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'darkolivegreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'darkolivegreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'darkolivegreen', alpha = 0.4)

    plt.plot(T1, conf_prob_LSE_uni2[idx], 
          line_type[idx], 
          color = 'darkolivegreen', 
          marker = markers[idx], 
          label = labels2[idx])
    
    for lower, upper, T in zip(lconf_prob_SeqHav_uni2[idx], uconf_prob_SeqHav_uni2[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'teal', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'teal', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'teal', alpha = 0.4)

    plt.plot(T1, conf_prob_SeqHav_uni2[idx], 
          line_type[idx], 
          color = 'teal', 
          marker = markers[idx], 
          label = labels3[idx])
    
    for lower, upper, T in zip(lconf_prob_SR_uni2[idx], uconf_prob_SR_uni2[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'darkred', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'darkred', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'darkred', alpha = 0.4)

    plt.plot(T1, conf_prob_SR_uni2[idx], 
          line_type[idx], 
          color = 'darkred', 
          marker = markers[idx], 
          label = labels4[idx])
    
legend_properties = {'weight':'bold'}
plt.legend(loc='upper center', fontsize = 10, prop=legend_properties)
plt.xlabel('Budget (T)', fontsize=14, fontweight='bold')
plt.ylabel('Error Probability', fontsize=14, fontweight='bold')
plt.ylim(0,0.9)
plt.grid()

plt.savefig(os.path.join("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\plots\\TMLR_prob_err_T_K_80_uni1_uni2.pdf"),bbox_inches="tight")


# In[44]:


# ===================================== Expt 1 and Expt 2 for K=100 ========================================

T1= np.array([50, 100, 500, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
markers = ['*', 'o']
labels1 = ['FB-BAUB, K = 100, Experiment 1', 'FB-BAUB, K = 100, Experiment 2']
labels2 = ['LSE, K = 100, Experiment 1', 'LSE, K = 100, Experiment 2']
labels3 = ['Seq. Halv., K = 100, Experiment 1', 'Seq. Halv., K = 100, Experiment 2']
labels4 = ['SR, K = 100, Experiment 1', 'SR, K = 100, Experiment 2']
line_type = ['-', '-.']
plt.rcParams['pdf.fonttype'] = 42

for idx in range(conf_prob_our_uni2_100.shape[0]):
    for lower, upper, T in zip(lconf_prob_our_uni2_100[idx], uconf_prob_our_uni2_100[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'purple', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'purple', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'purple', alpha = 0.4)
    
    plt.plot(T1, conf_prob_our_uni2_100[idx], 
              line_type[idx], 
              color = 'purple', 
              marker = markers[idx], 
              label = labels1[idx])
    
    for lower, upper, T in zip(lconf_prob_LSE_uni2_100[idx], uconf_prob_LSE_uni2_100[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'darkgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'darkgreen', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'darkgreen', alpha = 0.4)

    plt.plot(T1, conf_prob_LSE_uni2_100[idx], 
          line_type[idx], 
          color = 'darkgreen', 
          marker = markers[idx], 
          label = labels2[idx])
    
    for lower, upper, T in zip(lconf_prob_SeqHav_uni2_100[idx], uconf_prob_SeqHav_uni2_100[idx], T1):
        plt.plot((T,T), (upper, lower), line_type[idx], color = 'teal', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'teal', alpha = 0.4)
        plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'teal', alpha = 0.4)

    plt.plot(T1, conf_prob_SeqHav_uni2_100[idx], 
          line_type[idx], 
          color = 'teal', 
          marker = markers[idx], 
          label = labels3[idx])
        
    for lower, upper, T in zip(lconf_prob_SR_uni2_100[idx], uconf_prob_SR_uni2_100[idx], T1):
         plt.plot((T,T), (upper, lower), line_type[idx], color = 'darkred', alpha = 0.4)
         plt.plot((T - 0.125, T + 0.125), (upper, upper), line_type[idx], color = 'darkred', alpha = 0.4)
         plt.plot((T - 0.125, T + 0.125), (lower, lower), line_type[idx], color = 'darkred', alpha = 0.4)
    
    plt.plot(T1, conf_prob_SR_uni2_100[idx],
        line_type[idx], 
        color = 'darkred', 
        marker = markers[idx], 
        label = labels4[idx])
    
    
legend_properties = {'weight':'bold'}
plt.legend(loc='upper center', fontsize = 10, prop=legend_properties)
plt.xlabel('Budget (T)', fontsize=14, fontweight='bold')
plt.ylabel('Error Probability', fontsize=14, fontweight='bold')
plt.ylim(0,0.9)
plt.grid()
plt.savefig(os.path.join("D:\\PhD IITB-MONASH\\PhD\\Problem 4\\Unimodal Code Infocom 2022\\TMLR Code\\plots\\TMLR_prob_err_T_K_100_uni1_uni2.pdf"),bbox_inches="tight")


# In[ ]:




