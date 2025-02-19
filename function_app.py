import azure.functions as func
import json
import openai
import logging

AZURE_OPENAI_KEY = "X"
AZURE_OPENAI_ENDPOINT = "https://sknir-m765z46u-eastus2.cognitiveservices.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "gpt-4-deployment"  
AZURE_OPENAI_VERSION = "2024-08-01-preview"

client = openai.AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=AZURE_OPENAI_VERSION
)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="SummarizedDataAPI")
@app.route(route="summarize", auth_level=func.AuthLevel.ANONYMOUS)
def summarize(req: func.HttpRequest) -> func.HttpResponse:
    """Handles HTTP requests and returns AI-generated summaries."""
    logging.info("Received request for summarization.")

    try:
        req_body = req.get_json()
        text = req_body.get("text")

        if not text:
            return func.HttpResponse(
                json.dumps({"error": "Text field is required."}),
                status_code=400,
                mimetype="application/json"
            )

        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[{"role": "user", "content": f"Summarize this: {text}"}],
            max_tokens=50
        )

        summary = response.choices[0].message.content

        return func.HttpResponse(
            json.dumps({"summary": summary}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error in summarization: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


