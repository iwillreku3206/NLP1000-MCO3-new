import pandas as pd

parallel_corpora = pd.read_csv('parallel_corpora.csv')

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'english') 
     & (parallel_corpora['language2'] == 'filipino')
][['language1_text', 'language2_text']]

corpora.to_csv("en-to-tl-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'bicol') 
     & (parallel_corpora['language2'] == 'ivatan')
][['language1_text', 'language2_text']]

corpora.to_csv("bicol-to-ivatan-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'ivatan') 
     & (parallel_corpora['language2'] == 'yami')
][['language1_text', 'language2_text']]

corpora.to_csv("ivatan-to-yami-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'english') 
     & (parallel_corpora['language2'] == 'yami')
][['language1_text', 'language2_text']]
    
corpora.to_csv("english-to-yami-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'bicol') 
     & (parallel_corpora['language2'] == 'english')
][['language1_text', 'language2_text']]

corpora['temp'] = corpora['language1_text']
corpora['language1_text'] = corpora['language2_text']
corpora['language2_text'] = corpora['temp']
corpora = corpora.drop(columns=['temp'])
    
corpora.to_csv("english-to-bicol-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'bicol') 
     & (parallel_corpora['language2'] == 'filipino')
][['language1_text', 'language2_text']]

corpora['temp'] = corpora['language1_text']
corpora['language1_text'] = corpora['language2_text']
corpora['language2_text'] = corpora['temp']
corpora = corpora.drop(columns=['temp'])
    
print(f"tgl-bicol: {len(corpora)}")

corpora.to_csv("tagalog-to-bicol-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'bicol') 
     & (parallel_corpora['language2'] == 'english')
][['language1_text', 'language2_text']]

corpora.to_csv("bicol-to-english-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'english') 
     & (parallel_corpora['language2'] == 'filipino')
][['language1_text', 'language2_text']]

corpora['temp'] = corpora['language1_text']
corpora['language1_text'] = corpora['language2_text']
corpora['language2_text'] = corpora['temp']
corpora = corpora.drop(columns=['temp'])

corpora.to_csv("tagalog-to-english-corpora.csv")

corpora = parallel_corpora[
    (parallel_corpora['language1'] == 'cebuano') 
     & (parallel_corpora['language2'] == 'english')
][['language1_text', 'language2_text']]

print(f"ceb-eng: {len(corpora)}")

corpora.to_csv("cebuano-to-english-corpora.csv")