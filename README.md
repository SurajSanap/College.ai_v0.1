# College.ai

College.ai is a versatile project that harnesses the power of ChatGPT-4 to provide a range of features. The application includes functionalities such as exploring ChatGPT-4 features, training/uploading PDFs, resume analysis, and more.

## Table of Contents
- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to College.ai, your comprehensive solution for exploring the capabilities of ChatGPT-4! This project offers a variety of features, including a Home page, an About section, Ask_To_PDF functionality for training/uploading PDFs, Resume_Analyser for analyzing resumes, ATS for matching job descriptions and resumes, and examples for prompting in Ask to PDF.

## Dependencies

Make sure you have the following dependencies installed:

- [Streamlit](https://streamlit.io/)
- [google-generativeai](https://github.com/googleapis/python-generators)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [langchain](https://github.com/lukasschwab/langchain)
- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [faiss-cpu](https://github.com/facebookresearch/faiss)
- [langchain_google_genai](https://github.com/googleapis/python-generators)
- [pdf2image](https://github.com/Belval/pdf2image)
- [poppler-utils](https://poppler.freedesktop.org/)
- [streamlit_lottie](https://github.com/okld/streamlit-lottie)

You can install them using the following:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SurajSanap/College.ai_v0.1.git
```

2. Navigate to the project directory:

```bash
cd College.ai_v0.1
```

## Getting Started

To start the application, run the following command:

```bash
streamlit run home.py
```

This will launch the College.ai application in your default web browser.

## Folder Structure

- **Pages/**
  - `home.py`: Home page with an introduction to College.ai.
  - `About.py`: Information about the creator and other details.
  - `Ask_To_PDF.py`: Functionality to train/upload PDFs and make queries.
  - `Resume_Analyser.py`: Analyze resumes and provide recommendations.
  - `ATS.py`: Match job descriptions with resumes and show feedback.
  - `Prompt_Examples.py`: Examples for prompting in Ask to PDF.

## Contributing

If you'd like to contribute to College.ai, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.