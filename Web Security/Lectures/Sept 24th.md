

Objectives  
 Understand basic cryptographic principles  
 Understand the fundamentals of encryption  
 Describe the most common ciphers in use today  
 Identify the most common attacks on passwords  
 Use various programs for cracking passwords  
2

Encryption and Password  
Cracking  
 Strong passwords  
Good defense against unwanted entry  
 Guessing, stealing, or cracking passwords  
Foundation of defeating any kind of security

Encryption and Password  
Cracking  
![[Pasted image 20240924114346.png]]
https://spycloud.com/blog/cryptography-of-password-cracking/
  
![[Pasted image 20240924114410.png]]
Encryption and Password  
Cracking  
6  
Entropy as a measure of password strength  
Password strength is specified by the amount of information  
entropy, measured in shannon (Sh) and is a concept from  
Information Theory. It can be regarded as the minimum number  
of bits necessary to hold the information in a password of a  
given type. A related measure is the base-2 logarithm of the  
number of guesses needed to find the password with certainty,  
which is commonly referred to as the "bits of entropy". A  
password with 44 bits of entropy would be as strong as a string  
of 44 bits chosen randomly, for example by a fair coin toss. Put  
another way, a  
password with 44 bits of entropy would require 244 (17,592,186,  
044,416) attempts to exhaust all possibilities during a brute  
force search.  
In one analysis of over 3 million eight-character passwords, the  
letter "e" was used over 1.5 million times, while the letter "f"  
was used only 250,000 times. A uniform distribution would have  
had each character being used about 900,000 times. The most



Cryptography  
9  
The Caesar Cipher, used by Julius Caesar around 58 BC,  
is a substitution cipher that shifts letters in a message to  
make it unreadable if intercepted.

![[Pasted image 20240924114827.png]]


Cryptography  
 The Caesar Cipher is known as a Monoalphabetic  
Substitution due to the simplicity of the encryption method  
 If we use the text ‘Hello’ as our message, and shift the  
letters by 5 characters to the right, we get the encrypted  
message of ‘Mjqqt’  
 Even without the cipherkey it can easily be brute forced  
within 25 attempts, or even guessed.  
 By the 14th century, we started to see the appearance of  
Polyalphabetic Substitution where each plaintext letter can  
be assigned more than one substitute  
 The Vigenère Cipher (16th century) is a method of  
encrypting alphabetic text where each letter of the plaintext  
is encoded with a different Caesar Cipher, whose increment  
is determined by the corresponding letter of another text,  
the key.  
1

Vigenère Cipher  
By combining the message with a key, we can encrypt in a  
way that alters the letter so that repeated letters are  
different  
If we use the text ‘Hello’ as our message, and the key  
being ‘key’, we get the encrypted message of ‘Rijvs’  
1

![[Pasted image 20240924114958.png]]

![[Pasted image 20240924115104.png]]



# Cryptography  



## Vigenère Cipher  

By combining the message with a key, we can encrypt in a  
way that alters the letter so that repeated letters are  
different  
If we use the text ‘Hello’ as our message, and the key  
being ‘key’, we get the encrypted message of ‘Rijvs’  
  
## One Time Pad (OTP)  

• An encryption technique that cannot be cracked, but  
requires the use of a single-use pre-shared key that is  
*larger than* or *equal to the size of the message being  
sent*. In this technique, a plaintext is paired with a  
random secret key (also referred to as a one-time pad).  

The Vigenère Cipher is very similar to this, however there  
is one major difference; The Vigenère cipher *reuses the  
key*, *especially if the ciphertext is longer than the key*,  
which makes it vulnerable to certain attacks. The One-  
Time Pad *uses a key that is as long as the message itself*,  
providing a higher level of security.
  
## Enigma Machine  

 Possibly the most famous substitution cryptography  
machine and used by the German military during World  
War II  
 Roughly equivalent to a *76-bit encryption key*.  

  
## Turing Bombe  

 An electro-mechanical device used by British  
cryptologists to help decipher German Enigma-  
machine-encrypted secret messages during World War  
II.  
  
### Common terms when dealing with cryptography  
>#### Cleartext/Plaintext :
	Unencrypted data  

>Ciphertext :
	Encrypted data  

>Key :
	Information, usually a string of numbers or letters, used to create the encryption and/or decryption process  

>Algorithm :
	The mathematical equation used to scramble/descramble the plain text and make it  
unreadable/readable  

>Encryption :
	Scrambles the original data (cleartext) into an  unreadable format (ciphertext) using an algorithm and a key.
  
>Hash :
	Used to create a fixed-size string of characters (**hash value** or **digest**) from input data of any size. 
>
>The purpose of  hashing is mainly to verify data integrity and to quickly  compare large sets of data.  
  >
