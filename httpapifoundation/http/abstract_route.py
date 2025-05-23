from abc import abstractmethod

from httpapifoundation.http.meta_route import MetaRoute
from httpapifoundation.http.route_details import RouteDetails
from httpapifoundation.http.user_claims import UserClaims


class AbstractHttpRoute(metaclass=MetaRoute):

    details: RouteDetails | None = None

    def __init__(self):
        self.user_claims: UserClaims | None = None

    @abstractmethod
    async def callback(self, **kwargs):
        pass

    async def endpoint(self, **kwargs):
        self._validate()
        return await self.callback(**kwargs)

    def _validate(self):
        if self.user_claims is None:
            raise Exception("User claims are not set")
