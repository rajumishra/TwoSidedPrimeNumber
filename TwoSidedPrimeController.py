from flask import Flask
app = Flask(__name__)


@app.route('/number/<number>')
def checkTwoSidedPrime(number):
    for i in range(0,len(number)+1):
        tempNumber = number[0:i]
        if(isPrime(tempNumber) == False):
            return 'False'
        tempNumber = number[i:len(number)+1]
        if (isPrime(tempNumber) == False):
            return 'False'
    return 'True'


def isPrime(tempNumber):
    if tempNumber.strip():
        number = int(tempNumber)
        if number <= 1:
            return False
        for i in range(2, number//2):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    app.run()