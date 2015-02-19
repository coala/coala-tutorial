from coalib.bears.LocalBear import LocalBear


class HelloWorldBear(LocalBear):
    def run_bear(self,
                 filename,
                 file):
        self.debug_msg("Hello World! Checking file", filename, ".")
