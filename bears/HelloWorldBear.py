from coalib.bears.LocalBear import LocalBear


class HelloWorldBear(LocalBear):

    def run(self,
            filename,
            file):
        self.debug("Hello World! Checking file", filename, ".")
