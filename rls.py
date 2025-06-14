import os
print("rls")
input("")
os.system("pip install flask")
from flask import Flask
app = Flask
@app.route('/')
def main():
  returt("server hackd")

