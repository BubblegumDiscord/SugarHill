import pymongo
from Crypto.Cipher import XOR
import base64, os, sys, json
key = os.environ.get('CONFIG_KEY')
if not key:
    print("Please set an environment variable of CONFIG_KEY=thekey and restart")
    sys.exit(1)

def getMongoUri():
    def encrypt(key, plaintext):
        cipher = XOR.new(key)
        return base64.b64encode(cipher.encrypt(plaintext))

    def decrypt(key, ciphertext):
        cipher = XOR.new(key)
        return cipher.decrypt(base64.b64decode(ciphertext))
    ciphert = b'Xh0XXhoAFVhKRAheXg5GWgsaAElRHBgGFkcdEnlEShMASwERQ1xIUVBeUVlKD14YABRaHA=='

    plaint = decrypt(key, ciphert).decode("utf8")
    return plaint

uri = getMongoUri()
client = pymongo.MongoClient(uri)
db = client.sugarhill
configColl = db.config
config = configColl.find_one({
})
if not config:
    print("Could not see the 'Config' collection")
    sys.exit(2)
config.pop("_id")
with open("./config.json", "w") as f:
    f.write(json.dumps(config))