from initial_setups import create_client 

# OPEN_AI API Code:

response = create_client().responses.create(
    model="gpt-4o",   
    input="Name three fruits grown in Asia"
)

print(response.output_text)