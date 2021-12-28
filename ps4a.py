# Problem Set 4A
# Name: Nithin
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Base case: len(sequence) = 1
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        for permutation in get_permutations(sequence[1:]):
            for possible_index in range(len(permutation) + 1):
                mod_permutation = list(permutation)
                mod_permutation.insert(possible_index, sequence[0])
                permutations.append("".join(mod_permutation))
        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


# Nithin note: remember only 3 chars or less or, by multiplication rule, permutation of n
# distinct elements is n!, a large number for values n > 3 whereas n = 3 yields 3! = 6 perm.

    print("Input:", "jit")
    print("Expected Output:", ["jit", "ijt", "itj", "jti", "tji", "tij"])
    print("Actual Output:", get_permutations("jit"))
    
    print("Input:", "cat")
    print("Expected Output:", ["cat", "act", "atc", "cta", "tca", "tac"])
    print("Actual Output:", get_permutations("cat"))
    
    print("Input:", "god")
    print("Expected Output:", ["god", "ogd", "odg", "gdo", "dgo", "dog"])
    print("Actual Output:", get_permutations("god"))
    
    # All 3 test cases passed