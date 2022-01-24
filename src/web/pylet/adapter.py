from typing import TypeVar, Generic

from .model import Model
from .view import View

M = TypeVar('M', bound=Model)
V = TypeVar('V', bound=View)


class Adapter(Generic[M, V]):
    """
    This is the Adapter in the Model-View-Adapter pattern.
    An adapter is bound to a specific type of Model and is responsible
    for building a specific type of View.
    Always ensure Adapter subclasses call `super().__init__()` last in
    their `__init__` function. This is because `super` will invoke the
    `build_view()` method on the subclass, so this allows other subclass
    fields to be initialized before that.
    """

    def __init__(self, model: M = None):
        self._model = model
        self._view = self.build_view()

    @property
    def model(self) -> M:
        return self._model

    @property
    def view(self) -> V:
        return self._view

    def build_view(self) -> V:
        raise NotImplementedError()
