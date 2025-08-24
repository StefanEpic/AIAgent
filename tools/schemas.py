from typing import List

from pydantic import BaseModel, Field


class EmployeeForInfoList(BaseModel):
    """Данные о сотруднике для Листа ознакомления."""
    name: str = Field(description="Фамилия Имя Отчество")
    job_title: str = Field(description="Название должности")
    baza: str = Field(description="Топливная база")


class EmployeeForOrderB(BaseModel):
    """Данные о сотруднике для Приказа Б."""
    surname: str = Field(description="Фамилия")
    name: str = Field(description="Имя")
    patronymic: str = Field(description="Отчество")
    number: str = Field(description="Табельный номер")
    dates_of_training: List[str] = Field(description="Даты обучения сотрудника")
    knowledge_test_date: str = Field(description="Дата проверки знаний сотрудника")
