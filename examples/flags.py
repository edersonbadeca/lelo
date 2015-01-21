"""
flags.py: Download public-domain country flag images from the web

Usage examples:

    $ python flags.py        # download a default number of flags
    $ python flags.py 30     # download 30 flags concurrently
    $ python flags.py 30 -s  # download 30 flags sequentially

"""

import sys
import os
import atexit
import time
import contextlib

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from lelo import parallel

COUNTRY_CODES = '''
    AD AE AF AG AL AM AO AR AT AU AZ BA BB BD BE BF BG BH BI BJ BN BO BR
    BS BT BW BY BZ CA CD CF CG CH CI CL CM CN CO CR CU CV CY CZ DE DJ DK
    DM DZ EC EE EG ER ES ET FI FJ FM FR GA GB GD GE GH GM GN GQ GR GT GW
    GY HN HR HT HU ID IE IL IN IQ IR IS IT JM JO JP KE KG KH KI KM KN KP
    KR KW KZ LA LB LC LI LK LR LS LT LU LV LY MA MC MD ME MG MH MK ML MM
    MN MR MT MU MV MW MX MY MZ NA NE NG NI NL NO NP NR NZ OM PA PE PG PH
    PK PL PT PW PY QA RO RS RU RW SA SB SC SD SE SG SI SK SL SM SN SO SR
    SS ST SV SY SZ TD TG TH TJ TL TM TN TO TR TT TV TW TZ UA UG US UY UZ
    VA VC VE VN VU WS YE ZA ZM ZW'''.split()

BASE_URL = '''http://python.pro.br/fluent/data/flags/'''
DOWNLOAD_DIR = 'flag-img/'
DEFAULT_QTY = 10


@parallel
def fetch(url):
    print('Fetching: ' + url)
    local_path = os.path.join(DOWNLOAD_DIR, url.split('/')[-1])
    with contextlib.closing(urlopen(url)) as remote:
        img = remote.read()
    with open(local_path, 'wb') as local:
        local.write(img)
    print('Saved: ' + local_path)


def main(qty_flags):
    if not os.path.exists(DOWNLOAD_DIR):
        print('Creating {!r} directory'.format(DOWNLOAD_DIR))
        os.mkdir(DOWNLOAD_DIR)

    print('Downloading {} flags...'.format(qty_flags))
    for cc in COUNTRY_CODES[:qty_flags]:
        url = BASE_URL + cc.lower() + '.gif'
        fetch(url)

    print('Finished requesting {} downloads.'.format(qty_flags))


@atexit.register
def report():
    # XXX: in Python 3 this is called after all child processes
    # are done, but in Python 2 right after the main process is
    # done, and before most children are completed.
    elapsed = time.time() - start_time
    print('Total time: {:.3}s'.format(elapsed))


if __name__ == '__main__':
    if '-s' in sys.argv:  # sequential download option
        sys.argv.remove('-s')
        fetch = fetch.func  # remove decorator
    try:
        qty_flags = int(sys.argv[1])
    except IndexError:
        qty_flags = DEFAULT_QTY

    start_time = time.time()
    main(qty_flags)
