# COLX 523 Group 7 Project Proposal

## Source of data

We are going to use the Reddit API to scrape documents from the Change my View subreddit, where users post their opinion on a topic and ask to hear arguments from the opposing point of view. The documents will be collected from delta threads (i.e., threads where the original poster was persuaded to change their view). The subreddit helpfully contains a list of posts relating to climate change that can be accessed [here](https://www.reddit.com/r/DeltaLog/search?q=climate+change&restrict_sr=on&sort=relevance&t=all).

## Text characteristics

Each document will be a sentence from a delta thread on the Change my View subreddit. As our annotation scheme collects information related to four stakeholder groups, or aspects (politics/government, scientists/academia, industry, and consumers), we will filter for comments that touch on at least one of these aspects using a keyword search. The keywords relevant to each topic will be obtained using tf-idf. Although a given comment may contain multiple sentences, we will extract the specific sentence(s) that contain the keyword(s). These “focus sentences” are what will be presented for annotation.

The writing style of Change my View users is such that most of the sentences will be in clear, grammatically correct, non-technical English. We do not intend to impose a limit on the maximum length of sentences, but based on the data we have extracted so far, we expect that the document lengths will be fairly consistent and not unreasonably long. We will also make any edits that may be necessary for interpretability, including substituting unreadable characters.

Sentences that are potentially too short (i.e., <15 words) to express an interpretable opinion on climate change will be filtered out automatically. Sentences that are clearly irrelevant to our annotation scheme will be filtered out manually.

## Corpus characteristics

Based on the scraping we have done so far, we expect to be able to find about 500 sentences. Along with the focus sentences themselves, we will extract the titles of the posts to which they are responding. Presenting the post title to annotators might be useful in resolving any ambiguities in the focus sentence.

Our corpus will be stored in json format.

## Annotation characteristics

Annotators will be doing a form of sentiment analysis related to the four aspects mentioned above. If a given aspect is not touched on in the sentence, annotators will select “None” for that aspect for that sentence. If an aspect is touched upon, then the annotator will attempt to determine the attitude of the commenter towards climate change. If they seem concerned about climate change or supportive of measures to combat climate change, then under any aspects that are mentioned in the sentence, they will select "Concerned about climate change"; if not, they will select "Not concerned about climate change". If the commenter’s attitude towards climate change cannot be inferred from the sentence provided, then the annotator will select "Neutral" under any aspects mentioned in the sentence.

## Applications

Although we will be doing sentiment analysis with respect to each of our four aspects, the information on distribution of topics will be useful in and of itself as a measure of how frequently each of our stakeholder groups figure into public, non-expert discussion of climate change. That is, it will enable us to answer questions like "Is the public more interested in the relationship between industry and climate change or that between government and climate change?". Similarly, the sentiment analysis component will be of interest independent of stakeholder groups to which it applies: how worried about climate change are Reddit users? Finally, the joint distribution of stakeholder groups and sentiments will tell us how concerned people whose take on climate change is mediated through their knowledge of industry, consumers, etc. are.