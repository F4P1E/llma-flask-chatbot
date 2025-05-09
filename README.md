# 🧘‍♀️ LLaMA Flask Chatbot – Digital Wellness Assistant

This is a Flask-based AI chatbot powered by Meta's **LLaMA 4 Scout 17B Instruct** model, designed to help users improve their **digital wellness**. It provides thoughtful and empathetic responses on topics like screen time, mental health, productivity, and emotional balance.

---

## 🚀 Features

- 🤖 AI-powered digital wellness chat using LLaMA 4 Scout
- 🧠 System prompt customization for personality and tone
- 📦 Dockerized for easy deployment
- 🛡️ .env support for Hugging Face token


## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/F4P1E/llma-flask-chatbot.git
cd llma-flask-chatbot
````

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Hugging Face Token

Create a `.env` file:

```env
HUGGINGFACE_TOKEN=your_hf_token_here
```

### 4. Run Flask App

```bash
python app/main.py
```

---

## 🐳 Docker Usage

### Build the Docker image:

```bash
docker build -t llama-chatbot .
```

### Run the container:

```bash
docker run -p 5000:5000 --env-file .env llama-chatbot
```

---

## 📬 API Endpoint

**POST /chat**

Send a JSON request:

```json
{ "prompt": "How can I reduce screen time before bed?" }
```

Response:

```json
{ "response": "Try setting a device curfew..." }
```

---

## 🤝 Credits

* Model: [Meta LLaMA 4 Scout](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct)
* Backend: Flask
* Containerization: Docker

---

## 📄 License

MIT – free to use and adapt.

```

---

Would you like to add badges (e.g., Docker, Python, Hugging Face) or a usage GIF to the README?
```
