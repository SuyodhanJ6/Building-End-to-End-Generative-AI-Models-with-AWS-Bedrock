import json
import boto3
import base64


bedrock=boto3.client(service_name="bedrock-runtime")



# Define the payload parameters
payload_params = {
    "text_prompts": [{"text": "this is where you place your input text", "weight": 1}],
    "cfg_scale": 10,
    "seed": 0,
    "steps": 50,
    "width": 512,
    "height": 512
}

# Define the payload object
response = {
    "modelId": "stability.stable-diffusion-xl-v0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps(payload_params)  # Serialize the payload parameters to JSON format
}

response_body = json.loads(response.get("body").read())
print(response_body)
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

# Save image to a file in the output directory.
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-img.png"
with open(file_name, "wb") as f:
    f.write(image_bytes)
