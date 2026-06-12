# fraud detection engine using hashset and frequency maps

class PaymentObject():
    def __init__(self, key):
        self.person = key[0]
        self.TransactionID = key[1]
        self.accountNumber = key[2]
        self.timestamp = key[3]
        self.amount = key[4]
        
class FraudDetect():
    def __init__(self):
        self.set = {}
        self.counter = 0
        