fruits= ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [x.capitalize() for x in fruits]


fruits_with_only_two_vowels = [x for x in fruits]
for i in range(len(fruits)):
    if