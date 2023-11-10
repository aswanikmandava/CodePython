from dotenv import load_dotenv
import os

load_dotenv()

secret_name = os.getenv('SECRET_NAME')
secret_value = os.getenv('SECRET_VALUE')

if __name__ == "__main__":
    print(f"name: {secret_name}, val: {secret_value}")