import os
print("rls")
input("")
os.system("pip install flask")
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
  returt("server hackd")

