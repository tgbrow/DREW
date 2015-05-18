from PyQt5.QtCore import pyqtSignal, QThread
from constants import *

class PauseChangeThread(QThread):
	isDone = False
	doneSignal = pyqtSignal()
	action = RESUME

	def __init__(self, systemState):
		super().__init__()
		self.systemState = systemState

	def setAction(self, action):
		self.action = action

	def run(self):
		self.isDone = False
		self.systemState.setSystemPause(self.action)
		self.doneSignal.emit()
		self.isDone = True