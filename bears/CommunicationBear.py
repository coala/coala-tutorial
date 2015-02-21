from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result


class CommunicationBear(LocalBear):
    def run(self,
            filename,
            file,
            user_input: str):
        """
        Communicates with the user.

        :param user_input: Arbitrary user input.
        """
        self.debug_msg("Got '{ui}' as user input of type {type}.".format(
            ui=user_input,
            type=type(user_input)))

        return [Result(message="A hello world result.",
                       origin=self.__class__.__name__,
                       file=filename)]
