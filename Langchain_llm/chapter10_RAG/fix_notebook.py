import json

file_path = r'D:\JAVAprogram\Langchain_llm\chapter10_RAG\01-DocumentLoaders.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    corrupted = json.load(f)

source = corrupted['cells'][0]['source']
if isinstance(source, list):
    inner_json_str = ''.join(source)
else:
    inner_json_str = source

original_notebook = json.loads(inner_json_str)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(original_notebook, f, indent=1, ensure_ascii=False)

print('修复完成！')
print('单元格数量:', len(original_notebook['cells']))
for i, cell in enumerate(original_notebook['cells']):
    print('  Cell %d: type=%s' % (i, cell['cell_type']))