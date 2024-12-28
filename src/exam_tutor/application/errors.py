from exam_tutor.domain.error import Error


class ApplicationError(Error): ...


class DoesNotExistError(ApplicationError): ...


class NotCreated(ApplicationError): ...
