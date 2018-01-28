import logging

from coalib.bears.LocalBear import LocalBear

class HelloWorldBear(LocalBear):
    def run(self,
            filename,
            file):
        logging.debug("Hello World! Checking file {}.".format(filename))
