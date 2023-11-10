try:
    print(5/0)
# catch any exception
except Exception as e:
    print(f"Exception: {e}")
else:
    print("No exception occurred")

print("normal code block")