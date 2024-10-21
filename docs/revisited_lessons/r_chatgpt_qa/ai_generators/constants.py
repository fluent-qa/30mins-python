from pydantic import BaseModel


# `https://api.cloudflare.com/client/v4/accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1`;
# model: mistral
#
# 1. sent prompt
# 2. getting result
# messages = [
#     {role: "system", content: "You are a helpful assistant."},
#     {role: "user", content: prompt},
# ];

# vibe == = "Casual" ? "relaxed": vibe == = "Funny" ? "silly": "Professional"

class BioPrompt(BaseModel):
    vibe: str
