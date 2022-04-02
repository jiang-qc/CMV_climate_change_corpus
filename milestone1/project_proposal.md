# COLX 523 Group 7 Project Proposal

## Source of data

We are going to use tweepy API to scrape tweets from [Twitter](twitter.com).

## Text characteristics

Each document will be a tweet that mentions a concept or topic related to cryptocurrency. In our current implementation, we are using keywords and hashtags to detect relevant tweets. Since many of these keywords are likely to be the same in any language (e.g. "Bitcoin"), the language of the documents is unrestricted (although, to judge from the sample tweets collected for our proof of concept, most of the results will be in English). In future implementations we will use the language filtering function of tweepy in conjunction with a tool such as spacy's `langdetect` to limit results to English-language text.

Because of this keyword-based approach, the register and authorship of the tweets will also be unrestricted. The length of each document will be capped at 280 characters, the maximum length of a tweet.

## Corpus characteristics

Assuming the average English word is 4.7 characters long and the average tweet is 140 characters long (this is just an assumption -- we have not collected data on this), we will need to collect about 40,000 tweets to match the size of Brown corpus (1,161,192 words). In fact, the number of tweets collected in our initial scrape will have to be greater than this so that our corpus has an appropriate size once spam tweets have been removed. (We may use a classifier to assist with this.) This number is subject to adjustment as we explore the accuracy of the above assumptions. Since cryptocurrency is a popular topic on Twitter it seems unlikely that we will have difficulty finding enough tweets.

Our corpus will be unstructured above the level of individual tweets; e.g., we are not binning together tweets belonging to a single discussion thread.

We are planning to store our corpus in json format, with the tweet text occupying one field and the subject, predicate, and object annotations each occupying their own respective fields (see below under Annotation characteristics). As the subject will at times be first-person (i.e., the author of the tweet) and at other times be third-person (some entity that the tweet refers to), we will need to collect metadata on the tweet authors, as this will sometimes be directly used in our annotation scheme.

## Annotation characteristics

For each applicable sentence in each tweet we are going to be annotating subject, predicate, and object. The exact list of predicates is still to be determined, but will most likely include at least "ownerOf" (an existing dbpedia predicate), "participatesIn" (an existing predicate) and "minerOf" (a predicate we will have to define). Our idea for "participatesIn" is that the object will be the blockchain or hyperledger system. We are looking into using/defining new predicates that interact with these in a non-trivial way (e.g., not "ownedBy" which would just swap the subject and object of "ownerOf") and allow us to exploit RDF's graph operations to automatically deduce new relationships.

## Applications

Our corpus will be useful for determining the popularity of different cryptocurrencies (the objects in our annotation scheme) on Twitter. The subjects will also be useful in the case that they refer to entities such as countries, financial firms, etc. and not anonymous Twitter users. This information would be of interest to anyone wanting to gauge the level and sources of interest in cryptocurrencies.

## Servicing the under-resourced domain

New terms, meanings, and relationships are often found in the domain of technological innovation. Tasatanattakool et al. (2018) says, “The technology that has had the most impact on our lifestyles in the last decade is Blockchain. … Many people still confuse Blockchain with Bitcon; however, they are not the same.” The more pervasive the technology is, the more entities are involved. The more entities are involved, the more relationships are born. The more innovative the technology is, the more new terms are coined and the more existing terms have new meanings.

So what exactly is blockchain? What is the difference from Bitcoin? Simply put, blockchain is a form of database that functions as a digital public ledger. Bitcoin is a digital currency (cryptocurrency) maintained by the Blockchain technology. There are more new terms. NFT stands for non-fungible token. Hyperledger is a global blockchain project that offers framework and guidelines to build open-source blockchains (Frankenfield, 2021). Miner is an existing term that means “a person who works in a mine” (Oxford Dictionary), but in the context of blockchain, it means a transaction verifier. 

When looking up on [DBpedia](https://dbpedia.org/page/Category:Cryptocurrencies), there are only a handful of existing properties/predicates, which do not seem to keep up with the knowledge present in the ecosystem of cryptocurrency. In that sense, cryptocurrency is an under-resourced domain. Annotating the entities in terms of “miners” and “participants” relationships would be directly useful for named entity recognition tasks. Also they would help anaphor resolution, which in turn helps text summarization and other downstream tasks.

## References

Tasatanattakool, P., & Techapanupreeda, C. (2018, January). Blockchain: Challenges and applications. In 2018 International Conference on Information Networking (ICOIN) (pp. 473-475). IEEE.

Frankenfield, 2021. https://www.investopedia.com/terms/h/hyperledger.asp
