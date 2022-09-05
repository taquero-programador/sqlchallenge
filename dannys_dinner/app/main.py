#!/usr/bin/env python3

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
