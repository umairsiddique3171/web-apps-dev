import gradio as gr

def greet(name):
    return "Hello, " + name + "!" 

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=3,placeholder="Enter text here...."),
    outputs="text",
)

demo.launch()
