#!/usr/bin/env python3
# -*- ecoding: utf-8 -*-

import requests as re


class API:

    def __init__(self, estado, municipio):

        self.estado = estado

        self.municipio = municipio

        self.status = re.get(
            'https://brasil.io/api/dataset/covid19/caso/data?is_last=True&state={}&city={}'.format(self.estado, self.municipio))

    def get(self):

        return self.status.json()['results']
