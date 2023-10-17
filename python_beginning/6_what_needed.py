#!/usr/bin/python3
sentence = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."
#can't find the good solution and answer for your tricky sentence . Does it link for ----"Dutch follows the Subject-Object-Verb (SOV) word order in main clauses, which means the subject typically comes first, followed by the object, and then the verb. However, this can change in questions and subordinate clauses." ?

sentence =sentence[sentence.index("preferably"):(sentence.index("preferably")+len("preferably "))]+ sentence[sentence.index("only"):(sentence.index("only")+len("only "))]+ sentence[sentence.index("one"):(sentence.index("one")+len("one"))]+ " "+  sentence[sentence.index("way"):(sentence.index("way")+len("way "))] + sentence[sentence.index("unless"):(sentence.index("unless")+len("unless"))]

print(sentence)
