# nexforz-projects
# Contact Manager (Python)

A simple **Contact Manager application** built using **Python** and **Pickle**.  
This program lets you **add**, **view**, and **delete** contacts — all saved in a binary file for persistence.  

---

## Features

- Add new contacts with validation  
- View all saved contacts  
- Delete existing contacts  
- Store data permanently using the `pickle` module  

---

## How to Run

### 1. Prerequisites
Make sure you have **Python 3** installed on your system.  

#Menu Options

Once you run the program, you’ll see:

1. Create new contact
2. View contact
3. Delete contact
4. Exit

#My Learning Journey

The biggest challenge I faced was validating user input — especially phone numbers and email addresses.
At first, users could enter invalid emails (like uppercase or missing @) or short numbers, causing errors later.

I solved this by learning and implementing regular expressions (regex) to validate both:

-Phone numbers must start with 6–9 and be 10 digits long.

-Emails must contain only lowercase letters and follow a format like example@gmail.com.

Through this, I learned the importance of data validation and error handling in user-facing programs.

| Tool            | Purpose                                           |
| ----------------| --------------------------------------------------|
|  **Python 3**   | Programming language                              |
|  **Pickle**     | File handling & data storage                      |
|  **re (Regex)** | Input validation                                  |
| **os**          | File operations (delete, rename, check existence) |

#Example output
1. create new contact
2. view contact
3. delete contact
4. exit

enter your choice: 1
Enter the name: Arshad
Type the phone number: 9876543210
Email: arshad123@gmail.com
Contact added successfully!
