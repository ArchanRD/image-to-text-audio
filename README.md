
## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

To run this project you need to setup a virtual environment and install few python packages.


1. **Clone the Repository:**

   ```sh
   git clone https://github.com/ArchanRD/image-to-text-audio
   cd cloned-repository

1. **Setup virtual environment:**
- For ubuntu or macOS
```bash
  python3 -m venv myvenv
  source myvenv/bin/activate
```

- For windows
```bash
  python -m venv myvenv
  source myvenv\Scripts\activate
```

3. **Install packages**
After setting up virtual environment, you need to install below mentioned python packages into the virtual environment.

```bash
  pip install dotenv
  pip install transformers
  pip install tensorflow==2.16
  pip install tf-keras
  pip install streamlit
```

4. **Run using streamlit**
To run the program using a web interface, run

```bash
  streamlit run app.py
```

## Add environemnt variables
1. **Log in to Hugging Face**
- Open your web browser and go to [Hugging Face](https://huggingface.co/)
- Log in using your credentials. If you don't have an account, sign up for one.

2. **Generate an Access Token:**
- Once logged in, navigate to the [Tokens Settings](https://huggingface.co/settings/tokens) page.
- Click on the "New token" button.
- Provide a name for the token (e.g., my-read-token).
- Select the "Read" permission from the options.
- Click the "Generate" button to create the token.
- Copy the generated token. Keep it secure and do not share it publicly.

3. **Create a .env File:**
- In the .env file, add the following line:
  ```bash
  HUGGINGFACEHUB_API_TOKEN=your_generated_token_here
  ```
- Replace your_generated_token_here with the actual token you copied in step 2.
