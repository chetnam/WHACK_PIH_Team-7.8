def isBodyValid(body):
    # body is valid if there are two commas, two strings, 1 integer
    # need to separate body into three things
    try:
        validCommas = (body.count(',')==2)
        
        int((splitBody(body))['amount'])
        return validCommas
    except ValueError:
        return False

# returns dictionary with order message split into location_id, sku, amountItem
def splitBody(body):
    message = body.replace(' ','').split(',')
    messageDict = {"location_id":message[0],"SKU":message[1],"amount":message[2]}
    return messageDict
