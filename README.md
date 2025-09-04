
# 🌌 Space Weather Monitor Application (SWMA)

[![🐍 Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  

**Space Weather Monitor Application (SWMA)** is a full-stack Python-based tool built with **Streamlit** to provide real-time solar and space weather monitoring.

---


## ⚙️ Installation (Using Pip)

1. **Clone the repository**  
    ```bash
    git clone https://github.com/gaurib124/Space-Weather-Monitor-Application.git
    cd Space-Weather-Monitor-Application
    ```

2. **Create and activate a virtual environment**  
    ```bash
    python -m venv env
    # On Windows:
    env\Scripts\activate
    # On Mac/Linux:
    source env/bin/activate
    ```

3. **Install dependencies**  
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

---

## ▶️ Run the Application

```bash
streamlit run swma/swma.py
````

The app will open in your default browser with an interactive sidebar.

---

## 🛰 Available Monitors

| 🌞 Monitor                            | 📖 Description                                     |
| ------------------------------------- | -------------------------------------------------- |
| **Soft X-ray Flux (NOAA-GOES)**       | Real-time solar X-ray flux updates                 |
| **Proton Flux (NOAA-GOES)**           | Proton flux measurements from 1–500 MeV            |
| **Solar Event Probabilities (NOAA)**  | Daily forecasts of solar flares & proton events    |
| **EUV Images (SDO/AIA)**              | Near-real-time solar images in extreme ultraviolet |
| **Coronagraphic Images (SoHO/LASCO)** | White-light views of the solar corona              |

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Data Sources:** NOAA GOES, NASA SDO, SoHO LASCO
* **Core Libraries:** SunPy, AstroPy, Pillow, Matplotlib, Requests
* **Features:** Real-time data, interactive charts, image download

---

## 📦 Key Python Packages

* [SunPy](https://sunpy.org) – Solar data analysis in Python
* [AstroPy](https://www.astropy.org) – Core tools for astronomy & astrophysics

---




