import logging
import sys

#home_path = '/home/martin/.local/lib/python3.9/site-packages'
#if home_path not in sys.path:
#	sys.path.append(home_path)

from remote import lancer_remote, stopper_remote
from webserver import lancer_serveur

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    lancer_remote()
    lancer_serveur()
    stopper_remote()
