import gradio as gr
import requests

def generate_text(prompt):
    url = "http://{private IPv4}:8080/completion"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "n_predict": 256
    }
    print(prompt)
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return response.json().get('content')


iface = gr.Interface(
    fn=generate_text,
    # inputs=[
    #     gr.Textbox(label="Prompt"),
    #     gr.Slider(0.0, 2.0, value=0.0, label="Temperature"),
    #     gr.Slider(0.0, 1.0, value=0.95, label="Top P"),
    #     gr.Slider(1, 1000, value=256, step=1, label="Max Tokens"),
    #     gr.Dropdown(
    #         choices=["default"] + list(lora_configs.keys()),
    #         label="Model Type",
    #         value="default"
    #     ),
    # ],
    inputs="text",
    outputs="text",
    title="Model Demo",
    description="Enter a prompt to generate text using the fine-tuned model.",
    # live=True
    # api_name = "generate"
)

# iface.launch(server_name="0.0.0.0", server_port=7870)
iface.launch(server_name="0.0.0.0")
