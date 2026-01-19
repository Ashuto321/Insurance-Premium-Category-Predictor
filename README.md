<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Insurance Premium Category Predictor</title>
    <style>
        body {
            font-family: "Segoe UI", Roboto, Arial, sans-serif;
            background-color: #f4f6f9;
            color: #333;
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            background: #ffffff;
            padding: 40px;
        }

        h1, h2, h3 {
            color: #1f4fbf;
        }

        h1 {
            font-size: 38px;
        }

        h2 {
            margin-top: 50px;
            border-bottom: 2px solid #eaeaea;
            padding-bottom: 10px;
        }

        p {
            font-size: 16px;
        }

        ul {
            margin-left: 25px;
        }

        li {
            margin-bottom: 8px;
        }

        .badge {
            display: inline-block;
            padding: 6px 14px;
            border-radius: 20px;
            background: #1f4fbf;
            color: white;
            font-size: 13px;
            margin-right: 6px;
        }

        .card {
            background: #f8f9fb;
            border-radius: 12px;
            padding: 25px;
            margin-top: 25px;
        }

        .workflow {
            background: #0f172a;
            color: #e5e7eb;
            padding: 25px;
            border-radius: 12px;
            font-family: monospace;
            font-size: 15px;
            margin-top: 20px;
        }

        .highlight {
            background: #eef3ff;
            padding: 12px;
            border-left: 4px solid #1f4fbf;
            margin: 20px 0;
        }

        .footer {
            text-align: center;
            margin-top: 60px;
            color: #777;
            font-size: 14px;
        }

        img {
            max-width: 100%;
            border-radius: 12px;
            margin-top: 15px;
        }

        .tech-stack span {
            background: #e9ecff;
            color: #1f4fbf;
            padding: 8px 14px;
            border-radius: 20px;
            margin: 6px;
            display: inline-block;
            font-size: 14px;
        }
    </style>
</head>

<body>
<div class="container">

    <h1>🛡️ Insurance Premium Category Predictor</h1>
    <p>
        A <strong>production-ready Machine Learning application</strong> that predicts
        the <strong>insurance premium category</strong> of a user based on demographic,
        lifestyle, and financial factors.
    </p>

    <span class="badge">Machine Learning</span>
    <span class="badge">FastAPI</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Random Forest</span>

    <div class="highlight">
        🚀 This project demonstrates an <strong>end-to-end ML pipeline</strong> —
        from model training to real-time inference using a modern API + UI stack.
    </div>

    <!-- PROJECT OVERVIEW -->
    <h2>📌 Project Overview</h2>
    <p>
        Insurance premium calculation is a complex decision-making process influenced
        by multiple factors such as age, income, occupation, health habits, and location.
        This project uses a <strong>Random Forest classification model</strong>
        to intelligently categorize users into premium classes like <em>Low</em>,
        <em>Medium</em>, or <em>High</em>.
    </p>

    <p>
        The trained model is exposed via a <strong>FastAPI backend</strong> and consumed
        through an interactive <strong>Streamlit frontend</strong>.
    </p>

    <!-- TECH STACK -->
    <h2>⚙️ Technology Stack</h2>
    <div class="tech-stack">
        <span>Python</span>
        <span>scikit-learn</span>
        <span>Random Forest Classifier</span>
        <span>FastAPI</span>
        <span>Pydantic</span>
        <span>Streamlit</span>
        <span>Pickle</span>
        <span>REST API</span>
    </div>

    <!-- ML WORKFLOW -->
    <h2>🧠 Machine Learning Workflow</h2>
    <div class="card">
        <ul>
            <li>📊 Data preprocessing and feature engineering</li>
            <li>🧮 Categorical encoding using OneHotEncoder</li>
            <li>🌲 Model training using Random Forest Classifier</li>
            <li>📈 Model evaluation and validation</li>
            <li>💾 Model persistence using Pickle</li>
        </ul>
    </div>

    <!-- SYSTEM ARCHITECTURE -->
    <h2>🔁 End-to-End System Architecture</h2>
    <div class="workflow">
        User Input (Streamlit UI)
                ↓
        REST API Request (JSON)
                ↓
        FastAPI Backend
        (Pydantic Validation)
                ↓
        Preprocessing Pipeline
                ↓
        Random Forest Model
                ↓
        Prediction + Confidence
                ↓
        JSON Response
                ↓
        Streamlit Visualization
    </div>

    <!-- FASTAPI -->
    <h2>🚀 FastAPI Backend</h2>
    <div class="card">
        <ul>
            <li>Strict request validation using <strong>Pydantic models</strong></li>
            <li>Serialized Random Forest model loaded using <strong>pickle</strong></li>
            <li>RESTful <code>/predict</code> endpoint</li>
            <li>Returns prediction, confidence score & class probabilities</li>
            <li>Swagger documentation enabled</li>
        </ul>
    </div>

    <!-- STREAMLIT -->
    <h2>🎨 Streamlit Frontend</h2>
    <div class="card">
        <ul>
            <li>User-friendly input form</li>
            <li>Live API integration</li>
            <li>Confidence metrics & probability visualization</li>
            <li>Professional dashboard layout</li>
        </ul>
    </div>

    <!-- OUTPUT -->
    <h2>📊 Output Preview</h2>
    <p>
        Below is a sample prediction response generated by the system:
    </p>

    <div class="workflow">
{
  "predicted_category": "Medium",
  "confidence": 0.87,
  "class_probabilities": {
    "Low": 0.08,
    "Medium": 0.87,
    "High": 0.05
  }
}
    </div>

    <!-- PLACEHOLDER FOR IMAGES -->
    <h3>🖼️ Application Screenshots</h3>
    <p>(Add screenshots here)</p>
    <!--
    <img src="images/streamlit_ui.png" alt="Streamlit UI">
    <img src="images/api_docs.png" alt="FastAPI Docs">
    -->

    <!-- WHY THIS PROJECT -->
    <h2>🌟 Why This Project Stands Out</h2>
    <div class="card">
        <ul>
            <li>✔ Real-world ML deployment</li>
            <li>✔ Clean separation of model, API, and UI</li>
            <li>✔ Scalable architecture</li>
            <li>✔ Production-ready validation & error handling</li>
        </ul>
    </div>

    <div class="footer">
        © 2026 • Insurance Premium Category Predictor<br>
        Built with ❤️ using Machine Learning, FastAPI & Streamlit
    </div>

</div>
</body>
</html>
