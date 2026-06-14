from pathlib import Path
import json

p = Path('LLMGAURD_Project_notebook.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
md = nb.get('metadata', {})
nb['metadata'] = {k: v for k, v in md.items() if k in ('kernelspec', 'language_info')}
for c in nb['cells']:
    c['metadata'] = {}
    if c.get('cell_type') == 'code':
        c['execution_count'] = None
        c['outputs'] = []
    else:
        c.pop('execution_count', None)
        c.pop('outputs', None)
nb['nbformat'] = 4
nb['nbformat_minor'] = 5
p.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('sanitized')
