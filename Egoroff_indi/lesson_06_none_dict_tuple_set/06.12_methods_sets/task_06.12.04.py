""" Перед вами располагается множество my_set
Ваша задача удалить из него 3 строковых элемента:
government
national
tease
Выводить ничего не нужно, только удалить элементы выше"""

my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',
    'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',
    'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',
    'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention',
    'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national',
    'tradition', 'government', 'mention', 'proposal'
}
# variant 1:
my_set.remove('government')
my_set.remove('national')
my_set.remove('tease')

# variant 2:
# my_set.discard('government')
# my_set.discard('national')
# my_set.discard('tease')

# variant 3:
# my_set -= {'government', 'national', 'tease'}

# variant 4:
# my_set.difference_update(('government', 'national', 'tease'))

# variant 5:
# [my_set.remove(i) for i in ('government','national','tease')]
