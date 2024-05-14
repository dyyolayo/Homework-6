#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:59:15 2024

@author: user2
"""

def make_change(total):
    
    """Given an amount, between 0 and 100, this function produces a list
    of the potential coin combinations that could be made from that number"""
    coins = [1, 5, 10, 25, 100]

    ucombos = set()

    def combinations(amount, current_combo):

        if amount == 0:
            ucombos.add(tuple(sorted(current_combo)))
            return

        for coin in coins:
            if coin <= amount:
                combinations(amount - coin, current_combo + [coin])

    combinations(total, [])

    all_combinations = [list(combo) for combo in ucombos]

    return all_combinations


def dict_filter(function, dic):
    """Takes in a function and a dictionary and produces a new
    dictionary where a given key and value remain associated with each other 
    in the new dictionary, if and only if the function returns True when 
    called with the key and the value. """

    empty = {}
    for key,val in dic.items():
        if function(key,val):
            empty[key] = val
    
    return empty


class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)


def treemap(fun,tree):
    """takes function and tree, returns a mod version of tree
    that changes value of each child based on function"""
    
    tree.key,tree.value = fun(tree.key,tree.value)
    for child in tree.childen:
        treemap(fun, child)


class DTree:
    def __init__(self,variable,threshold,lessequal,greater,outcome):
        if (variable is not None and threshold is not None and lessequal is not None
            and greater is not None) is not (outcome is None):
            raise ValueError
            
        self.variable = variable
        self.threshold = threshold
        self.lessequal= lessequal
        self.greater = greater
        self.outcome = outcome


    def tuple_atleast(self):
            """determines necessary entries that should exist in a tuple"""
            
            high = 0
            if self.lessequal:
                high = (high,self.lessequal.tuple_atleast())
            if self.greater:
                high = (high,self.greater.tuple_atleast())
            if self.varuable is not None:
                high = (high,self.variable + 1)

            return high


    def find_outcome(self,obs):
            """takes in a tuple with observations and navigates through the tree 
            to provide the outcome that matches (like “walk”) """
            
            if self.outcome is not None:
                return self.outcome
            
            value = obs(self.variable)
        
            if value <= self.threshold:
                return self.lessequal.find_outcome(obs)
            else:
                return self.greater.find_outcome(obs)


    def no_repeats(self):
            """True iff there are no repeats, False otherwise"""
            
            def helper(node, lv = None):
                if node is None:
                    return True
                if node.variable == lv:
                    return False
                return helper(node.lessequal, node.variable) and helper(node.greater,node.variable)
                
            return helper(self)
        
        