
# Web Services and Applications – Assignments 2025  
**Author:** Finian Doonan  

## Module Overview  
This module introduces learners to the design and development of web services and applications using Python. The focus is on interacting with APIs, handling HTTP requests, retrieving online data, and automating tasks involving web-based systems.

---

## Learning Outcomes  
On successful completion of this module, learners will be able to:

1. **Interact with web APIs using HTTP requests**  
   - Send and receive data from RESTful services.

2. **Retrieve, process, and store data from online services**  
   - Work with live data sources and save them locally.

3. **Work with JSON data formats**  
   - Parse and manipulate structured data returned from APIs.

4. **Automate tasks involving web-based platforms**  
   - Develop scripts to perform repetitive web interactions.

---

## Contents – Assignments

| Assignment | Filename | Description |
|------------|---------|-------------|
| 2 | `assignment2-carddraw.py` | Draw 5 cards using an API and evaluate the hand. |
| 3 | `assignment03-cso.ipynb` | Retrieve CSO dataset and save as JSON. |
| 4 | `assignment04-github.py` | Modify file in GitHub repo and push changes. |

---

## Assignment Details

### Assignment 2 – Card Draw API  
**Filename:** `assignment2-carddraw.py`  

**Description:**  
- Use the Deck of Cards API to simulate dealing a hand of 5 cards.  
- Shuffle a deck and retrieve a `deck_id`.  
- Draw 5 cards and print their value and suit.  

**Bonus (Final Marks):**  
- Check if the hand contains:
  - Pair  
  - Three of a kind  
  - Straight  
  - Flush  
- Print a congratulatory message if detected.  


---

### Assignment 3 – CSO Data Retrieval  
**Filename:** `assignment03-cso.ipynb`  

**Description:**  
- Retrieve the dataset: *Exchequer Account (Historical Series)* from CSO.ie.  
- Save the dataset locally as `cso.json`.  

**Requirements:**  
- Keep the program short (~10 lines).  
- No need to analyse or reformat the data.  

**Tips:**  
- Use `requests` to fetch the data.  
- Save using Python file handling (`open`, `write`).  

---

### Assignment 4 – GitHub File Modification  
**Filename:** `assignment04-github.py`  

**Description:**  
- Read a file from a GitHub repository.  
- Replace all instances of `"Andrew"` with your name.  
- Commit and push the updated file back to the repository.  

**Requirements:**  
- Authentication is required (do not include keys).  
- Code should be functional and clearly structured.  

**Comment:**  
This program uses a GitHub Personal Access Token (stored in config.py) to securely connect to a GitHub repository. It reads a file from the repository, replaces all occurrences of the name “Andrew” with “Finian”, and then commits and pushes the updated file back to GitHub. The config.py file is added to .gitignore to ensure the token is not uploaded to GitHub for security reasons. 


---

## References & Resources  

**APIs & Web Services**  
- [Deck of Cards API](https://deckofcardsapi.com/)  
- [CSO Website](https://www.cso.ie/)  

**Python & HTTP Requests**  
- [Requests Library Documentation](https://docs.python-requests.org/)  
- [Real Python – APIs](https://realpython.com/api-integration-in-python/)  

**GitHub Integration**  
- [GitHub REST API](https://docs.github.com/en/rest)  
- [PyGithub Documentation](https://pygithub.readthedocs.io/)  
