"""Response object models."""


class Response:
    """Response object returned by the API."""
    
    def __init__(self, output_text, input_text=None, model=None):
        """Initialize a Response object.
        
        Args:
            output_text: The generated output text.
            input_text: The input text provided.
            model: The model used for generation.
        """
        self.output_text = output_text
        self.input_text = input_text
        self.model = model
