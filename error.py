from io import err
### Exceptions ###
hadError = False
def exception(line, message):
    report(message, line)
def report(line, message, where=""):
    err("[line %d] Error %s: %s\n" % (line, message, where))
    hadError = True
#######
