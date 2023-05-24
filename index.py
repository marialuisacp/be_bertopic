from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']
model = BERTopic(language="portuguese")

df = pd.read_csv('04_nova_almeida_atualizada.csv')


