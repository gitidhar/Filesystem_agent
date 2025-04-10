from initial_setups import create_client

response = create_client().responses.create(
    model="gpt-4o",
    input="Name three fruits grown in Asia"
)

print(response.output_text)
