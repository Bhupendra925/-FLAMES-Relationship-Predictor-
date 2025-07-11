# -FLAMES-Relationship-Predictor-
This project implements the popular childhood game FLAMES using Python, which predicts the relationship between two individuals based on their names.
# 🔥 FLAMES Relationship Predictor

A fun Python-based mini project that predicts the relationship between two people based on the letters in their names using the popular childhood game **FLAMES**.

## 📌 What is FLAMES?

**FLAMES** stands for:
- **F** – Friends  
- **L** – Love  
- **A** – Affection  
- **M** – Marriage  
- **E** – Enemy  
- **S** – Sibling  

This game removes common letters between two names, counts the remaining letters, and uses that number to eliminate letters from the word **FLAMES** in a circular fashion until one remains — revealing your "relationship result."

---

## 🚀 How It Works

1. The user enters their name and their partner's name.
2. All common characters are removed from both names.
3. The total count of remaining letters is calculated.
4. Based on the count, the program performs circular elimination on the `FLAMES` list.
5. The final relationship type is displayed.

---

## 🧠 Concepts Used

- String manipulation
- List operations
- Looping and conditionals
- Modular arithmetic

---

## 🛠️ Requirements

- Python 3.x  
No external libraries are required — this project runs on core Python features only.

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more details.

---

## 🧑‍💻 Author

**[Bhupendra vishwakarma]**  
You can connect with me on [LinkedIn](https://www.linkedin.com/in/bhupendra-vishwakarmaa?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) or check out more projects on [GitHub](https://github.com).

---

## 📷 Demo

## Output 
Enter your name: Alice  
Enter your partner's name: Bob  
Your Relationship is: Love

##📂 Project Structure
bash
Copy
Edit
flames_predictor/
│
├── flames.py         # Main script
├── README.md         # Project description
└── LICENSE           # MIT License

