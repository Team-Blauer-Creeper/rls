import os
print("rls")
input("")
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
  returt("server hackd")

