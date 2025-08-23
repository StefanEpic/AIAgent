from pydantic import BaseModel, Field


class Employee(BaseModel):
    """Данные о сотруднике."""
    name: str = Field(description="Фамилия имя Отчество")
    job_title: str = Field(description="Название должности")
    baza: str = Field(description="Топливная база")
