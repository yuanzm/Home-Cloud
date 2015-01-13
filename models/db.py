#!/usr/bin/env python
# coding=utf-8

import pymongo

conn = pymongo.Connection("localhost", 27017)
db = conn["Home-Cloud"]