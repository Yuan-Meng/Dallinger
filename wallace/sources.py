from .models import Info, Source
import random


class RandomBinaryStringSource(Source):

    """A source that transmits random binary strings."""

    __mapper_args__ = {"polymorphic_identity": "random_binary_string_source"}

    def create_information(self):
        info = Info(
            origin=self,
            origin_uuid=self.uuid,
            contents=self._binary_string())
        return info

    def _binary_string(self):
        return "".join([str(random.randint(0, 1)) for i in range(2)])
