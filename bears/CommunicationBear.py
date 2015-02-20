from coalib.bears.LocalBear import LocalBear


class CommunicationBear(LocalBear):
    def run_bear(self,
                 filename,
                 file,
                 user_input: str):
        self.debug_msg("Got '{ui}' as user input of type {type}.".format(
            ui=user_input,
            type=type(user_input)))
