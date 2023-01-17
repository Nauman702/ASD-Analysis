import mne
import matplotlib.pyplot as plt


url="C:\\Users\\nauma\\OneDrive - King's College London\\Research\\Autism Research\\ASD_Sheffield\\ASD Dataset\\EEGLAB"
raw = mne.io.read_raw_eeglab(url+"\\1Abby_Resting.set", preload=True)
#raw_fdt = mne.io.read_raw_ctf(url+"\\1Abby_Resting.fdt", preload=True)


#---------------------EEG Electrodes Data-----------

# Access the raw EEG data as a numpy array
eeg_data= raw.get_data()

#---------------------MetaData----------------------
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

#--------------------Output-------------------------

print("Testing")
print(eeg_data.shape)

print(len(ch_names))

print(ch_names)
#print(raw_fdt)

#--------------------Montage------------------------

# Define the montage
montage = mne.channels.make_standard_montage('biosemi64')

# Apply the montage to the raw data
raw.set_montage(montage)

# Plot the montage
mne.viz.plot_montage(montage, show_names=True, sphere=0.085)

#3D?

#-------------------Plotting--------------------------
# Plot the EEG data
mne.viz.plot_raw(raw, n_channels=56, color='blue', show_options=True)

# Estimate the power spectral density
psds, freqs = mne.time_frequency.psd_array_multitaper(eeg_data, fmin=0, fmax=40,sfreq=raw.info['sfreq'])

# Plot the power spectral density for each channel
n_channels = eeg_data.shape[0]
for i in range(n_channels):
    plt.plot(freqs, psds[i], label=raw.ch_names[i])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (V^2/Hz)')
plt.legend()
plt.show()