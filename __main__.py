#!/usr/bin/env python
# -*- coding: utf-8 -*-


TARGETS = [
    'resgen_web.py',
]


PACKAGE = {
    'title': 'resgen',
    'desc': 'in-browser part generator',
}


def setup(targets):
    '''Setup example for translation, MUST call util.setup(targets).'''
    util.setup(targets)


def translate():
    '''Translate example, MUST call util.translate().'''
    util.translate()


def install(package):
    '''Install and cleanup example module. MUST call util.install(package)'''
    util.install(package)


##---------------------------------------##
# --------- (-: DO NOT EDIT :-) --------- #
##---------------------------------------##


import sys
import os

setup(TARGETS)
translate()
install(PACKAGE)
