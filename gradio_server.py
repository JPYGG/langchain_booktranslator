import gradio as gr

from ai_model.openai_model import OpenAIModel
from translator.book_translator import PDFTranslator
from utils.project_config import ProjectConfig

def translation(input_file, source_language, target_language):
    output_file = translator.translate_book(file_path=input_file, source_language=source_language, target_language=target_language)
    return output_file


def init_translator():
    # 项目整体配置的初始化
    config = ProjectConfig()
    config.initialize()

    # 初始化大语言模型
    if config.model_type == 'OpenAIModel':
        model = OpenAIModel(config.model_name, config.api_key, config.base_url)
    else:
        # model = ChatGLMModel(config.model_name, config.api_key)
        pass
    global translator
    # 初始化一个翻译器
    translator = PDFTranslator(model)

def run_gradio():
    """
    启动gradio
    :return:
    """
    instance = gr.Interface(
        fn=translation, #调用翻译书籍的函数
        title='自动翻译器 V2.0',
        inputs=[
            gr.File(label='上传PDF书籍文件'),
            gr.Textbox(label='源语言(默认: 英文)', placeholder='English', value='English'),
            gr.Textbox(label='目标语言(默认: 中文)', placeholder='中文', value='中文')
        ],
        outputs=[
            gr.File(label='下载翻译之后的文件')
        ],
        # allow_flagging="never" # 不显示Flag的按钮
    )
    # 启动服务
    instance.launch(server_name='0.0.0.0', server_port=8008)


if __name__ == '__main__':
    init_translator()
    run_gradio()