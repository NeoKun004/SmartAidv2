"""
LLM Connector Module for Teacher App

This module provides functionality to connect to and query LLM services (AWS Bedrock)
for generating educational content tailored to students with learning disabilities.
"""

import boto3
import json
import logging
import os
from botocore.config import Config
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMConnector:
    """
    A connector class for interacting with AWS Bedrock LLMs.
    """
    
    def __init__(self, 
                aws_access_key_id: str = None,
                aws_secret_access_key: str = None,
                aws_region: str = 'us-east-1',
                model_id: str = 'anthropic.claude-3-sonnet-20240229-v1:0',
                read_timeout: int = 1000):
        """
        Initialize the LLM connector with AWS credentials and model settings.
        AWS credentials are loaded from environment variables if not provided.
        """
        # Load credentials from environment variables if not provided
        self.aws_access_key_id = aws_access_key_id or os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = aws_secret_access_key or os.getenv('AWS_SECRET_ACCESS_KEY')
        self.aws_region = aws_region
        self.model_id = model_id
        self.config = Config(read_timeout=read_timeout)
        self.client = self._initialize_client()
        
        logger.info(f"Initialized LLM connector with model: {self.model_id}")
    
    def _initialize_client(self):
        """Initialize the AWS Bedrock client."""
        try:
            return boto3.client(
                'bedrock-runtime',
                region_name=self.aws_region,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                config=self.config
            )
        except Exception as e:
            logger.error(f"Failed to initialize AWS Bedrock client: {str(e)}")
            raise
    
    def generate_response(self, 
                            prompt: str, 
                            system_prompt: str = "", 
                            max_tokens: int = 1000, 
                            temperature: float = 0.7) -> str:
            """
            Generate a response from the LLM based on the provided prompt.
            """
            try:
                payload = self._construct_payload(
                    prompt, 
                    system_prompt, 
                    max_tokens, 
                    temperature
                )
                
                logger.info(f"Invoking model {self.model_id} with prompt length: {len(prompt)}")
                logger.info(f"Full payload: {json.dumps(payload)}")
                
                # DEBUG: Set up a temporary fallback for testing the interface
                use_mock = os.getenv('USE_MOCK_RESPONSES', 'False').lower() == 'true'
                if use_mock:
                    logger.info("Using test response instead of API")
                    if "tdah" in prompt.lower():
                        return """Tu montres de bons résultats en mémorisation et en flexibilité cognitive! 🌟 

        Tu as bien retenu les détails de l'histoire et tu as pu t'adapter à de nouvelles consignes. C'est super!

        J'ai remarqué que tu pourrais améliorer ton attention soutenue et ton organisation. Ce sont des compétences que tout le monde peut développer avec un peu de pratique.

        Voici quelques jeux amusants pour t'aider:
        - Joue à "Où est Charlie?" pour entraîner ton attention
        - Essaie des jeux de mémoire avec des cartes
        - Utilise un tableau coloré pour organiser tes tâches quotidiennes

        N'oublie pas: chaque petit effort compte! Ton cerveau est comme un muscle qui devient plus fort à chaque entraînement. Continue comme ça, je suis sûr que tu vas faire des progrès formidables! 🚀"""
                    else:
                        return """Tu as de bonnes compétences en mathématiques! 🌟

        J'ai remarqué que tu comprends bien les additions et que tu peux reconnaître les objets lourds.

        Tu pourrais améliorer ta compréhension des suites logiques. C'est comme comprendre le rythme des nombres qui se suivent!

        Essaie ces jeux amusants:
        - Compte à rebours à partir de 20
        - Cherche des motifs dans les numéros de maisons
        - Utilise des blocs ou des jouets pour visualiser les nombres

        Tu progresses déjà beaucoup, et chaque exercice te rendra encore plus fort en maths! Continue comme ça! 🚀"""
                    
                # Comment this part temporarily if you want to use the test responses above
                response = self.client.invoke_model(
                    modelId=self.model_id,
                    body=json.dumps(payload)
                )
                
                # DEBUG: Display raw response
                logger.info(f"Raw API response: {response}")
                
                response_body = json.loads(response['body'].read())
                logger.info(f"Response body: {response_body}")
                
                result = self._extract_response(response_body)
                
                logger.info(f"Extracted result: {result}")
                logger.info(f"Result length: {len(result) if result else 'None'}")
                
                return result
                    
            except Exception as e:
                logger.error(f"Error generating response: {str(e)}")
                return f"Error: Unable to generate response. {str(e)}"
            
    def _construct_payload(self, 
                          prompt: str, 
                          system_prompt: str, 
                          max_tokens: int, 
                          temperature: float) -> Dict[str, Any]:
        """Construct the payload for the model request."""
        return {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        }
    
    def _extract_response(self, response_body: Dict[str, Any]) -> str:
        """Extract the response text from the model response body."""
        content = response_body.get('content', [])
        if content:
            return content[0]['text']
        return "No response generated."


# Utility function to get a pre-configured LLM connector instance
def get_llm_connector(model_id: str = 'anthropic.claude-3-sonnet-20240229-v1:0') -> LLMConnector:
    """
    Returns a pre-configured LLM connector instance.
    This simplifies getting a connector in solution modules.
    """
    return LLMConnector(model_id=model_id)