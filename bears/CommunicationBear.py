import logging

from coalib.bears.LocalBear import LocalBear

class CommunicationBear(LocalBear):

    def run(self,
            filename,
            file,
            user_input: str):
        """
        Communicates with the user.

        :param user_input: Arbitrary user input.
        """
        logging.debug("Got '{ui}' as user input of type {type}.".format(
            ui=user_input,
            type=type(user_input)))

        yield self.new_result(message="A hello world result.",
                              file=filename)
