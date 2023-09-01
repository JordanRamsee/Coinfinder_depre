from cryptography.fernet import Fernet


    
def key():
    
    '''
    this function is used to generate the key used 
    in encrypting and decrypting the binary data
    '''
    with open('key.txt' , 'rb') as f:
        key = f.read()
        
    return Fernet(key)
    
    
def encrypt(data):
    '''
    this function is used to encrypt the binary data 
    '''
    return key().encrypt(data)


def decrypt(data):
    '''
    this function is used to decrypt the binary data 
    '''
    return key().decrypt(data)