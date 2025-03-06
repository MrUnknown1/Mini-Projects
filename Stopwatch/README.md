# Stopwatch Application

A simple **Stopwatch Application** built using **PyQt5**. It provides basic stopwatch functionality, including **Start, Stop, and Reset** buttons, with a clean and modern UI.

---

## **🚀 Features**
- ⏱ **Start, Stop, and Reset** functionality
- 🎨 **Modern UI with Styled Buttons & Labels**
- 🎯 **High Precision (Updates Every 10ms)**
- 🖥 **Fixed Window Size (600x400px)**
- 📌 **Hover Effects for Buttons**

---

## **📦 Installation**

### **1️⃣ Install PyQt5**
Ensure you have PyQt5 installed. If not, install it using pip:
```sh
pip install PyQt5
```

### **2️⃣ Copy the code in your code editor**

### **3️⃣ Run the Application**
```sh
python stopwatch.py
```

---

## **🛠 How It Works**
- **Start**: Begins the stopwatch counting time in HH:MM:SS.ms format.
- **Stop**: Pauses the stopwatch.
- **Reset**: Resets the time back to `00:00:00.00`.

---

## **📜 Code Overview**
- Uses `QTimer` to update time every **10ms**.
- `QTime` object stores elapsed time.
- `QLabel` displays time in a readable format.
- `QPushButton` handles user interactions.

---

## **🎨 UI Design**
- **Time Label**: Large, centered, and visually appealing.
- **Buttons**: Rounded edges with hover effects.
- **Color Theme**: Cool blue tones for a professional look.

---

## **📌 Future Enhancements**
✅ Add a **Lap Timer** feature.
✅ Implement **Dark Mode** toggle.
✅ Provide **Custom Font Selection**.

---

