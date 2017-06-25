"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""



def has_balanced_brackets(string):

    # build a dictionary of closers to openers
    closers_to_openers = {")": "(", "}": "{", "]": "[", ">": "<"}

    #set of openers to compare to while looping
    openers = set(closers_to_openers.values())
    
    #list of seen openers 
    openers_seen = []


    for char in string:
        #pushes open characters to openers_seen
        if char in openers:
            openers_seen.append(char)
        
        #check closing characters, the values of the dictionary 
        elif char in closers_to_openers:
            #if there are no opening characters return false
            if openers_seen == []:
                return False 

            if openers_seen[-1] == closers_to_openers.get(char):
                openers_seen.pop()

            else:
                return False 

    return openers_seen == []


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"

