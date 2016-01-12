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
        self.debug("Got '{ui}' as user input of type {type}.".format(
            ui=user_input,
            type=type(user_input)))

        return [Result.from_values(message="A hello world result.",
                                   origin=self,
                                   file=filename)]
