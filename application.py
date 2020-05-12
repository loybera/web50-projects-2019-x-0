#!/usr/bin/python

from flask import Flask, g, render_template, jsonify, url_for, flash
from flask import request, redirect, make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (MetaData, Table, Column,
                        Integer, String, Sequence,
                        create_engine,
                        insert)
from functools import wraps
#from databaseFinal_setup import Base, Signo, User
import string
import json
import datetime


app = Flask(__name__)

 



# Connect to Database and create database session
#engine = create_engine('postgresql://anita:anita@localhost/moduloastrologia')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind=engine)
session = DBSession()

		
@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

		
if __name__ == '__main__':
	app.secret_key = "secret key"
	app.debug = True
	app.run(host = '0.0.0.0', port = 8081)
	

