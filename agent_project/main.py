from initial_setups import create_client 
from crawler import activate_crawler, shutdown

example_url = "https://soundcloud.com"

crawler, browser = activate_crawler(example_url, False)
input("Press Enter to close the browser...") # debug

shutdown(crawler, browser)

# playwright codegen https://soundcloud.com --target python

# OPEN_AI API Code:

# response = create_client().responses.create(
#     model="gpt-4o",
#     input="Name three fruits grown in Asia"
# )

# print(response.output_text)

