import gradio as gr

def greet(name):
    return f"Hello, {name} — welcome to Hugging Face Spaces!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs=gr.Textbox(label="Greeting")
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
