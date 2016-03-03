# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:37:51 2015

Kinematics only -EMG plot from Nexus (no kinetics) + PDF.
L/R sides on separate plots.
Get all cycles from data and overlay.

@author: Jussi
"""

 
from gp.plot import gaitplotter
import gp.layouts

plotheightratios = [3,2,2,2,2,2,2]
pdf_prefix = 'Kinematics_EMG_'
maintitleprefix='Kinematics-EMG plot for '

emgcolors = ['b','g','r','c','m','y','k']

for side in ['L','R']:
    gplotter = gaitplotter()
    gplotter.open_nexus_trial()
    plotvars_ = gp.layouts.kinematics_emg(side)
    plotvars = plotvars_ + [['emglegend',None,None]]
    #plotvars = gp.layouts.overlay_emg
    gplotter.read_trial(plotvars)

    cyc = 1

    while gplotter.trial.get_cycle('L',cyc) and gplotter.trial.get_cycle('R',cyc):
        
        trialname = gplotter.trial.trialname
        maintitle = maintitleprefix + trialname + ' ('+side+')'
        maintitle = maintitle + '\n' + gplotter.get_emg_filter_description()
        emgcolor = emgcolors[cyc-1]
        gplotter.plot_trial(plotheightratios=plotheightratios, maintitle=maintitle, cycle=cyc, emg_tracecolor=emgcolor)
        cyc += 1
        #gplotter.create_pdf(pdf_name=pdf_prefix+trialname+'_'+side+'.pdf')
        gplotter.show()

