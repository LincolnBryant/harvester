"""
utilities

"""

import sys
import time
import random
import inspect
import traceback

from pandalogger.LogWrapper import LogWrapper


# make logger
def makeLogger(tmpLog,token=None):
    # get method name of caller
    tmpStr = inspect.stack()[1][3]
    if token != None:
        tmpStr += ' <{0}>'.format(token)
    else:
        tmpStr += ' :'.format(token)
    newLog = LogWrapper(tmpLog,tmpStr)
    return newLog

                        

# dump error message                                                                          
def dumpErrorMessage(tmpLog,errStr=None):
    if not isinstance(tmpLog,LogWrapper):
        methodName = '{0} : '.format(inspect.stack()[1][3])
    else:
        methodName = ''
    # error
    if errStr == None:
        errtype,errvalue = sys.exc_info()[:2]
        errStr = "{0} {1} {2}".format(methodName,errtype.__name__,errvalue)
        errStr.strip()
        errStr += traceback.format_exc()
    tmpLog.error(errStr)



# sleep for randome duration
def sleep(interval):
    time.sleep(random.randint(int(interval*0.8),int(interval*1.2)))
