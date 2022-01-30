import json

### TOOLS TO NAVIGATE JSON RESPONSE
def _val_str_to_type(s):
    """parses json dump and removes quotes from values"""
    new = ''
    encounter = 0
    for i in range(len(s)):
        if s[i]==':' and s[i+2] == '"': #begin parsing key's value
            encounter = 1
        if s[i]=='"' and s[i+1] in [',', '\n']: #end parse of value
            encounter = 0
            continue
        if s[i] == '"' and encounter: #ignore quotes
            continue
        else:
            new += s[i]
            
    return new

type2sample = {str:"string", float:3.1415, int:42, list:'[...]'}
def dict_tree_map(d, semantic=False):
    """Display dictionary as a simple tree, with leaves as data types
    Helps navigate deeply nested or lenghty JSON response
    TODO: display dictionaries present in list"""
    tree_start = {}
    def traverse(d, tree):
        for i in d.keys():
            if isinstance(d[i], dict):
                tree[i] = {}
                traverse(d[i], tree[i])
            else:
                if semantic:
                    tree[i] = type2sample[type(d[i])]
                else:
                    tree[i] = str(type(d[i])).split("'")[1] #convert  type to string so json serializable
    traverse(d, tree_start)
    tree_str = json.dumps(tree_start, sort_keys=False, indent=4)
    print(_val_str_to_type(tree_str))