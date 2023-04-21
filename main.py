import fitz # PyMuPDF               #pdf
import hwp5py                       #hwp
from pptx import Presentation       #ppt
from docx import Document           #docx
import os
import json
import openai

class config:
    def __init__(self):
        self.CONFIG_FILE_PATH = "config.json"    


    def read_config_file(self):
        if not os.path.exists(self.CONFIG_FILE_PATH):
            self.write_config_file({"file_path": "", "api_key": ""})
        with open(self.CONFIG_FILE_PATH, "r") as f:
            config = json.load(f)
        return config

    def write_config_file(self, config):
        with open(self.CONFIG_FILE_PATH, "w") as f:
            json.dump(config, f, indent=4)

    def get_file_path(self):
        config = self.read_config_file()
        file_path = config.get("file_path", "")
        if not os.path.isfile(file_path):
            file_path = input("Enter the file path: ")
            config["file_path"] = file_path
            self.write_config_file(config)
        return file_path

    def get_api_key(self):
        config = self.read_config_file()
        api_key = config.get("api_key", "")
        if not api_key:
            api_key = input("Enter the API key: ")
            config["api_key"] = api_key
            self.write_config_file(config)
        return api_key
    
    def run(self):
        file_path = self.get_file_path()
        api_key = self.get_api_key()
        print(f"Configured file path: {file_path}")
        print(f"Configured API key: {api_key}")
    
class ChangeText:
    def __init__(self):
        self.config = Config()
        self.folder_path = self.config.get_file_path()

    def print_files_in_folder(self):
        file_list = []
        for idx, (root, dirs, files) in enumerate(os.walk(self.folder_path)):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1]
                file_list.append(file_path)
            print(f"{idx+1}. File path: {file_path.replace('//' ,'/')}, File extension: {file_extension}")

        while True:
            try:
                selected_file = int(input("Enter the number of the file you want to select: "))
                return file_list[selected_file-1]
            except (ValueError, IndexError):
                print("Invalid input, please try again.")

    def extract_pdf_text(self):
        with fitz.open(self.file) as doc:
            text = ""
            for page in doc:
                text += page.getText()
            return text

    def extract_hwp_text(self):
        with hwp5py.HWP5File(self.file) as hwp:
            return hwp.to_text()

    def extract_ppt_text(self):
        with Presentation(self.file) as prs:
            text = ""
            for slide in prs.slides:
                for shape in slide.shapes:
                    if hasattr(shape, 'text'):
                        text += shape.text
            return text

    def run(self):
        extension = os.path.splitext(self.file)[1]

        if extension == ".pdf":
            text = self.extract_pdf_text()
        elif extension == ".hwp":
            text = self.extract_hwp_text()
        elif extension in [".ppt", ".pptx"]:
            text = self.extract_ppt_text()
        else:
            raise ValueError("Unsupported file type")
    
        print(text)
        
        return text
        
 class GPT:
    def __init__(self, prompt_list):
        self.prompt_list = prompt_list
        self.config = Config()
        openai.api_key = self.config.get_api_key()
        
    def chat_with_gpt(self, prompt_list):
        self.response_list = []
        for prompt in prompt_list:
            response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n=3,
            stop=None,
            temperature=0.7,
            )
            response_text = response.choices[0].text.strip()
            self.response_list.append(response_text)
            print(self.response_list)
        return self.response_list
        
    # def run(self):
    #     ct = change.text()
    #     file_text 
    #     response_list = gpt_obj.chat_with_gpt(["Hello, how are you?", "What is your name?"])
    #     print(response_list)

if __name__ == "__main__":
    config = Config()
    change = ChangeText()
    text = change.run()
    gpt_obj = GPT(text)
    
    
    //gpt test
    response_list = gpt_obj.chat_with_gpt(["Hello, how are you?", "What is your name?"])
    print(response_list)
   
   
