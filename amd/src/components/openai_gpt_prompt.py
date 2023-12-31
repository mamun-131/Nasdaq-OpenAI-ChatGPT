# -*- coding: utf-8 -*-
"""
Created on 2023-11-16

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
import openai 
import json
import utils as common
from src.exception import CustomException
from src.logger import logging
openai.api_key = common.get_openai_key()


class OpenAIGptPrompt:
    def __int__(self):
        self

    #Openai Chatgpt API call     
    def chatgpt_prompt(self,user_query, instruction):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": user_query},

                ],
                temperature=0,
                top_p=0.1
            )
        except Exception as e:
            logging.info("Failed to gpt response.")
            raise CustomException(e,sys)
    
        data = json.loads(response.json())
        logging.info("GPT Raw Response: " + str(response))
        return data['choices'][0]['message']['content']
        