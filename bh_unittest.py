import asyncio
from time import time
import unittest
import binaryheap
from datetime import datetime

#unit testing for 5 encode
class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( binaryheap.encode('us'), '..- ...')

    def test_encode_fy(self):
        self.assertEqual( binaryheap.encode('FY'), '..-. -.--')

    def test_encode_uwe(self):
        self.assertEqual( binaryheap.encode('UWE'), '..- .-- .')

    #fail test 1
    def test_encode_fail(self):
        self.assertEqual( binaryheap.encode('FAIL'), '..... ---')

    #fail test 2
    def test_encode_fail2(self):
        self.assertEqual( binaryheap.encode('FAIL2'), '..... ---')

    #unit testing for 5 decode
    def test_decode_us(self):
        self.assertEqual( binaryheap.encode('..- ...'), 'US')

    def test_decode_us(self):
        self.assertEqual( binaryheap.encode('.. --- -'), 'IOT')

    def test_decode_us(self):
        self.assertEqual( binaryheap.encode('..- .-- .'), 'UWE')

    def test_decode_us(self):
        self.assertEqual( binaryheap.encode('.-.. --- .-..'), 'LOL')

    #fail test 3
    def test_decode_us(self):
        self.assertEqual( binaryheap.encode('..... .. .. ....'), 'FAIL3')

    # Task 4 Testing
    def test_encode_task4(self):
        self.assertEqual(binaryheap.encode('(+&,:"!)'), '-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-')

    def test_decode_task4(self):
        self.assertEqual(binaryheap.decode('-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-'), '(+&,:"!)')

    # Other tests
    # Test tree
    def test_isTreeEmpty(self):
        self.assertEqual(binaryheap.checkIsEmpty(), False)

    def test_isTreeNotEmpty(self):
        self.assertEqual(binaryheap.checkIsNotEmpty(), True)

    # Test insertion
    def test_insert_false(self):
        self.assertEqual(binaryheap.insert('E'), False)

    def test_insert_true(self):
        self.assertEqual(binaryheap.insert('choo'), True)

    # Tests Deletion
    def test_delete_true(self):
        self.assertEqual(binaryheap.delete('E'), True)

    def test_delete_false(self):
        self.assertEqual(binaryheap.delete('choo'), False)

    def test_delete_fail(self):
        self.assertEqual(binaryheap.delete('choo'), True)

    # Test Search
    def test_find_true(self):
        self.assertEqual(binaryheap.find('E'), True)

    def test_find_false(self):
        self.assertEqual(binaryheap.find('choo'), False)

    def test_find_fail(self):
        self.assertEqual(binaryheap.find('choo'), True)

    # Testing Part 2 Task 1 
    def test_decode_bt_pass(self):
       self.assertEqual(binaryheap.decode_bt('..- ...'), 'us')

    def test_decode_bt_fail(self):
        self.assertEqual(binaryheap.decode_bt('... ...'), 'fail')

    # Testing Part 2 Task 2
    def test_decode_ham1(self):
        self.assertEqual(binaryheap.decode_ham('.. --- - -.. . ..-. -.-- -...- ..- ... -...- -.--.'), ['fy', 'iot', 'us'])

    def test_decode_ham2(self):
        self.assertEqual(binaryheap.decode_ham('.-. .---- -.. . ... .---- -...- -.-. .... --- --- -...- -.--.'), ['s2', 'r2', 'choo'])

    def test_encode_ham1(self):
       self.assertEqual(binaryheap.encode_ham('s1', 'r1', 'us'), '.-. .---- -.. . ... .---- -...- ..- ... -...- -.--.')

    def test_encode_ham2(self):
       self.assertEqual(binaryheap.encode_ham('fy', 'iot', 'us'), '.. --- - -.. . ..-. -.-- -...- ..- ... -...- -.--.')

    def test_send_echo(self):
       self.assertEqual(asyncio.run(binaryheap.send_echo('fy', 'yo')), 'FYDEECHO=YO=(')

    def test_send_time(self):
        now = datetime.now()
        self.assertEqual(asyncio.run(binaryheap.send_time('s')), 'SDETIME=' + now.strftime("%H:%M:%S") + '=(')

if __name__ == '__main__':
    unittest.main()
