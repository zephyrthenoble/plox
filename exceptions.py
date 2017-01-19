### Exceptions ###
hadError = False
def exception(line, message):
    report(message, line)
def report(message, line, where=""):
    err("[line %d] Error %s: %s" % (message, line, where))
    hadError = True
#######
