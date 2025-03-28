# YL-360 Initiative Chatbot

This is an AI-powered chatbot for the YL-360 Initiative by Unisole that uses a text file for storing and retrieving information about the program, company, and students.

## Features

- Easily updateable through a simple text file
- Retrieves relevant information using vector search
- Welcomes students to the YL-360 Initiative
- Provides information about the program, company, and founder
- Lists students in the program and their project interests
- Maintains conversation history for meaningful interactions
- Includes an admin panel to update information without editing code

## Setup Instructions

### 1. Create Your Project Directory

```bash
mkdir yl360-chatbot
cd yl360-chatbot
```

### 2. Create the Required Files

1. Create `app.py` by copying the code from the "Updated App with Text File Loading" artifact
2. Create `requirements.txt` by copying the content from the updated requirements
3. Create `yl360_info.txt` by copying the content from the "YL-360 Initiative Information" artifact
4. Create `.env` with your API keys:

```
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=GENAIAPP
HF_TOKEN=your_huggingface_token
LANGSMITH_API_KEY=your_langsmith_api_key
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
GROQ_API_KEY=your_groq_api_key
```

### 3. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application Locally

```bash
streamlit run app.py
```

## Updating Information

You can update the information in two ways:

1. **Using the Admin Panel:**
   - Open the sidebar in the Streamlit app
   - Click "Edit Information"
   - Update the text as needed
   - Click "Save Changes"

2. **Editing the File Directly:**
   - Open `yl360_info.txt` in any text editor
   - Make your changes
   - Save the file
   - Restart the application

## Free Deployment Options

### 1. Streamlit Cloud (Recommended)

1. Create a GitHub repository and push your code
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Sign in with your GitHub account
4. Deploy your app by selecting the repository
5. Add your secrets (API keys) in the Streamlit dashboard

### 2. Hugging Face Spaces

1. Create an account on [https://huggingface.co/](https://huggingface.co/)
2. Create a new Space (select Streamlit)
3. Upload your code or connect to GitHub repository
4. Add your secrets (API keys) in the Space settings

### 3. Render (Free Tier)

1. Create an account on [https://render.com/](https://render.com/)
2. Create a new Web Service
3. Connect to your GitHub repository
4. Add environment variables (API keys) in the dashboard
5. Set the build command to `pip install -r requirements.txt`
6. Set the start command to `streamlit run app.py`

## Structure of the Information File

The information file (`yl360_info.txt`) is structured in Markdown format with sections for:

- Program Details
- Key Features
- Company Information
- Achievements
- Founder Information
- Current Students (with details for each)
- Additional sections as needed

You can edit this file to add new students, update information, or add entirely new sections.

## Customization

You can customize the chatbot by:

1. Modifying the system prompt in `app.py` to change the chatbot's personality
2. Adjusting the text splitting parameters for better information retrieval
3. Adding more sections to the information file for richer responses

## Troubleshooting

If you encounter issues:

1. Check if all API keys are correctly set in the environment variables
2. Ensure the `yl360_info.txt` file exists and is properly formatted
3. Verify that all dependencies are installed correctly
4. Check the logs on your deployment platform for any errors

## Contact

For any questions or support, please contact Ajay Mokta at ajay@unisole.com
