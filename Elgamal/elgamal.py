from utils import saveKeys, loadKeys, gcd, modinv
import random
import os
import hashlib


class Elgamal:
    def __init__(self, q, a):
        self.q = q
        self.a = a
        self.X = self.privateKey()['X']
        self.Y = self.pubicKey()['Y']

    def privateKey(self, replace:bool = False):
        # 6339704285463808776231959245308191488039613798101989081223085325101197360426698
        private_Key = {}
        if replace:
            private_Key['X'] = self.X = random.randint(1, self.q-1)
            saveKeys(private_Key, filename='privateKey.txt')
        elif os.path.isfile('privateKey.txt'):
            private_Key = loadKeys(filename='privateKey.txt')
        else:
            private_Key['X'] = self.X = random.randint(1, self.q-1)
            saveKeys(private_Key, filename='privateKey.txt')
        return private_Key # [X]

    def pubicKey(self):
        pubic_Key = {}
        if os.path.isfile('pubicKey.txt'):
            pubic_Key = loadKeys(filename='pubicKey.txt')
        else:
            pubic_Key['q'] = self.q
            pubic_Key['a'] = self.a
            pubic_Key['Y'] = self.Y = pow(self.a, self.X, self.q)
            saveKeys(pubic_Key, filename='pubicKey.txt')
        return pubic_Key # [q, a, y]

    def __encode_md5(self, message):
        message_md5 = hashlib.md5(message.encode()).hexdigest()
        return int(message_md5,16)
    
    def signing(self, message):
        m = self.__encode_md5(message)
        self.K = random.randint(1, self.q-1)
        while gcd(self.K, self.q-1) != 1:
            self.K = random.randint(1, self.q-1)
        
        s1 = pow(self.a, self.K, self.q)
        s2 = modinv(self.K, self.q-1)*(m - self.X*s1)%(self.q-1)
        return s1, s2

    def verifying(self, s1, s2, message):
        m = self.__encode_md5(message)
        v1 = pow(self.a, m, self.q)
        v2 = (pow(self.Y, s1,self.q)*pow(s1,s2,self.q))%self.q
        valid = v1==v2
        return valid



if __name__ == "__main__":
    keys = loadKeys()
    q, a = keys['q'], keys['a']
    encryption = Elgamal(q, a)

    # digital signature
    message = 'hom nay toi vui qua'
    s1, s2 = encryption.signing(message)

    # verify the signature
    valid = encryption.verifying(s1,s2,message)
    print('The signature is valid:',valid)
