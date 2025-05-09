from abc import ABC, abstractmethod

from httpapifoundation.event_bus.type_enum import EventBusEventType


class AbstractEventBus(ABC):

    @abstractmethod
    def publish(self, event_type: EventBusEventType, event_data: dict):
        pass
