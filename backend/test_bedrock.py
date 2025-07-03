from aws_bedrock import initialize_bedrock_client, invoke_bedrock_model

# Step 1: Initialize the Bedrock client
print("Initializing Bedrock client...")
client = initialize_bedrock_client()
print("Bedrock client initialized.")

# Step 2: Get user input manual
user_prompt = input("Asistana Sor: ")

# Step 3: Invoke the Bedrock model with the user input
print("Invoking Bedrock model...")
response = invoke_bedrock_model(client, user_prompt)
print("Bedrock model invoked.")

# Step 4: Print the response from the model
print(f"Response from Bedrock model: {response}")
