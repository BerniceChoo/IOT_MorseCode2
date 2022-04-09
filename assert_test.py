import binaryheap

def test_encode_us():
    assert binaryheap.encode('us') == '..- ...', "should be ..- ..."


if __name__ == "__main__":
    assert binaryheap.encode('us') == '..- ...', "Should be ..- ..."
    print('everything passed')

