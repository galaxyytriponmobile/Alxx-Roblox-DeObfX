import re
import ast
import base64
import operator

# --- Safe math evaluator ---
def safe_eval(expr):
    node = ast.parse(expr, mode='eval')

    def eval_node(node):
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        elif isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            if isinstance(node.op, ast.Div): return left / right
            if isinstance(node.op, ast.FloorDiv): return left // right
        elif isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -eval_node(node.operand)
        raise ValueError("Unsafe expression")
    return str(eval_node(node))

# --- Evaluate math expressions ---
def eval_math_expressions(code):
    pattern = re.compile(r'(?<![\w])([-+]?\d+(?:\.\d+)?(?:\s*[-+*/]\s*[-+]?\d+(?:\.\d+)?)+)(?![\w])')

    def repl(match):
        expr = match.group(1)
        try:
            return safe_eval(expr)
        except:
            return expr

    prev = None
    while prev != code:
        prev = code
        code = pattern.sub(repl, code)
    return code

# --- Beautifier ---
def beautify_code(code):
    indent_level = 0
    beautified = ''
    indent_keywords = {'function', 'if', 'else', 'elseif', 'for', 'while', 'do'}
    unindent_keywords = {'end', 'else', 'elseif'}
    for line in code.splitlines():
        stripped = line.strip()
        if any(stripped.startswith(kw) for kw in unindent_keywords):
            indent_level = max(indent_level - 1, 0)
        beautified += '    ' * indent_level + stripped + '\n' if stripped else '\n'
        if any(stripped.startswith(kw) for kw in indent_keywords):
            indent_level += 1
    return beautified

# --- string.char and tables ---
def inline_string_chars(code):
    code = re.sub(
        r'string\.char\(([0-9,\s]+)\)',
        lambda m: '"' + ''.join(chr(int(x)) for x in m.group(1).split(',')) + '"',
        code
    )
    def repl_table(match):
        var = match.group(1)
        nums = match.group(2)
        s = ''.join(chr(int(x)) for x in nums.split(','))
        return f'local {var}_resolved = "{s}"'
    code = re.sub(r'local\s+(\w+)\s*=\s*\{([\d,\s]+)\}', repl_table, code)
    return code

# --- Base64 decoding ---
def decode_base64_literals(code):
    def repl(match):
        b64 = match.group(1)
        try:
            return '"' + base64.b64decode(b64).decode('utf-8') + '"'
        except:
            return match.group(0)
    return re.sub(r'"([A-Za-z0-9+/=]{8,})"', repl, code)

# --- Emulate loadstring ---
def emulate_loadstring(code):
    def repl(match):
        left, right = match.group(1), match.group(2)
        return f'local _exec = loadstring({left} .. {right})\n_exec()'
    return re.sub(r'loadstring\((\w+_resolved)\s*\.\.\s*(\w+_resolved)\)', repl, code)

# --- Rename identifiers ---
def rename_identifiers(code):
    vars_ = re.findall(r'local\s+(\w+)', code)
    var_map = {v: f'deobf_var_{i+1}' for i, v in enumerate(vars_) if not v.endswith('_resolved')}
    for orig, new in var_map.items():
        code = re.sub(rf'(?<!\.)\b{orig}\b', new, code)
    funcs = re.findall(r'function\s+(\w+)', code)
    func_map = {f: f'deobf_func_{i+1}' for i, f in enumerate(funcs)}
    for orig, new in func_map.items():
        code = re.sub(rf'\b{orig}\b', new, code)
    return code

# --- Full pipeline ---
def process_lua_code(path):
    with open(path, 'r') as f:
        code = f.read()
    code = inline_string_chars(code)
    code = decode_base64_literals(code)
    code = emulate_loadstring(code)
    code = rename_identifiers(code)
    code = eval_math_expressions(code)
    code = beautify_code(code)
    return code

# --- Main ---
if __name__ == '__main__':
    import sys
    in_file = sys.argv[1] if len(sys.argv) > 1 else 'script.txt'
    out_file = sys.argv[2] if len(sys.argv) > 2 else 'deobf_script.txt'
    deobf = process_lua_code(in_file)
    with open(out_file, 'w') as f:
        f.write(deobf)
    print(f'Deobfuscated saved to {out_file}')
    input("Press enter to close the script.")
