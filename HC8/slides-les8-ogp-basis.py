from counter import Counter

def main():
    teller = Counter()
    print(teller.getValue())
    teller.click()
    teller.click()
    print(teller.getValue())

    nogEenTeller = Counter()
    nogEenTeller.click()
    print(teller.getValue(), nogEenTeller.getValue())
    teller.reset()
    print(teller.getValue(), nogEenTeller.getValue())

    eenDerdeTeller = nogEenTeller
    print(nogEenTeller.getValue(),eenDerdeTeller.getValue())
    eenDerdeTeller.click()
    print(nogEenTeller.getValue(), eenDerdeTeller.getValue())

main()

