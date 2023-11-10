def custom_name(func):
    def wrapper(*args, **kwargs):
        # capitalize each input
        fname = kwargs.get('fname', '').capitalize()
        lname = kwargs.get('lname', '').capitalize()

        result = func(*args, fname=fname, lname=lname)
        return result + " is a senior SWE"
    return wrapper



@custom_name
def getname(id, fname=None, lname=None):
    full_name = ""
    if not fname:
        full_name += "Unknown "
    else:
        full_name += fname + " "
    if not lname:
        full_name += "Unknown"
    else:
        full_name += lname
    return str(id) + ": " + full_name


print(getname(20, fname='aswani', lname='mandava'))