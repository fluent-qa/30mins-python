from promptlayer import PromptLayer

promptlayer_client = PromptLayer()

# Swap out 'from anthropic import Anthropic'
Anthropic = promptlayer_client.anthropic.Anthropic

anthropic = Anthropic()
completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
    prompt=f"{anthropic.HUMAN_PROMPT} Compose a poem please.{anthropic.AI_PROMPT}",
    pl_tags=["getting-started"],
)
print(completion.completion)
