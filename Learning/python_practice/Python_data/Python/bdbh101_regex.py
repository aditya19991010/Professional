import re
import sys

# credit: https://realpython.com/regex-python/
def regex1():

    s = 'foo123bar'
    print(re.search('123', s))  # <_sre.SRE_Match object; span=(3, 6), match='123'>

    # Match object can be used as boolean value
    if re.search('123', s):
        print('Found a match.')
    else:
        print('No match.')

    ### metacharacters
    s = 'foo123bar'
    # In a regex, a set of characters specified in square brackets ([]) makes up a character class.
    # This metacharacter sequence matches any single character that is in the class
    # The full expression [0-9][0-9][0-9] matches any sequence of three decimal digit characters.
    print(re.search('[0-9][0-9][0-9]', s))  # <_sre.SRE_Match object; span=(3, 6), match='123'>
    print(re.search('[0-9][0-9][0-9]', 'foo456bar'))  # <_sre.SRE_Match object; span=(3, 6), match='456'>
    print(re.search('[0-9][0-9][0-9]', '234baz'))  # <_sre.SRE_Match object; span=(0, 3), match='234'>
    print(re.search('[0-9][0-9][0-9]', 'qux678'))  # <_sre.SRE_Match object; span=(3, 6), match='678'>
    print(re.search('[0-9][0-9][0-9]', '12foo34'))  # None

    # The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard
    s = 'foo123bar'
    print(re.search('1.3', s))  # <_sre.SRE_Match object; span=(3, 6), match='123'>
    s = 'foo13bar'
    print(re.search('1.3', s))  # None

    # metacharacters supported by the re module
    # Character(s)	Meaning
    # .	        Matches any single character except newline
    # ^	        Anchors a match at the start of a string,  Complements a character class
    # $	        Anchors a match at the end of a string
    # *	        Matches zero or more repetitions
    # +	        Matches one or more repetitions
    # ?	        Matches zero or one repetition, Specifies the non-greedy versions of *, +, and ?,
    #           Introduces a lookahead or lookbehind assertion, Creates a named group
    # {}	    Matches an explicitly specified number of repetitions
    # \	        Escapes a metacharacter of its special meaning, Introduces a special character class,
    #           Introduces a grouping backreference
    # []	    Specifies a character class
    # |	        Designates alternation
    # ()	    Creates a group
    # :         Designate a specialized group
    # #         Designate a specialized group
    # =         Designate a specialized group
    # !	        Designate a specialized group
    # <>	    Creates a named group


    # [] A character class metacharacter sequence will match any single character contained in the class.
    print(re.search('ba[artz]', 'foobarqux')) # <_sre.SRE_Match object; span=(3, 6), match='bar'>
    print(re.search('ba[artz]', 'foobazqux')) # <_sre.SRE_Match object; span=(3, 6), match='baz'>
    # A character class can also contain a range of characters separated by a hyphen (-),
    # in which case it matches any single character within the range.
    # For example, [a-z] matches any lowercase alphabetic character between 'a' and 'z', inclusive
    print(re.search('[a-z]', 'FOObar')) # <_sre.SRE_Match object; span=(3, 4), match='b'>
    print(re.search('[0-9][0-9]', 'foo123bar')) # <_sre.SRE_Match object; span=(3, 5), match='12'>
    # You can complement a character class by specifying ^ as the first character,
    # in which case it matches any character that isn’t in the set.
    # In the following example, [^0-9] matches any character that isn’t a digit
    print(re.search('[^0-9]', '12345foo')) # <_sre.SRE_Match object; span=(5, 6), match='f'>
    # If a ^ character appears in a character class but isn’t the first character,
    # then it has no special meaning and matches a literal '^' character
    print(re.search('[#:^]', 'foo^bar:baz#qux')) # <_sre.SRE_Match object; span=(3, 4), match='^'>
    print(re.search('[#:^]', 'foo^bar:baz#qux')) # <_sre.SRE_Match object; span=(3, 4), match='^'>
    #  if you want the character class to include a literal hyphen character
    # You can place it as the first or last character or escape it with a backslash (\)
    print(re.search('[-abc]', '123-456')) # <_sre.SRE_Match object; span=(3, 4), match='-'>
    print(re.search('[abc-]', '123-456')) # <_sre.SRE_Match object; span=(3, 4), match='-'>
    print(re.search('[ab\-c]', '123-456')) # <_sre.SRE_Match object; span=(3, 4), match='-'>
    # If you want to include a literal ']' in a character class,
    # then you can place it as the first character or escape it with backslash
    print(re.search('[]]', 'foo[1]')) # <_sre.SRE_Match object; span=(5, 6), match=']'>
    print(re.search('[ab\]cd]', 'foo[1]')) # <_sre.SRE_Match object; span=(5, 6), match=']'>
    # Other regex metacharacters lose their special meaning inside a character class:
    print(re.search('[)*+|]', '123*456')) # <_sre.SRE_Match object; span=(3, 4), match='*'>
    print(re.search('[)*+|]', '123+456')) # <_sre.SRE_Match object; span=(3, 4), match='+'>
    
    ### dot (.) - The . metacharacter matches any single character except a newline:
    print(re.search('foo.bar', 'fooxbar')) # <_sre.SRE_Match object; span=(0, 7), match='fooxbar'>
    print(re.search('foo.bar', 'foobar')) # None
    print(re.search('foo.bar', 'foo\nbar')) # None

    ### \W - Match based on whether a character is a word character.
    # \w matches any alphanumeric word character.\w is essentially shorthand for [a-zA-Z0-9_]
    print(re.search('\w', '#(.a$@&')) # <_sre.SRE_Match object; span=(3, 4), match='a'>
    print(re.search('[a-zA-Z0-9_]', '#(.a$@&')) # <_sre.SRE_Match object; span=(3, 4), match='a'>
    # \W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]
    print(re.search('\W', 'a_1*3Qb')) # <_sre.SRE_Match object; span=(3, 4), match='*'>
    print(re.search('[^a-zA-Z0-9_]', 'a_1*3Qb')) # <_sre.SRE_Match object; span=(3, 4), match='*'>

    ### \d, \D - Match based on whether a character is a decimal digit.
    # \d is essentially equivalent to [0-9], and \D is equivalent to [^0-9].
    print(re.search('\d', 'abc4def')) # <_sre.SRE_Match object; span=(3, 4), match='4'>
    print(re.search('\D', '234Q678')) # <_sre.SRE_Match object; span=(3, 4), match='Q'>

    ### \s, \S - Match based on whether a character represents whitespace.
    # unlike the dot wildcard metacharacter, \s does match a newline character
    print(re.search('\s', 'foo\nbar baz')) # <_sre.SRE_Match object; span=(3, 4), match='\n'>
    print(re.search('\S', '  \n foo  \n  ')) # <_sre.SRE_Match object; span=(4, 5), match='f'>
    # The character class sequences \w, \W, \d, \D, \s, and \S can appear inside a square bracket character class as well:
    print(re.search('[\d\w\s]', '---3---')) # <_sre.SRE_Match object; span=(3, 4), match='3'>
    print(re.search('[\d\w\s]', '---a---')) # <_sre.SRE_Match object; span=(3, 4), match='a'>
    print(re.search('[\d\w\s]', '--- ---')) # <_sre.SRE_Match object; span=(3, 4), match=' '>

    ### Escaping metacharacters
    # backslash (\) - Removes the special meaning of a metacharacter.
    print(re.search('.', 'foo.bar')) # <_sre.SRE_Match object; span=(0, 1), match='f'>
    print(re.search('\.', 'foo.bar')) # <_sre.SRE_Match object; span=(3, 4), match='.'>
    s = r'foo\bar'
    print(s)
    print(re.search('\\', s))
    print(re.search('\\\\', s)) # <_sre.SRE_Match object; span=(3, 4), match='\\'>
    # the following is cleaner and suppresses \ at the interpreter level
    # It’s good practice to use a raw string to specify a regex in Python whenever it contains backslashes.
    print(re.search(r'\\', s)) # <_sre.SRE_Match object; span=(3, 4), match='\\'>

    ### Anchors
    # ^ , A - Anchor a match to the start of <string>.
    print(re.search('^foo', 'foobar')) # <_sre.SRE_Match object; span=(0, 3), match='foo'>
    print(print(re.search('^foo', 'barfoo'))) # None
    print(re.search('\Afoo', 'foobar')) # <_sre.SRE_Match object; span=(0, 3), match='foo'>
    print(re.search('\Afoo', 'barfoo')) # None

    ### $ , \Z - Anchor a match to the end of <string>.
    print(re.search('bar$', 'foobar')) # <_sre.SRE_Match object; span=(3, 6), match='bar'>
    print(re.search('bar$', 'barfoo')) # None
    print(re.search('bar\Z', 'foobar')) # <_sre.SRE_Match object; span=(3, 6), match='bar'>
    print(re.search('bar\Z', 'barfoo')) # None
    print(re.search('bar$', 'foobar\n')) # <_sre.SRE_Match object; span=(3, 6), match='bar'>

    ### \b - Anchors a match to a word boundary.
    print(re.search(r'\bbar', 'foo bar')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search(r'\bbar', 'foo.bar')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search(r'\bbar', 'foobar')) # None
    print(re.search(r'foo\b', 'foo bar')) # <_sre.SRE_Match object; span=(0, 3), match='foo'>
    print(re.search(r'foo\b', 'foo.bar')) # <_sre.SRE_Match object; span=(0, 3), match='foo'>'
    print(print(re.search(r'foo\b', 'foobar'))) # None
    # Using the \b anchor on both ends of the <regex> will cause it to match when
    # it’s present in the search string as a whole word:
    print(re.search(r'\bbar\b', 'foo bar baz')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search(r'\bbar\b', 'foo(bar)baz')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search(r'\bbar\b', 'foobarbaz')) # None
    print(re.search(r'\Bfoo\B', 'foo')) # None
    print(re.search(r'\Bfoo\B', '.foo.')) # None
    print(re.search(r'\Bfoo\B', 'barfoobaz')) # <_sre.SRE_Match object; span=(3, 6), match='foo'>


    ### Quantifiers - A quantifier metacharacter immediately follows a portion of a <regex> and
    # indicates how many times that portion must occur for the match to succeed.
    # * Matches zero or more repetitions of the preceding regex.
    # For example, a* matches zero or more 'a' characters. That means it would match
    # an empty string, 'a', 'aa', 'aaa', and so on.

    ### *
    # # zero dashes -
    print(re.search('foo-*bar', 'foobar')  ) # <_sre.SRE_Match object; span=(0, 6), match='foobar'>
    # One dash
    print(re.search('foo-*bar', 'foo-bar')) # <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
    # Two dashes
    print(re.search('foo-*bar', 'foo--bar')) # <_sre.SRE_Match object; span=(0, 8), match='foo--bar'>
    # the regex .* matches zero or more occurrences of any character
    print(re.search('foo.*bar', '# foo $qux@grault % bar #')) #<_sre.SRE_Match object; span=(2, 23), match='foo $qux@grault % bar'>

    ### + - Matches one or more repetitions of the preceding regex.
    # Zero dash
    print(re.search('foo-+bar', 'foobar'))  # None
    print(re.search('foo-+bar', 'foo-bar')) # <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
    print(re.search('foo-+bar', 'foo--bar')) # <_sre.SRE_Match object; span=(0, 8), match='foo--bar'>

    ### ? - Matches zero or one repetitions of the preceding regex.
    print(re.search('foo-?bar', 'foobar')) # <_sre.SRE_Match object; span=(0, 6), match='foobar'>
    print(re.search('foo-?bar', 'foo-bar')) # <_sre.SRE_Match object; span=(0, 7), match='foo-bar'>
    print(re.search('foo-?bar', 'foo--bar')) # None

    print(re.match('foo[1-9]*bar', 'foobar')) # <_sre.SRE_Match object; span=(0, 6), match='foobar'>
    print(re.match('foo[1-9]*bar', 'foo42bar')) # <_sre.SRE_Match object; span=(0, 8), match='foo42bar'>
    print(re.match('foo[1-9]+bar', 'foobar')) # None
    print(re.match('foo[1-9]+bar', 'foo42bar')) # <_sre.SRE_Match object; span=(0, 8), match='foo42bar'>
    print(re.match('foo[1-9]?bar', 'foobar')) # <_sre.SRE_Match object; span=(0, 6), match='foobar'>
    print(re.match('foo[1-9]?bar', 'foo42bar')) # None

    ### The non-greedy or lazy versions of *, + and ?
    # *?, +?, ?? - The non-greedy (or lazy) versions of the *, +, and ? quantifiers.
    # When used alone, the quantifier metacharacters *, +, and ? are all greedy,
    # meaning they produce the longest possible match.
    print(re.search('<.*>', '%<foo> <bar> <baz>%')) # <_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>
    print(re.search('<.*?>', '%<foo> <bar> <baz>%')) # <_sre.SRE_Match object; span=(1, 6), match='<foo>'>
    print(re.search('<.+>', '%<foo> <bar> <baz>%')) # <_sre.SRE_Match object; span=(1, 18), match='<foo> <bar> <baz>'>
    print(re.search('<.+?>', '%<foo> <bar> <baz>%')) # <_sre.SRE_Match object; span=(1, 6), match='<foo>'>
    print(re.search('ba?', 'baaaa')) # <_sre.SRE_Match object; span=(0, 2), match='ba'>
    print(re.search('ba??', 'baaaa')) # <_sre.SRE_Match object; span=(0, 1), match='b'>

    ### {m} - Matches exactly m repetitions of the preceding regex.
    # This is similar to * or +, but it specifies exactly how many times the preceding regex must occur for a match to succeed:
    # Here, x-{3}x matches 'x', followed by exactly three instances of the '-' character, followed by another 'x'.
    # The match fails when there are fewer or more than three dashes between the 'x' characters.
    # two dashses
    print(re.search('x-{3}x', 'x--x')) # None
    print(re.search('x-{3}x', 'x---x') ) # <_sre.SRE_Match object; span=(0, 5), match='x---x'>
    # four dashes
    print(re.search('x-{3}x', 'x----x')) # None

    ### {m, n} - Matches any number of repetitions of the preceding regex from m to n, inclusive.
    print(re.search('x-{2,4}x', 'x---x')) # <re.Match object; span=(0, 5), match='x---x'>
    print(re.search('x{}y', 'x{}y')) # <_sre.SRE_Match object; span=(0, 4), match='x{}y'>

    ### {m,n}? - The non-greedy (lazy) version of {m,n}.
    # {m,n} will match as many characters as possible, and {m,n}? will match as few as possible:
    print(re.search('a{3,5}', 'aaaaaaaa')) # <_sre.SRE_Match object; span=(0, 5), match='aaaaa'>
    print(re.search('a{3,5}?', 'aaaaaaaa')) # <_sre.SRE_Match object; span=(0, 3), match='aaa'>


    ### Grouping Constructs and Backreferences
    # grouping - A group represents a single syntactic entity. Additional metacharacters apply to the entire group as a unit.
    # A regex in parentheses just matches the contents of the parentheses:
    print(re.search('(bar)', 'foo bar baz')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search('(bar)+', 'foo bar baz')) # <_sre.SRE_Match object; span=(4, 7), match='bar'>
    print(re.search('(bar)+', 'foo barbar baz')) # <_sre.SRE_Match object; span=(4, 10), match='barbar'>
    print(re.search('(bar)+', 'foo barbarbarbar baz')) # <_sre.SRE_Match object; span=(4, 16), match='barbarbarbar'>

    # read the interpretation table (Treating a Group as a Unit) in https://realpython.com/regex-python/#treating-a-group-as-a-unit

    # The regex (ba[rz]){2,4}(qux)? matches 2 to 4 occurrences of either 'bar' or 'baz', optionally followed by 'qux':
    print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux')) # <_sre.SRE_Match object; span=(0, 12), match='bazbarbazqux'>
    print(re.search('(ba[rz]){2,4}(qux)?', 'barbar')) # <_sre.SRE_Match object; span=(0, 6), match='barbar'>
    























