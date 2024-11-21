import traceback
import time
import sys

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
        # get the exception type, value and traceback object
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traces = traceback.extract_tb(exc_traceback)
        print("Type of Traceback         : ", type(traces))
        # format the trackback data
        print("%50s | %10s | %5s | %10s" %("File Name", "Method Name", "Line Number", "Line"))
        print("-"*100)
        for frame_summary in traces:
            print("%50s | %11s | %11d | %10s"%(frame_summary.filename, frame_summary.name, frame_summary.lineno, frame_summary.line))
            print("-"*100)