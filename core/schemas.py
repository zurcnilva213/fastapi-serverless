from pydantic import BaseModel, validator


class DefaultModel(BaseModel):
    @validator("*", pre=True)
    def not_none(cls, v, field):
        if all((
            getattr(field, "default", None) is not None,
            v is None,
        )):
            return field.default
        else:
            return v
