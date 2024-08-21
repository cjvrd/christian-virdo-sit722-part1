import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://christian_virdo_sit722_part1_user:jCv9Zumy1QDVTVHI0w7vxlBTKuSGEHZI@dpg-cr2u2u88fa8c73c27q90-a.singapore-postgres.render.com/christian_virdo_sit722_part1")

settings = Settings()
