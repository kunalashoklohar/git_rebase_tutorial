import os
import logging
#add basic config here
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w',
                    level=logging.NOTSET)
logging.debug("First Debug")                   
