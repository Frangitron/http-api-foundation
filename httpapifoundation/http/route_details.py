from dataclasses import dataclass

from httpapifoundation.http.method_enum import HttpMethod


@dataclass()
class RouteDetails:
    method: HttpMethod
    name: str
    operation_id: str
    path: str
