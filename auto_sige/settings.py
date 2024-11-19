from dotenv import load_dotenv
import os

load_dotenv()

cpf = os.getenv("CPF")
password = os.getenv("PASSWORD")
print(cpf, password)
