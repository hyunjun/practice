#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from pydantic import BaseModel


#   https://fastapi.tiangolo.com/tutorial/body/
class Todo(BaseModel):
    id: int
    item: str

