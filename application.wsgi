import sys
import logging
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

from unisocial import app as application
