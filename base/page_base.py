import abc

from base.base_functions import Base


class PageBase(Base):
    __metaclass__ = abc.ABCMeta  # ADDED

    def __init__(self, driver):
        super(PageBase, self).__init__(driver)
        self.driver = driver

    @abc.abstractmethod
    def check(self):
        raise NotImplementedError("Not implemented yet.")

