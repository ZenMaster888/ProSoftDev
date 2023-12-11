# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:17:48 2023

@author: bilsk
"""

class Validator:
    
    def validate_numbers(self list_for_validation): 
        """
        Contains an error, missing comma 
        after self
        """

     
      
        validated_numbers = []

        for i in list_for_validation:
            
            try:
                number = int(i)
                if number > 0:
                    validated_numbers.append(number)
            except ValueError:
                pass
                

        return validated_numbers

