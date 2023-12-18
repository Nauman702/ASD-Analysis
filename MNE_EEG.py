import mne
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

# #----------------------------Reading Data---------------------------
# url="C:\\Users\\nauma\\OneDrive - King's College London\\Research\\Autism Research\\ASD_Sheffield\\ASD Dataset\\EEGLAB"
# #url2= r"C:\Users\nauma\OneDrive - King's College London\Research\Autism Research\ASD_Sheffield"
# #Reading single file
# #raw = mne.io.read_raw_eeglab(url+"\\1Abby_Resting.set", preload=True)
# #raw_fdt = mne.io.read_raw_ctf(url+"\\1Abby_Resting.fdt", preload=True)

# #Reading all .set files and creating 3D numpy array

# eeg_data_list = []
# eeg_ch_list = []

# # Loop through all files
# for i in range(1,57):
#     # Read the .set file
#     raw = mne.io.read_raw_eeglab(url+'\\{}Abby_resting.set'.format(i), preload=True)

#     # Extract EEG data from the file
#     eeg_data = raw.get_data()
#     # Extract channels data from the file
#     eeg_ch = raw.info ['ch_names']
#     # Append EEG data to the list
#     eeg_data_list.append(eeg_data)
#     # Append channels data to the list
#     eeg_ch_list.append(eeg_ch)


# plt.ion() #Makes plot interactive
# raw.plot()