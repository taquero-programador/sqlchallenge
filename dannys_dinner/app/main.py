#!/usr/bin/env python3

import models as md
from database import SessionLocal, engine

md.Base.metadata.create_all(bind=engine)