>Hashing is a one-way function; it cannot be reversed back  to its original form.  
Ensures data integrity and authenticity but does not  provide confidentiality.  

>## Encryption vs Hashing  
 ####Encryption: 
	 Encryption is commonly used in securing  communications (e.g., HTTPS), protecting sensitive data in databases, and securing files and emails.  
>#### Hashing: 
	Hashing is used for password storage (storing hashed passwords instead of plaintext), digital signatures,  data integrity verification, and in cryptographic protocols.  
>
 While both are cryptographic techniques used to protect  data, encryption focuses on confidentiality and reversible transformation, while hashing focuses on data integrity,  
authenticity, and irreversible transformation.  


---

### Vigenère Cipher

**Overview:** The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It combines the message with a key to alter the letters so that repeated letters in the plaintext are encrypted differently.

**Explanation:**

- **Encryption Process:** Each letter in the plaintext is shifted along some number of places defined by the key. For example, using the key “key” to encrypt “Hello” results in “Rijvs”.
- **Key Reuse:** The key is repeated if it is shorter than the message, which can make the cipher vulnerable to *frequency analysis attacks*.

**Questions/Answers:**

1. **Q:** What is the main advantage of the Vigenère Cipher over simple substitution ciphers? **A:** It uses multiple substitution alphabets, making it harder to break with frequency analysis.
    
2. **Q:** How does the Vigenère Cipher handle repeated letters in the plaintext? **A:** It alters them differently based on the key, so repeated letters in the plaintext do not result in repeated letters in the ciphertext.
    
3. **Q:** What is a major vulnerability of the Vigenère Cipher? **A:** The reuse of the key, especially if the ciphertext is longer than the key, which can make it susceptible to certain attacks.
    

**Key Points to Remember:**

- Uses a polyalphabetic substitution method.
- Key repetition can lead to vulnerabilities.
- More secure than simple substitution ciphers but not foolproof.

---

### One Time Pad (OTP)

**Overview:** The One Time Pad is an encryption technique that is theoretically unbreakable when used correctly. It requires a single-use pre-shared key that is at least as long as the message being sent.

**Explanation:**

- **Perfect Secrecy:** Each bit or character from the plaintext is encrypted by a modular addition with a bit or character from the key.
- **Key Requirements:** The key must be truly random, used only once, and kept completely secret.

**Questions/Answers:**

1. **Q:** What makes the One Time Pad theoretically unbreakable? **A:** The key is as long as the message and is used only once, ensuring perfect secrecy.
    
2. **Q:** How does the One Time Pad differ from the Vigenère Cipher? **A:** Unlike the Vigenère Cipher, the One Time Pad uses a key that is as long as the message and is never reused.
    
3. **Q:** What is a critical requirement for the One Time Pad to maintain its security? **A:** The key must be truly random and kept completely secret.
    

**Key Points to Remember:**

- Provides perfect secrecy when used correctly.
- Key must be as long as the message and used only once.
- Vulnerable if the key is reused or not truly random.

---

### Enigma Machine

**Overview:** The Enigma Machine was a famous encryption device used by the German military during World War II. It used a complex system of rotors and plugboards to encrypt messages.

**Explanation:**

- **Encryption Strength:** Equivalent to a 76-bit encryption key, making it very secure for its time.
- **Operational Use:** Messages were encrypted and decrypted using the same machine settings, which changed daily.

**Questions/Answers:**

1. **Q:** What was the primary use of the Enigma Machine? **A:** It was used by the German military to encrypt communications during World War II.
    
2. **Q:** How secure was the Enigma Machine’s encryption? **A:** It was roughly equivalent to a 76-bit encryption key, making it very secure for its time.
    
3. **Q:** What was a major factor in the Enigma Machine’s eventual decryption by the Allies? **A:** The use of the Turing Bombe and other cryptographic techniques to break the Enigma’s encryption.
    

**Key Points to Remember:**

- Used by the German military in WWII.
- Equivalent to a 76-bit encryption key.
- Eventually decrypted by the Allies using the Turing Bombe.

---

### Turing Bombe

**Overview:** The Turing Bombe was an electro-mechanical device used by British cryptologists to help decipher German Enigma-machine-encrypted messages during World War II.

**Explanation:**

- **Purpose:** Designed to find the settings of the Enigma machine by testing various possible configurations.
- **Impact:** Played a crucial role in the Allied victory by allowing them to intercept and understand German communications.

**Questions/Answers:**

1. **Q:** What was the primary function of the Turing Bombe? **A:** To decipher German Enigma-machine-encrypted messages by testing various possible configurations.
    
2. **Q:** Who was a key figure in the development of the Turing Bombe? **A:** Alan Turing, a British mathematician and logician.
    
3. **Q:** How did the Turing Bombe contribute to the Allied efforts in WWII? **A:** It allowed the Allies to intercept and understand German communications, significantly aiding their war efforts.
    

