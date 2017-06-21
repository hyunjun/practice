#! /usr/bin/python3

import site
site.addsitedir("/var/www/apache-flask")
site.addsitedir("/usr/bin/python3")

from app import app as application
import sys
sys.path.append("/var/www/apache-flask")
