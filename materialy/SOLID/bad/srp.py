"""
	Klasa Circle z dwiema odpowiedzialnosciami
"""

import math


class Circle:
	def __init__(self, radius=0, color="red"):
		self.radius = radius
		self.color = color

	def draw(self):
		"""Draws a rectangle"""
		pass

	def get_area(self):
		"""Counts the area"""
		return math.pi * self.radius**2
