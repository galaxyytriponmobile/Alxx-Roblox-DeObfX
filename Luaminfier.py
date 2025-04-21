import re
import base64

# --- Beautifier Function ---
def beautify_code(code):
    indent_level = 0
    beautified = ''
    indent_keywords = {'function', 'if', 'else', 'elseif', 'for', 'while', 'do'}
    unindent_keywords = {'end', 'else', 'elseif'}
    for line in code.splitlines():
        stripped = line.strip()
        # decrease indent before lines with unindent keywords
        if any(stripped.startswith(kw) for kw in unindent_keywords):
            indent_level = max(indent_level - 1, 0)
        if stripped:
            beautified += '    ' * indent_level + stripped + '\n'
        else:
            beautified += '\n'
        # increase indent after lines with indent keywords
        if any(stripped.startswith(kw) for kw in indent_keywords):
            indent_level += 1
    return beautified

# --- Inline string.char and static tables ---
def inline_string_chars(code):
    # string.char(65,66) -> "AB"
    code = re.sub(
        r'string\.char\(([0-9,\s]+)\)',  # Fixed this line by adding a closing parenthesis
        lambda m: '"' + ''.join(chr(int(x)) for x in m.group(1).split(',')) + '"',
        code
    )
    # local p1 = {112,114} -> local p1_resolved = "pr"
    def repl_table(match):
        var = match.group(1)
        nums = match.group(2)
        s = ''.join(chr(int(x)) for x in nums.split(','))
        return f'local {var}_resolved = "{s}"'
    code = re.sub(r'local\s+(\w+)\s*=\s*\{([\d,\s]+)\}', repl_table, code)
    return code

# --- Decode base64 literals ---
def decode_base64_literals(code):
    def repl(match):
        b64 = match.group(1)
        try:
            decoded = base64.b64decode(b64).decode('utf-8')
            return f'"{decoded}"'
        except:
            return match.group(0)
    return re.sub(r'"([A-Za-z0-9+/=]{8,})"', repl, code)

# --- Emulate loadstring ---
def emulate_loadstring(code):
    def repl_ls(match):
        left = match.group(1)
        right = match.group(2)
        return f'local _exec = loadstring({left} .. {right})\n_exec()'
    return re.sub(r'loadstring\((\w+_resolved)\s*\.\.\s*(\w+_resolved)\)', repl_ls, code)

# --- Rename identifiers ---
def rename_identifiers(code):
    # rename locals
    vars_ = re.findall(r'local\s+(\w+)', code)
    var_map = {}
    cnt = 1
    for v in vars_:
        if v.endswith('_resolved'):
            continue
        var_map[v] = f'deobf_var_{cnt}'
        cnt += 1
    for orig, new in var_map.items():
        code = re.sub(rf'(?<!\.)\b{orig}\b', new, code)
    # rename functions
    funcs = re.findall(r'function\s+(\w+)', code)
    func_map = {}
    cnt = 1
    for f in funcs:
        func_map[f] = f'deobf_func_{cnt}'
        cnt += 1
    for orig, new in func_map.items():
        code = re.sub(rf'(?<!\.)\b{orig}\b', new, code)
    return code

# --- Full pipeline ---
def process_lua_code(path):
    with open(path, 'r') as f:
        code = f.read()
    code = inline_string_chars(code)
    code = decode_base64_literals(code)
    code = emulate_loadstring(code)
    code = rename_identifiers(code)
    code = beautify_code(code)
    return code

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1] if len(sys.argv) > 1 else 'script.txt'
    out_file = sys.argv[2] if len(sys.argv) > 2 else 'deobf_script.txt'
    deobf = process_lua_code(in_file)
    with open(out_file, 'w') as f:
        f.write(deobf)
    print(f'Deobfuscated saved to {out_file}')
input("Press enter to close the script.")

