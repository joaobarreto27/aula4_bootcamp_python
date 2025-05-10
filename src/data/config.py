import sys
import os

def configurar_path():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))