import logging

from httpapifoundation.http.abstract import AbstractHttp
from httpapifoundation.http.meta_route import MetaRoute
from httpapifoundation.injector import Injector


_logger = logging.getLogger(__name__)


class Bootstrapper:
    def __init__(self):
        self.http: AbstractHttp | None = None

    def bootstrap(self):
        self.http = Injector().inject(AbstractHttp)

        self.http.bootstrap()
        for route in MetaRoute.routes:  # FIXME are we sure we want MetaRoute to hold routes ?
            _logger.info(
                f"Registering HTTP route '{route.__name__}' "
                f"for path '{route.details.path}' "
                f"and method '{route.details.method}'"
            )
            self.http.register_route(route)
