import traceback
import time

def myfunc_a(wait_secs):
    print(f"in func A - sleeping for {wait_secs} ...")
    time.sleep(wait_secs)
    return "result-a"


def myfunc_b():
    print("in func B")
    result = myfunc_a(1)
    time.sleep(1)
    print(f"got result: {result}")
    raise ValueError
    print("I won't get here")


if __name__ == '__main__':
    print("Starting program ....")
    try:
        myfunc_b()
    except Exception as e:
        # get traceback and format it as a string
        traceback_str = traceback.format_exc()
        print(f"Caught !!! {traceback_str}")

        # you can get stack trace using logger.exception and logger.error methods
        # logger.exception("Caught error")
        # logger.error("Caught error", exc_info=True)