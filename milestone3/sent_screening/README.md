# Sentence screening
The sentences for annotation were selected as described below. The automatic screening was documented [here](Sentence_Extraction_final.ipynb).

### Step 1. Extracted texts related to climate change
From the entire corpus, we extracted texts that contained 'climate change' in the submission titles This resulted in 4,524 sentences (98,164 word tokens).

### Step 2. Keyword selection by Tf-Idf
We obtained Tf-Idf weights for unigrams and bigrams, based on all the texts from Step 1. Trigrams were also investigated but they were found to be not useful for our project. For instance, the top ranked trigrams like "solution climate change" and "change end human" are not grammatical, thus not suitable as keywords for exact match in a sentence. For each aspect, we hand-picked keywords from [this](tfidf_result.txt) for each aspect of our interest. In addition, we defined a list of 'must' words such as 'climate change', 'carbon emission', 'renewable energy'. For each sentence, we first checked if it contains one of 'must' words; if yes, we checked if it contained one of 'aspect' words. We filtered out sentences that were too short or too long by setting the minimum word count of 15 and the maximum 70. This resulted in [722 sentences](climate_change_raw_v3.csv).

### Step 3. Pruning and manual cleaning
To further reduce the number of sentences, ~200 sentences were randomly filtered out. Then each sentence was manually inspected for duplicate sentences (when the respondent cites someone else's mention) and non-essential characters (e.g., '>' used to cite an earlier mention). As the sentences were listed in the order of 'politics/government', 'humanity/consumers', 'science/academia', 'industry/economy', we shuffled the sentences to control for an order effect. This resulted in [516 sentences](climate_change_edit_v3_n521_shuffled.csv).

