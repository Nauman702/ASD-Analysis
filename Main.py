import mne


url="C:\\Users\\nauma\\OneDrive - King's College London\\Research\\Autism Research\\ASD_Sheffield\\ASD Dataset\\EEGLAB"
raw = mne.io.read_raw_eeglab(url+"\\1Abby_Resting.set", preload=True)
#raw_fdt = mne.io.read_raw_ctf(url+"\\1Abby_Resting.fdt", preload=True)


#-----------------------------------------------

# Access the raw EEG data as a numpy array
eeg_data= raw.get_data()

#------------------------------------------------
# Access the associated metadata
info = raw.info

# Access the sampling rate (in Hz)
sfreq = raw.info['sfreq']

# Access the channel labels
ch_names = raw.info['ch_names']

# Access the channel types
#ch_types = raw.info['ch_types']

# Access the channel positions
ch_pos = raw.info['chs'][0]['loc']

#------------------------------------------------

print("Testing")
print(eeg_data)
print(ch_names)
#print(raw_fdt)