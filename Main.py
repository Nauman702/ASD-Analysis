import mne
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
%matplotlib qt
# #----------------------------Reading Data---------------------------
# #url="C:\\Users\\nauma\\OneDrive - King's College London\\Research\\Autism Research\\ASD_Sheffield\\ASD Dataset\\EEGLAB"
# url2= r"C:\Users\nauma\OneDrive - King's College London\Research\Autism Research\ASD_Sheffield"
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


# # Convert list to 3D numpy array
# eeg_data_3d = np.array(eeg_data_list)
# eeg_ch_3d = np.array(eeg_ch_list)

# #Reading Excel file, labels

# df = pd.read_excel(url2+'\Participant Data from Cohort 1 (Dickinson et al. 2022).xlsx')

# array = df.values
# #asd_td=
# #------------------Saving to Pickle---------------------

# # Save the array to a pickle file
# with open('EEG_data.pkl', 'wb') as f:
#     pickle.dump(eeg_data_3d, f)

# with open('EEG_ch.pkl', 'wb') as f:
#     pickle.dump(eeg_ch_3d, f)

# with open('labels_df.pkl', 'wb') as f:
#     pickle.dump(df, f)

#-----------------DATA from pickle-----------------------

url_pickle = r"C:\Users\nauma\OneDrive - King's College London\Research\Autism Research\ASD_Sheffield"




#Numpy Arrays
with open(url_pickle+"\EEG_data.pkl", 'rb') as f:
    eeg_data_3d = pickle.load(f)

with open(url_pickle+'\EEG_ch.pkl', 'rb') as f:
    eeg_ch_3d = pickle.load(f)



#Panda Dataframe
labels = pd.read_pickle(url_pickle+'\labels_df.pkl')


## number of channels in each subject data

print("EEG data shape",eeg_data_3d[0].shape())
ch_subjects=[]
for i in range(0,56):
    ch_subjects.append(len(eeg_data_3d[i]))

    


# # List of Lists
# eeg_data_list= eeg_data_3d.tolist()
# eeg_ch_list= eeg_ch_3d.tolist()

### ------------- Common channels List-------------

### its empty though 
# Find common channels across all subjects
common_channels = set(eeg_ch_list[0])
for channels in eeg_ch_list[1:]:
    common_channels.intersection_update(channels)

# Convert the set to a list of lists for each subject
common_channels_list = [list(common_channels) for _ in range(len(eeg_ch_list))]

# Print or use the result as needed
print(common_channels_list)


### occurances of a specific channel
matches=[]
for i in range(0,56):
    matches.append(list((x for x in eeg_ch_list[i] if x == 'A5')))

### occurances of each channel 

from collections import Counter

# Flatten the list of lists to get a single list of all electrodes
all_channels = [channel for channels in eeg_ch_list for channel in channels]

# Count occurrences of each electrode
channel_counts = Counter(all_channels)

# Print or use the result as needed
for channel, count in channel_counts.items():
    print(f"{channel}: {count} times")


####-----separate 128 and 64 channel recording as indexes---

list_64_ch = []
list_128_ch = []

for i, channels in enumerate(eeg_ch_list):
    if 'P1' in channels:
        list_64_ch.append(i)
    if 'A15' in channels:
        list_128_ch.append(i)

# Print or use the result as needed
print("Indexes containing 'P1':", list_64_ch)
print("Indexes containing 'A15':", list_128_ch)





#### ------ 128-64 channels equivalent---

df = pd.read_excel(url_pickle+"\\64_128_eq.xlsx")
out_list = df.to_numpy().tolist()
out_tuple= [tuple(elt) for elt in out_list]



####---- changing the channels list with new names 128-64 eq



# Replace electrode names in eeg_ch_list for the indexes in indexes_A15
for i in list_128_ch:
    for j, electrode in enumerate(eeg_ch_list[i]):
        for old_name, new_name in out_tuple:
            if electrode == old_name and new_name != '-':
                eeg_ch_list[i][j] = new_name

# Print or use the modified eeg_ch_list
print("Modified eeg_ch_list:", eeg_ch_list)







# #------------------Manipulating data----------------
# common_ch = set(eeg_ch_list[0]).intersection(*eeg_ch_list)
# print(common_ch)



# #---------------------EEG Electrodes Data-----------

# # Access the raw EEG data as a numpy array
# eeg_data= raw.get_data()

# #---------------------MetaData----------------------
# # Access the associated metadata
# info = raw.info

# # Access the sampling rate (in Hz)
# sfreq = raw.info['sfreq']

# # Access the channel labels
# ch_names = raw.info['ch_names']

# # Access the channel types
# #ch_types = raw.info['ch_types']

# # Access the channel positions
# ch_pos = raw.info['chs'][0]['loc']

# #--------------------Output-------------------------

# print("Testing")
# print(eeg_data.shape)

# print(len(ch_names))

# print(ch_names)
# #print(raw_fdt)

# #--------------------Montage------------------------

# # Define the montage
# montage = mne.channels.make_standard_montage('biosemi128')

# # Apply the montage to the raw data
# raw.set_montage(montage)

# Plot the montage
#mne.viz.plot_montage(montage, show_names=True, sphere=0.085)

#3D?

# #-------------------Plotting--------------------------
# # Plot the EEG data
# #mne.viz.plot_raw(raw, n_channels=56, color='blue', show_options=True)

# # Estimate the power spectral density
# psds, freqs = mne.time_frequency.psd_array_multitaper(eeg_data, fmin=0, fmax=40,sfreq=raw.info['sfreq'])

# # Plot the power spectral density for each channel
# n_channels = eeg_ch_3d.shape[0]
# for i in range(n_channels):
#     plt.plot(freqs, psds[i], label=eeg_ch_3d[0][i])
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Power Spectral Density (V^2/Hz)')
# plt.legend(ncol=8, loc='upper left')
# plt.show()


#------------------Testing---------------------
# #standardizing montage  ### didnt work
# #from mne.channels import make_standard_montage
# from mne import create_info, pick_channels

# ch_types = ['eeg'] * len(eeg_ch_list[0])
# info = create_info(eeg_ch_list[0], sfreq=512., ch_types=ch_types)


# # Create a custom montage based on the 10-20 system
# montage = make_standard_montage('biosemi128')

# # Find the channel indices that match the 10-20 system
# picks = pick_channels(eeg_ch_list[0], include=montage.eeg_ch_list[0])

# # Interpolate the data to the 10-20 system montage
# data_interp = np.zeros((len(montage.eeg_ch_list[0]), eeg_data_3d[0].shape[1]))
# data_interp[np.in1d(montage.eeg_ch_list[0], eeg_ch_list[0][picks])] = eeg_data_3d[0][picks]


#unique channels in all subjects
list_of_lists = eeg_ch_list
unique_strings = set([string for sublist in list_of_lists for string in sublist])
print(unique_strings)


# size of each list
result = [len(i) for i in list_of_lists]
print(result)


## raw.plot plotting any particular channel or group of channels

picks = mne.pick_channels_regexp(diode.ch_names, regexp='70')
diode.plot(order=picks, n_channels=len(picks))