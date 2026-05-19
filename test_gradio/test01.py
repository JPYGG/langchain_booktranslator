import gradio as gr


def calculator(num1, operation, num2):
    if operation == '加':
        return num1 + num2
    elif operation == '减':
        return num1 - num2
    elif operation == '乘':
        return num1 * num2
    elif operation == '除':
        if num2 == 0:
            raise gr.Error("除数不能为0")
        return num1 / num2
    return None


instance = gr.Interface(
    fn=calculator,
    inputs=[
        'number',
        gr.Radio(choices=['加', '减', '乘', '除'], label='计算法则'),
        'number'
    ],
    outputs='number'
)

instance.launch(server_name='0.0.0.0', server_port=18008, auth=('admin', 'admin'))
