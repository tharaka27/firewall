def get_answer():
    """Get an answer."""
    return True


def getIpAddress(array):
    s = ''
    for i in array:
        s = s + str(int(i, 16)) + '.'
    return s[:len(s)-1]
    
def getPort(s):
    i = s[0] + s[1]
    return str(int(i, 16))


def isSrc(myaddress, address):
    for i in range(len(myaddress)):
        if(myaddress[i] != address[i]):
            return False
    return True



'''
print(isIncoming(['f8','34','41','21','87','7a'],['f8','34','41','21','87','7a'])) #Print true
print(isIncoming(['f8','34','41','21','87','7a'],['f8','34','41','21','87','7'])) #Print False
'''
