import logging
'''logging level: 1.debug 2.info 3.warning 4.error 5.critical'''
"getLogger-define log name"

logA=logging.getLogger("this is AAAAA {}".format(__name__))
logB=logging.getLogger("this is BBBB {}".format(__name__))
logging.basicConfig(level=logging.INFO,format='%(asctime)s:[%(levelname)s]:[%(name)s]:[%(module)s]:%(message)s') #filename="c:/1/log.log"
# log.setLevel(logging.INFO)
try:
    logA.info('We Will try to divide by 0')
    logB.warning("now presenting logB")
    t=1/0
except Exception,e :
    logA.error(str(e))


'''Handling'''
logger = logging.getLogger('this is:%s' %__name__) # create logger
logger.setLevel(logging.DEBUG) #set level
handler = logging.StreamHandler() # create console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # create formatter
handler.setFormatter(formatter) # add formatter to handler
logger.addHandler(handler) # add handler to logger
logger.debug('This is logging message') # print log

