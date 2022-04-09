import binaryheap

if __name__ == "__main__":
    e = binaryheap.encode('us')
    print('%s' % e)
    d = binaryheap.decode('lol')
    print('%s' % d)

    assert binaryheap.encode('us') == '..- ...', "Should be ..-"
    assert binaryheap.encode('FY') == '..-. -.--', "Should be ..-"
    assert binaryheap.encode('UWE') == '..- .-- .', "Should be ..-"
    assert binaryheap.encode('FAIL') == '..... ---', "Should be ..-"
    assert binaryheap.encode('FAIL2') == '..... ---', "Should be ..-"

    assert binaryheap.decode('..- ...') == 'US', "Should be ..-"
    assert binaryheap.decode('.. --- -') == 'IOT', "Should be ..-"
    assert binaryheap.decode('..- .-- .') == 'UWE', "Should be ..-"
    assert binaryheap.decode('.-.. --- .-..') == 'LOL', "Should be ..-"
    assert binaryheap.decode('..... .. .. ....') == 'FAIL3', "Should be ..-"