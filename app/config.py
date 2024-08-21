import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://christianvirdo_sit722_part1_user:AFyr6BrSN0U2j05hMAHfz0ZkoJINinAH@dpg-cr2uef88fa8c73c2cnhg-a.oregon-postgres.render.com/christianvirdo_sit722_part1")

settings = Settings()
