# Python based roblox script de-obfuscator!

**Luaminifier.py** and **Luaminf.manual.py**: Powerful Python utilities for deobfuscating and beautifying Lua scripts. These scripts allow you to make your Lua code more readable through automatic and manual renaming of variables and functions, as well as advanced decompilation techniques.

---

## ⚠️ IMPORTANT NOTICE: READ USAGE BEFORE STARTING THE SCRIPT! ⚠️
  

**Potential Issues**  
If the script **closes unexpectedly**, you may have misconfigured it during the tweaks.  
Please **double-check** your adjustments before trying again.

---

## 🛠️ **Scripts Overview**

### 1. **Luaminifier.py**
A Python-based tool designed to enhance the readability of obfuscated Lua scripts. It performs deobfuscation by renaming variables and functions, improving the formatting by adjusting indentation and semicolons, and adding several additional Lua code optimizations such as:

- **Variable & Function Deobfuscation**: Automatically renames variables and functions to improve readability.
- **Beautification**: Adjusts indentation and formats code for cleaner presentation.
- **Makeshift Decompiler**: Attempts to reverse certain types of Lua obfuscation patterns, simplifying the code further.
- **Handling Encoded Strings**: Decodes base64-encoded and hex-encoded strings in the Lua code.
- **Optimized for Performance**: Regex optimizations and error handling for better script performance.

### 2. **Luaminf.manual.py** (NEW)
A complementary script to **Luaminifier.py**. This tool offers **manual and automated renaming** of variables and functions after the initial deobfuscation process, giving users full control over making Lua scripts readable and maintainable.


### 3. **testfile.py** (NEWEST)
A fully new test file, just for now. 
- **Requirements**: openai api key (paid).
- `pip install openai` to actually use.
- uses chatgpt after de-obfuscation, to help rename functions and variables, and change the spacing errors (obviously could be done manually).
- Has not been tested yet!

  
#### Key Features:
- **Interactive Renaming**: Detects all variables and functions in the deobfuscated Lua script and allows the user to manually rename them for better readability.
- **Automated Renaming**: Offers an option to automatically rename variables and functions based on predefined patterns.
- **Advanced Decompilation Techniques**: Simplifies complex Lua patterns, such as obfuscated table indexing and function signatures, making the code more readable.
- **File Handling**: Automatically saves the updated Lua script to a new file with all renaming applied.
- **Improved Edge Case Handling**: Gracefully handles missing or malformed Lua code files and provides meaningful error feedback.

---

## 📋 **Changelog**:

### **UPDATE 1**:  
- Improved the code by renaming functions, variables, etc., to numbers, increasing readability.  
- Started removing semicolons for better formatting.  

### **UPDATE 2**:  
- Semicolon removal **completed**.  

### **UPDATE 3**:  
- Now adds a **new line** after encountering closing characters `)`, `}`, `]`.

### **UPDATE 4**:  
- **Re-added semicolons** to improve readability.

### 🔥 **UPDATE 5: DECOMPILER FEATURE ADDED!** 🔥  
- A makeshift decompiler has been implemented—check it out!

### **UPDATE 6**:  
- Inserted a space before the keyword `"local"` for better formatting.

### **UPDATE 7**:  
- Additional features added to the makeshift decompiler.

###  **UPDATE 8**   
- **Predefined Renaming Patterns**: You can now automatically rename variables and functions based on a custom prefix, simplifying the renaming process.
- **Advanced Decompilation**: Added new techniques to handle more complex obfuscation patterns in Lua code, such as table indexing simplification.
- **Improved Edge Case Handling**: Enhanced error handling for missing or malformed Lua files, ensuring more robust execution.
- **Logging & Error Feedback**: Improved logging for better issue tracing.

### **UPDATE 9**
- **Lots of changes**: Overhauled the script a bit, now can decode base64 normally. Can decode tables, decod string.char-s aswell. Better identification of whats a function and whats not a function.

### **UPDATE 10**
- **Math**: Can do simple math now.
  
## 🚀 **How to Use**:

### Step 1: Run **Luaminifier.py** to Deobfuscate Lua Code
1. Open a terminal or command line in the directory containing the `luaminifier.py` script.
2. MAKE SURE TO HAVE YOUR SCRIPT THAT YOU WANT TO DE-OBFUSCATE BE NAMED; `script.txt` AND IT BEING IN THE SAME DIRECTORY AS THE DE-OBFUSCATOR!
3. Run the script to deobfuscate your Lua code:
    ```bash
    python luaminifier.py
    ```
4. Your new file will be named; `deobf_script.txt`
### Step 2: Run **Luaminf.manual.py** for Manual/Automated Renaming
1. Once your Lua code is deobfuscated, run `luaminf.manual.py` to manually or automatically rename variables and functions for better readability.
2. The script will prompt you to either manually rename or automate the renaming based on a pattern:
    ```bash
    python luaminf.manual.py
    ```
3. The manually or automatically renamed Lua script will be saved as a new file (e.g., `my_lua_script_renamed.lua`).

---

## 🛠️ **Planned Features**:
- **Further Advanced Decompilation**: More techniques to handle highly complex obfuscated Lua code structures.
- **Pattern-based Renaming Enhancements**: Improve the automation of renaming by using smarter patterns that analyze the Lua code for context-aware naming.
- **Comprehensive Error Handling**: Enhancing robustness against malformed scripts, particularly for unconventional obfuscation methods.
- **Increased Logging and Debugging Support**: Providing more detailed logs for better debugging of Lua scripts during the deobfuscation process.

---

Made with AI (chatgpt), expect errors.

## 💡 **Contributing**
If you have suggestions or improvements, feel free to open an issue or submit a pull request! Contributions are always welcome to help enhance these Lua deobfuscation tools.
