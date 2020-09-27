#!/usr/bin/env python3
# -*- ecoding: utf-8 -*-

import PySimpleGUI as sg


class APP:

    def __init__(self):

        self.layout = [

            [sg.Text('Estado', font='12'), sg.Combo(['', 'Estados'], size=(15, 1), font='12'),

             sg.Text('Município', font='12'), sg.Combo([''], size=(15, 1), font='12')],

            [sg.Submit('Mostrar', font='12'), sg.Cancel('Cancelar', font='12')]
        ]

        self.window = sg.Window('COVID-GUI', self.layout)

        self.event = self.window.read()

    def gui(self):

        return self.event


if __name__ == "__main__":

    APP().gui()
