# Mail Merge ✉️

This is a simple Python project that automates the process of creating personalized letters by performing a **Mail Merge**.\
It replaces a placeholder in a letter template with names from a text file and saves individual letters for each person.

---

## 📂 Project Structure

```
Input/
├── Letters/
│   └── starting_letter.txt         # Template with placeholder [name]
├── Names/
│   └── invited_names.txt           # List of names (one per line)

Output/
└── ReadyToSend/
    └── Saurabh.txt                 # Example of a generated letter

main.py                             # Python script for mail merge
README.md                           # Project documentation
```

---

## 🛠️ How It Works

1. Reads the list of names from `invited_names.txt`.
2. Loads the letter template from `starting_letter.txt`.
3. Replaces `[name]` with each actual name.
4. Generates a separate `.txt` letter for each person in the `Output/ReadyToSend/` folder.

---

## 📅 Input Files

### `Input/Letters/starting_letter.txt`

```
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela
```

### `Input/Names/invited_names.txt`

```
Saurabh
Aman
Riya
```

---

## ✅ Output Example

### `Output/ReadyToSend/Saurabh.txt`

```
Dear Saurabh,

You are invited to my birthday this Saturday.

Hope you can make it!

Angela
```

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3.x).

2. Place your names and template in the correct folders as shown above.

3. Run the script using:

   ```bash
   python main.py
   ```

4. Check the `Output/ReadyToSend/` folder for personalized letters.

---

## 🔓 License

This project is free to use, modify, and distribute.

---

## 💡 Author

**Saurabh Kulshrestha**

---

⭐ *Star this project if it helped you!*

