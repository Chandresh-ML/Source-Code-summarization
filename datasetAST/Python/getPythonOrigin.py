
import json

# save1 = open('data/test', 'w', encoding='utf-8')
save2 = open('data/test/test.token.code', 'w', encoding='utf-8')
save3 = open('data/test/test.token.nl', 'w', encoding='utf-8')
result = []
with open('data/test.jsonl', 'r') as f:
    i = 0
    for jsonstr in f.readlines():
        data = json.loads(jsonstr)
        # lines = source.readline()
        code_strs = ' '.join(data['code_tokens']).replace('\n', '').replace('\r', '').strip() + '\n'
        # result.append(code_strs)
        nl_strs = ' '.join(data['docstring_tokens']).strip()
        save2.write(code_strs)
        i += 1
        save3.write(nl_strs + '\n')

        # print(data['original_string'])
    print(i)
    print(len(result))
i = 0
num = 0

save2.close()
save3.close()