**Key Points to Remember:**

- Used to decipher Enigma-encrypted messages.
- Developed by British cryptologists, including Alan Turing.
- Crucial in the Allied victory in WWII.

---

### Common Terms in Cryptography

**Overview:** Understanding common terms is essential for grasping the basics of cryptography.

**Explanation:**

- **Cleartext/Plaintext:** Unencrypted data.
- **Ciphertext:** Encrypted data.
- **Key:** Information used to create the encryption and/or decryption process.
- **Algorithm:** The mathematical equation used to scramble/descramble the plaintext.

**Questions/Answers:**

1. **Q:** What is the difference between plaintext and ciphertext? **A:** Plaintext is unencrypted data, while ciphertext is encrypted data.
    
2. **Q:** What role does a key play in cryptography? **A:** A key is used to create the encryption and/or decryption process.
    
3. **Q:** What is an algorithm in the context of cryptography? **A:** It is the mathematical equation used to scramble/descramble the plaintext.
    

**Key Points to Remember:**

- Cleartext/Plaintext: Unencrypted data.
- Ciphertext: Encrypted data.
- Key: Used for encryption/decryption.
- Algorithm: Mathematical equation for encryption/decryption.


>[!sources]
>
>https://people.cs.uchicago.edu/~davidcash/284-autumn-21/slides-01.pdf
>https://www.cs.swarthmore.edu/~chaganti/cs88/s24/lecs/11-Symmetric-Key-Cryptography.pdf
>https://www.geeksforgeeks.org/implementation-of-vernam-cipher-or-one-time-pad-algorithm/
>https://www.geeksforgeeks.org/vigenere-cipher/
>https://www.cs.uchicago.edu/~davidcash/284-autumn-21/
>https://creativecommons.org/licenses/by-sa/3.0/deed.en
>


---


### Encryption

**Overview:** Encryption is a process that transforms original data (cleartext) into an unreadable format (ciphertext) using an algorithm and a key. This ensures that only authorized parties can read the data.

**Explanation:**

- **Process:** Encryption scrambles data using a specific algorithm and a key, making it unreadable to anyone who does not have the decryption key.
- **Purpose:** It is primarily used to protect the confidentiality of data, ensuring that sensitive information remains secure during transmission or storage.

**Questions/Answers:**

1. **Q:** What is the main purpose of encryption? **A:** To protect the confidentiality of data by transforming it into an unreadable format.
    
2. **Q:** What are the two main components required for encryption? **A:** An algorithm and a key.
    
3. **Q:** Can encrypted data be reverted back to its original form? **A:** Yes, using the correct decryption key and algorithm.
    

**Key Points to Remember:**

- Scrambles data into ciphertext.
- Requires an algorithm and a key.
- Ensures data confidentiality.

---

### Hash

**Overview:** Hashing is a process that converts input data of any size into a fixed-size string of characters, known as a hash value or digest. It is primarily used to verify data integrity and quickly compare large sets of data.

**Explanation:**

- **One-Way Function:** Hashing is irreversible; once data is hashed, it cannot be converted back to its original form.
- **Purpose:** Ensures data integrity and authenticity but does not provide confidentiality.

**Questions/Answers:**

1. **Q:** What is the primary purpose of hashing? **A:** To verify data integrity and quickly compare large sets of data.
    
2. **Q:** Can a hash value be reversed to obtain the original data? **A:** No, hashing is a one-way function and cannot be reversed.
    
3. **Q:** Does hashing provide data confidentiality? **A:** No, hashing ensures data integrity and authenticity but not confidentiality.
    

**Key Points to Remember:**

- Converts data into a fixed-size hash value.
- Irreversible one-way function.
- Ensures data integrity and authenticity.

---

### Encryption vs Hashing

**Overview:** While both encryption and hashing are cryptographic techniques used to protect data, they serve different purposes and have distinct characteristics.

**Explanation:**

- **Encryption:** Focuses on confidentiality and reversible transformation. Commonly used in securing communications (e.g., HTTPS), protecting sensitive data in databases, and securing files and emails.
- **Hashing:** Focuses on data integrity, authenticity, and irreversible transformation. Used for password storage, digital signatures, data integrity verification, and in cryptographic protocols.

**Questions/Answers:**

1. **Q:** What is the main focus of encryption? **A:** Confidentiality and reversible transformation.
    
2. **Q:** What is the main focus of hashing? **A:** Data integrity, authenticity, and irreversible transformation.
    
3. **Q:** Can encrypted data be decrypted back to its original form? **A:** Yes, with the correct decryption key and algorithm.
    

**Key Points to Remember:**

- **Encryption:** Ensures confidentiality, reversible.
- **Hashing:** Ensures integrity and authenticity, irreversible.
- Both are essential for different aspects of data security.


