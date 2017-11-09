
import os
import unittest
from models import Base, Book, Author, Publisher, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_source_insert_1(self):
        s = Book(id='1', title = 'TESTONE')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '1').one()
        self.assertEqual(str(r.id), '1')

        session.query(Book).filter_by(id = '1').delete()
        session.commit()
		
    def test_source_insert_2(self):
        s = Book(id='2', title = 'TESTTWO')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')

        session.query(Book).filter_by(id = '2').delete()
        session.commit()
		
    def test_source_insert_3(self):
        s = Book(id='3', title = 'TESTTHREE')
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(id = '3').one()
        self.assertEqual(str(r.id), '3')

        session.query(Book).filter_by(id = '3').delete()
        session.commit()
		
    def test_source_insert_4(self):
        s = Author(id='1', name = 'TESTONE')
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(id = '1').one()
        self.assertEqual(str(r.id), '1')

        session.query(Author).filter_by(id = '1').delete()
        session.commit()
		
    def test_source_insert_5(self):
        s = Author(id='2', name = 'TESTTWO')
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')

        session.query(Author).filter_by(id = '2').delete()
        session.commit()
		
    def test_source_insert_6(self):
        s = Author(id='3', name = 'TESTTHREE')
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(id = '3').one()
        self.assertEqual(str(r.id), '3')

        session.query(Author).filter_by(id = '3').delete()
        session.commit()
		
    def test_source_insert_7(self):
        s = Publisher(id='1', name = 'TESTONE')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(id = '1').one()
        self.assertEqual(str(r.id), '1')

        session.query(Publisher).filter_by(id = '1').delete()
        session.commit()
		
    def test_source_insert_8(self):
        s = Publisher(id='2', name = 'TESTTWO')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(id = '2').one()
        self.assertEqual(str(r.id), '2')

        session.query(Publisher).filter_by(id = '2').delete()
        session.commit()
		
    def test_source_insert_9(self):
        s = Publisher(id='3', name = 'TESTTHREE')
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(id = '3').one()
        self.assertEqual(str(r.id), '3')

        session.query(Publisher).filter_by(id = '3').delete()
        session.commit()
		

if __name__ == '__main__':
	unittest.main()