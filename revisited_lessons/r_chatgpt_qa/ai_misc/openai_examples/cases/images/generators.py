from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
#   model="dall-e-2",
  prompt="Painting of a red farmhouse with a tree in a peaceful valley with a stream and mountains in the background",
  size="1024x1024",
  quality="standard",
  n=1,
#   n=2,
)

image_url = response.data[0].url
# image_url_2 = response.data[1].url

print(image_url)
# print()
# print(image_url_2)
response = client.images.create_variation(
    image=open('./bucky.png', 'rb'), # input must be a square PNG image, less than 4mb in size
    n=1,
    size='1024x1024'
)

image_url = response.data[0].url
print(image_url)
