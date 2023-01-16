a={
    'b':{
        'c':1,'d':2,'e':3
    },

    'f': {
        'g': 1, 'h': 2, 'i': 3
    },

    'j': {
        'k': 1, 'l': 2, 'i': 3
    }
}

print(a['j']['l'])

b=dict(health=330,mana=100)
c=b.copy()

import copy

aa=copy.deepcopy(a)