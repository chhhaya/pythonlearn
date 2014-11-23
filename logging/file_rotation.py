import glob
import logging
import logging.handlers
import os

LOG_FILENAME = os.path.join('data', 'logging_rotatingfile_example.out')
my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=20, backupCount=5)
my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug('i = %d', i)

logfiles = glob.glob('%s*' % LOG_FILENAME)

for filename in logfiles:
    print(filename)