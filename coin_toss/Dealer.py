#! /usr/bin/python3
import random

class Dealer:
	def __init__(self,prob,hand):
		self.hit_prob = prob
		self.hand = hand

	def toss(self,bet):
		coin_is_hit = random.random()<self.hit_prob
		if coin_is_hit:
			self.hand += bet
			return bet
		else:
			self.hand -= bet
			return -bet
	
	def get_hand(self):
		return self.hand
