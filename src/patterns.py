class Patterns:    
    # List of patterns to be matched
    
    pat_1 = [
        #{"LEMMA" : {"IN" : ["be", "contain", "use", "need", "have"]}},
        {"DEP" : "ROOT"},
        {"IS_ALPHA" : True, "OP": "+"}
    ]
    
    pat_2 = [
        {"RIGHT_ID": "attr",
        "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["be", "use", "need", "have"]}}
        },
        {"LEFT_ID": "attr",
        "REL_OP": ">",
        "RIGHT_ID": "ingredient",
        "RIGHT_ATTRS": {"DEP": "attr"}
        }  
    ]
    
    #? Sembra funzionante su passivo
    passive_pat = [
        {"RIGHT_ID": "passive",
        "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["use", "need"]}}
        },
        {
        "LEFT_ID": "passive",
        "REL_OP": ">",
        "RIGHT_ID": "ingredient1",
        "RIGHT_ATTRS": {"DEP": "nsubjpass"}   
        },
        {
        "LEFT_ID": "ingredient1",
        "REL_OP": ">",
        "RIGHT_ID": "ingredient2",
        "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod"]}}     
        }
    ]
    
    #? Abbozzato, funziona per la frase con contains, ma probabilmente si può generalizzare
    pat_3 = [
        {"RIGHT_ID": "contains",
        "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["contain"]}}
        },
        {
        "LEFT_ID": "contains",
        "REL_OP": ">",
        "RIGHT_ID": "ingredient_1",
        "RIGHT_ATTRS": {"DEP": "ccomp"}   
        },
        {"LEFT_ID": "contains",
        "REL_OP": ">",
        "RIGHT_ID": "ingredient_2",
        "RIGHT_ATTRS": {"DEP": "dobj"}
        }
    ]
    
    #TODO:aggiungere pattern per una risposta con soli ingredienti (Es. "Crisopa Fly", Es2. "Crisopa fly and Mazzei's moustache")
