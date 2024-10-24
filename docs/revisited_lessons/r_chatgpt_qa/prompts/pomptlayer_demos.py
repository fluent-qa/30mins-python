import promptlayer
import os

anthropic = promptlayer.anthropic
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

completion = client.completions.create(
    prompt=f'{anthropic.HUMAN_PROMPT} Which NHL team plays in Pittsburgh?{anthropic.AI_PROMPT}',
    model='claude-2',
    max_tokens_to_sample=300,
)

print(completion)
print(completion.completion)

completion = client.messages.create(
    messages=[
        {
            'content': 'How many toes do dogs have?',
            'role': 'user',
        },
    ],
    temperature=0.0,
    system='Respond only in Yoda-speak',
    model='claude-3-haiku-20240307',
    max_tokens=256,
    pl_tags=['animal-toes']
)
print()
print(completion)
print()
print(completion.content[0].text)
print()

import os
import promptlayer
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

"""
Prompt templates are customizable prompt strings with placeholders for variables.
"""

assistant_type = promptlayer.prompts.get('assistant_type')

# You can also optionally pass version to get an older version of a prompt.
# By default, the newest version of a prompt is returned.
# assistant_type = promptlayer.prompts.get('assistant_type', version=1)

variables = {
    'type': 'english'
}

assistant_type_template = assistant_type['messages'][0]['prompt']['template']

content = assistant_type_template.format(**variables)

response, pl_request_id = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[
        {'role': 'system', 'content': content},
        {'role': 'user', 'content': 'What is HTML?'}
    ],
    return_pl_id=True
)

answer = response.choices[0].message.content
print(answer)

# Associate request with a prompt template
promptlayer.track.prompt(
    request_id=pl_request_id,
    prompt_name='assistant_type',
    prompt_input_variables=variables
)

# Attach multiple key value pairs as metadata to a request
# Using the PromptLayer UI you can search for specific metadata
promptlayer.track.metadata(
    request_id=pl_request_id,
    metadata={
        'client_type': 'browser',
        'request_date': '2023-11-07',
        'username': 'ian',
    }
)
