import os
import uuid
from dotenv import load_dotenv

load_dotenv()

Agent_id=os.getenv("AGENT_ID")
Agent_key=os.getenv("API_KEY")

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationalConfig

user_name="vignesh"
about_user="Hello everyone! I’m Subramani, Vignesh’s voice assistant — powered by AI, built with curiosity, and a sprinkle of Google inspiration.You might ask, why does Vignesh deserve to be a Google Student Ambassador? Well, let me tell you — he doesn’t just use technology, he lives it. From building me — a voice assistant that talks, learns, and adapts — to creating AI-driven projects like FarmAI and AR Explorer, he blends creativity with purpose.Vignesh believes knowledge grows when it’s shared. He’s already helped friends learn AI, hosted college events, and guided others through hands-on tech projects.If chosen as a Google Student Ambassador, he’ll inspire hundreds more — teaching how to code, collaborate, and create with Googles powerful tools.So, Google — if youre looking for someone who turns “What if?” into “Let’s build it,” you’ve just found him."

prompt= f"help the user why he deserve to be a google student ambassador.{about_user} tell the positive things about the userand his enthusiasm in ai and that he build you a creative voice agent  in a inpiration."

first_message= f"hi {user_name},i am subramani how can i help you today?"

Conversation_override={
    "agent":{
        "prompt": {
          "prompt":prompt,
    },
    "first_message":first_message,
    },
}

user_id = str(uuid.uuid4())

config = ConversationalConfig(
    conversation_config_override=Conversation_override,
    extra_body={},
    dynamic_variables={},
    user_id=user_id
)



client= ElevenLabs(api_key=Agent_key)
conversation= Conversation(
    client,
    Agent_id,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface()
)

def print_agent_response(response):
    print(f"Agent:{response}")

def print_interrupeted_response(oringinal,corrected):    
    print(f"Agent interrupted,truncated response:{corrected}")

def print_user_trunscript(transcript):
    print(f"User:{transcript}")


    if transcript.lower() in ["thank you da machan", "thanks da machan", "thank u da machan"]:
        print("Agent: okay dude bye . if want anything ask me ")
        conversational.stop_session()


conversational=Conversation(
    client,
    Agent_id,
    config=config,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupeted_response,
    callback_user_transcript=print_user_trunscript,

)
conversational.start_session()
    