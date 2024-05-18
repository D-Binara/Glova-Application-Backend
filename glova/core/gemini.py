import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv(".env")


class Solution(object):
    def __init__(self, skinType : str, skinTone : str) -> None:
        genai.configure(api_key="AIzaSyDzWH1iqE9S3kg1L-IS-en9CgEoD08lcow")

        generation_config={
                        'temperature':0.01, 
                        'max_output_tokens': 300
                    }
        
        safety_settings=[
            {
                "category": "HARM_CATEGORY_DANGEROUS",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        
        self._model = genai.GenerativeModel('gemini-pro-vision')
        
        self._prompt=f"Please identify the this skin disease and make a daily routing for avoid this disease on {skinType} and {skinTone}"
        
        
          
                        
        
    def geminiResponse(self, image : str) -> str:
        try:
            self._response=self._model.generate_content([self._prompt, image], stream=False)
                
            for chunk in self._response:
                self._response_ = ''.join(chunk.text) 
            
            #print(self._response_)
            return self._response_
        except:
            return False
            
            
            
        

    







