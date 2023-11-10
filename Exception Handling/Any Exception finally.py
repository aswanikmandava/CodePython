try:
    print(5/0)
# catch any exception
except Exception as e:
    print(f"Exception: {e}")
finally:
    print("I always run")

print("normal code block")