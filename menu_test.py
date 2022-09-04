import PySimpleGUI as sg

# define layout
layout1 = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
           [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
           [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
           [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
           [sg.Button('Save Personal Details')]]
layout2 = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
           [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
           [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
           [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
           [sg.Button('Save Education Details')]]
layout3 = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
           [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
           [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
           [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
           [sg.Button('Save Experience Details')]]
# Define Layout with Tabs
tabgrp = [
    [sg.TabGroup([[sg.Tab('Personal Details', layout1, title_color='Red', border_width=10, background_color='Green',
                          tooltip='Personal details', element_justification='center'),
                   sg.Tab('Education', layout2, title_color='Blue', background_color='Yellow'),
                   sg.Tab('Experience', layout3, title_color='Black', background_color='Pink',
                          tooltip='Enter  your Lsst job experience')]], tab_location='centertop',
                 title_color='Red', tab_background_color='Purple', selected_title_color='Green',
                 selected_background_color='Gray', border_width=5), sg.Button('Close')]]

# Define Window
window = sg.Window("Tabs", tabgrp)
# Read  values entered by user
event, values = window.read()
# access all the values and if selected add them to a string
window.close()
