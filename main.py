import os
import logging
#add basic config here
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',
                    level=logging.NOTSET)
logging.debug("Harmless debug Message")
logging.info("Just an information")
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down") 
logging.info("I added this line while resolving the rebase/merge conflict")                 
