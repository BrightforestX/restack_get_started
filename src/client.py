import os
from restack_ai import Restack
from restack_ai.restack import CloudConnectionOptions
from dotenv import load_dotenv

load_dotenv()

connection_options = CloudConnectionOptions(
    engine_id=os.getenv('RESTACK_ENGINE_ID'),
    address=os.getenv('RESTACK_ENGINE_ADDRESS'),
    api_key=os.getenv('RESTACK_ENGINE_API_KEY')
)

client = Restack(connection_options)