def main():
    # result = re.match(pattern, source)

    # checks if source begins with the pattern
    result = re.match('Rohit', 'Rohit Sharma')
    print(result)
    # compile your pattern to speed up the search later
    pattern = re.compile("Rohit")
    result = pattern.match("Rohit Sharma")
    print(result)

    # search returns the first match, if any
    pattern = re.compile("Sha")
    m = pattern.search("Rohit Sharma")
    if m:
        print(m.group())

    # . means any single character.
    # * means any number of the preceding thing. Together, .* mean any number of
    # characters (even zero).
    # Ten is the phrase that we wanted to match, somewhere.
    source = "Sachin Ramesh Tendulkar"
    m = re.match('.*Ten', source)
    if m:
        print(m.group())


    # findall() returns a list of all non-overlapping matches, if any.
    source = "It was a good match against Australia with good cricket display"
    pattern = re.compile("good")
    result = pattern.findall(source)
    print(result)
    # good followed by any character and that is optional
    m = re.findall("good.?", source)
    print(m)

    # split() splits source at matches with pattern and returns a list of the string pieces.
    pattern = re.compile("good")
    result = pattern.split("It was a good match against Australia with good cricket display")
    print(result)

    # sub() takes another replacement argument, and changes all parts of source that
    # are matched by pattern to replacement.
    result = re.sub("good", "great", "It was a good match against Australia with good cricket display")
    print(result)

    #Special characters
    # Pattern   Matches
    # \d        a single digit
    # \D        a single non-digit
    # \w        an alphanumeric character
    # \W        a non-alphanumeric character
    # \s        a whitespace character
    # \S        a non-whitespace character
    # \b        a word boundary (between a \w and a \W, in either order)
    # \B        a non-word boundary
    import string
    printable = string.printable
    print(len(printable))
    print(printable[0:50])
    print(printable[50:])
    # Which characters in printable are digits?
    m = re.findall('\d', printable)
    if m:
        print(m)
    # Which characters are digits, letters, or an underscore?
    m = re.findall('\w', printable)
    if m:
        print(m)
    # Which are spaces?
    m = re.findall('\s', printable)
    if m:
        print(m)

    # Pattern specifiers
    # Pattern           Matches
    # abc               literal abc
    # ( expr )          expr
    # expr1 | expr2     expr1 or expr2
    # .                 any character except \n
    # ^                 start of source string
    # $                 end of source string
    # prev ?            zero or one prev
    # prev *            zero or more prev, as many as possible
    # prev *?           zero or more prev, as few as possible
    # prev +            one or more prev, as many as possible
    # prev +?           one or more prev, as few as possible
    # prev { m }        m consecutive prev
    # prev { m, n }     m to n consecutive prev, as many as possible
    # prev { m, n }?    m to n consecutive prev, as few as possible
    # [ abc ]           a or b or c (same as a|b|c)
    # [^ abc ]          not (a or b or c)
    # prev (?= next )   prev if followed by next
    # prev (?! next )   prev if not followed by next
    # (?<= prev ) next  next if preceded by prev
    # (?<! prev ) next  next if not preceded by prev

    #
    source = '''I wish I may, I wish I might Have a dish of fish tonight.'''
    # find wish anywhere:
    m = re.findall('wish', source)
    if m:
        print(m)
    # find wish or fish anywhere:
    m = re.findall('wish|fish', source)
    if m:
        print(m)
    # Find wish at the beginning:
    m = re.findall('^wish', source)
    if m:
        print(m)
    # Find I wish at the beginning:
    m = re.findall('^I wish', source)
    if m:
        print(m)
    # Find fish at the end:
    m = re.findall('fish$', source)
    if m:
        print(m)
    # find fish tonight. at the end:
    m = re.findall('fish tonight.$', source)
    if m:
        print(m)
    # Begin by finding w or f followed by ish:
    m = re.findall('[wf]ish', source)
    if m:
        print(m)
    # Find one or more runs of w, s, or h
    m = re.findall('[wsh]+', source)
    if m:
        print(m)
    # Find ght followed by a non-alphanumeric:
    m = re.findall('ght\W', source)
    if m:
        print(m)
    # Find I followed by wish:
    m = re.findall('I (?=wish)', source)
    if m:
        print(m)
    # wish preceded by I:
    m = re.findall('(?<=I) wish', source)
    if m:
        print(m)

    # Python's raw strings
    print(re.findall('\bfish', source))  # \b means backspace in strings
    # Avoid the accidental use of escape characters by using Python’s raw strings when you define your
    # regular expression string. Always put an r character before your regular expression
    # pattern string, and Python escape characters will be disabled
    print(re.findall(r'\bfish', source)) # use r in pattern always


    # Patterns: specifying match output
    # When using match() or search(), all matches are returned from the result object m as
    # m.group(). If you enclose a pattern in parentheses, the match will be saved to its own
    # group, and a tuple of them will be available as m.groups(),
    m = re.search(r'(. dish\b).*(\bfish)', source)
    print(m.group())
    print(m.groups())

    # If you use this pattern (?P< name > expr ), it will match expr, saving the match in
    # group name:
    m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
    print(m.group())
    print(m.groups())
    print(m.group('DISH'))
    print(m.group('FISH'))





    # re.search(pattern, string, flags=0)
    # # Scan through string looking for the first location where the
    # # regular expression pattern produces a match, and return a
    # # corresponding match object. Return None if no position in the
    # # string matches the pattern.
    # #
    # # This program reports if a motif (ATG followed by zero or more any
    # # characters-non greedy-ending with TAA) is present in a DNA sequence,
    # # and prints the matched substring, the start and end indices.

    DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
    print('DNA_sequence:', DNA_sequence)

    motif = r'ATG.*?TAA'  # r for raw string
    # motif = r'[ATG.*?TAA'       # This is an invalid regular expression
    print('Motif:', motif)

    # Checking if motif is a valid regular expression
    try:
        re.compile(motif)
    except:
        print('Invalid regular expression, exiting the program!')
        sys.exit()

    match = re.search(motif, DNA_sequence)

    if match:
        print('Found the motif   :', match.group())
        print('Starting at index :', match.start())
        print('Ending at index   :', match.end())
    else:
        print('Did not find the motif.')

    ## example 2
    # # Match.group([group1, ...])
    # # Returns one or more subgroups of the match. If there is a single argument,
    # # the result is a single string; if there are multiple arguments, the result
    # # is a tuple with one item per argument. Without arguments, group1 defaults
    # # to zero (the whole match is returned). If a groupN argument is zero, the
    # # corresponding return value is the entire matching string; if it is in the
    # # inclusive range [1..99], it is the string matching the corresponding
    # # parenthesized (...) group.
    # #
    # # This program reports if a motif (ATG followed by zero or more any
    # # characters-non greedy-ending with TAA) is present in a DNA sequence
    # # and lists the groupings (two groups are the motif found and the characters
    # # between ATG and TAA in the found motif).
    DNA_sequence = 'AATGAAGGGCCGCTACGATAAGGAACTTCGTAATTTCAG'
    print('DNA_sequence:', DNA_sequence)
    motif = r'(ATG(.*?)TAA)'
    print('Motif:', motif)

    # Checking if motif is a valid regular expression
    try:
        re.compile(motif)
    except:
        print('Invalid regular expression, exiting the program!')
        sys.exit()

    match = re.search(motif, DNA_sequence)

    if match:
        print('group0           :', match.group(0))
        print('group0 start-end :', match.start(0), match.end(0))
        print('group1           :', match.group(1))
        print('group1 start-end :', match.start(1), match.end(1))
        print('group2           :', match.group(2))
        print('group2 start-end :', match.start(2), match.end(2))
        print('groups as tuples :', match.groups())
    else:
        print('Did not find the motif.')

if __name__ == "__main__":
    # main()

    # more examples
    regex1()
