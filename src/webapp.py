#!flask/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from app import app

reload(sys)
sys.setdefaultencoding('utf8')

DEBUG = False

if 'DEBUG' in os.environ and os.environ['DEBUG'] == "1":
    DEBUG = True

app.run(debug=DEBUG, host='0.0.0.0', port=80)
