import streamlit as st
import boto3
import json

# Define AWS Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")

# Streamlit app layout
st.title('LLama2 Model App')

# Text input for user prompt
user_prompt = st.text_area('Enter your text prompt here:', '')

# Button to trigger model invocation
if st.button('Generate Output'):
    payload = {
        "prompt": user_prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    body = json.dumps(payload)
    model_id = "meta.llama2-70b-chat-v1"
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    generation = response_body['generation']
    st.text('Generated Output:')
    st.write(generation)
