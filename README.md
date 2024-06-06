
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
