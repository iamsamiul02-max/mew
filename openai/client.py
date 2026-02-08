"""OpenAI client implementation."""

from openai.resources.responses import Responses


class OpenAI:
    """Main OpenAI client class."""
    
    def __init__(self, api_key=None):
        """Initialize the OpenAI client.
        
        Args:
            api_key: Optional API key for authentication.
        """
        self.api_key = api_key
        self.responses = Responses(self)
