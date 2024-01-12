import os
import sys
import subprocess as sp

def run():
	command = os.path.join(os.path.dirname(__file__), "..", "quarto", "bin", "quarto")
	sp.call([command] + sys.argv)
