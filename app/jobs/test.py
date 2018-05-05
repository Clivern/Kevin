"""
Test Job
"""

from app.modules.util.helpers import Helpers
from app.jobs.base import Base

class Test(Base):

    def execute(self):
        self._logger.debug(self._arguments["text"] if "text" in self._arguments else "Text not in arguments")
        return True