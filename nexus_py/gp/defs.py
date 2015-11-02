# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 15:41:41 2015

Gait lab -specific stuff (electrode names etc.)

@author: Jussi
"""

# EMG device name
emg_devname = 'Myon'


# dict for electrode names and descriptions
emg_labels = {'RHam': 'Medial hamstrings (R)',
           'RRec': 'Rectus femoris (R)',
           'RGas': 'Gastrognemius (R)',
           'RGlut': 'Gluteus (R)',
           'RVas': 'Vastus (R)',
           'RSol': 'Soleus (R)',
           'RTibA': 'Tibialis anterior (R)',
           'RPer': 'Peroneus (R)',
           'LHam': 'Medial hamstrings (L)',
           'LRec': 'Rectus femoris (L)',
           'LGas': 'Gastrognemius (L)',
           'LGlut': 'Gluteus (L)',
           'LVas': 'Vastus (L)',
           'LSol': 'Soleus (L)',
           'LTibA': 'Tibialis anterior (L)',
           'LPer': 'Peroneus (L)'}

# EMG normal bars (the expected range of activation during gait cycle),
# axis is 0..100%
emg_normals = {'RGas': [[16,50]],
       'RGlut': [[0,42],[96,100]],
       'RHam': [[0,2],[92,100]],
       'RPer': [[4,54]],
       'RRec': [[0,14],[56,100]],
       'RSol': [[10,54]],
       'RTibA': [[0,12],[56,100]],
       'RVas': [[0,24],[96,100]],
       'LGas': [[16,50]],
       'LGlut': [[0,42],[96,100]],
       'LHam': [[0,2],[92,100]],
       'LPer': [[4,54]],
       'LRec': [[0,14],[56,100]],
       'LSol': [[10,54]],
       'LTibA': [[0,12],[56,100]],
       'LVas': [[0,24],[96,100]]}

# put names into a separate variable
emg_names = emg_labels.keys()


# video device ids to friendly names. used in layouts.py
video_id_front = '59875835'
video_id_side = '64826554'

