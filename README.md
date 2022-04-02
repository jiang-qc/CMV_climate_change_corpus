# Source of the corpus

We built this corpus by scraping Reddit. Specifically, we scraped the subreddit called "Change My View" (CMV; see here). CMV is a very popular community for online discussion dedicated to civil discourse. According to the organizers, this community is built around the idea that understanding comes first for resolving our differences. To that end, they promote productive conversations that are marked with respect and openness" (for more details, see here).

Our motivation was to build a corpus that could be useful for argumentation mining. Even in English, argumentation mining is still a low-resourced domain (e.g., Skeppstedt, et al., 2018). "What makes an argument persuasive?" "How do people justify their stance when succeeding in persuasion?" "Are there certain linguistic cues that make people feel respected and more open to other's opinion?" These are all important research questions that are yet to be answered to fill the gap between machine-generated text and human text.

Possible applications will include a personal coaching bot with which corporate managers can simulate negotiation and brush up their communication skills, a counseling chatbot with which the patient can interact to develop social skills, and a ghost writer that can transform human text into more persuasive writing.

CMV is a perfect choice for us because, not only it has a record history of constructive arguments, but also it has a special symbol, delta, to acknowledge the opinion that successfully changed someone's view. This approach has been employed in the literature, but the sizes of their corpora are very small (e.g., Hidey, et al., 2017). This fact made our choice even more focused. Instead of just scraping all the text in CMV, we scraped multi-participant discourse that eventually led to 'Aha!', the moment that is signified by the symbol delta.

For example, below is a thread from the topic "Roadside advertising should be illegal." Here, the participant Reddits_Worst_Night granted "delta" to the participant hucklebae, which was then confirmed by DeltaBot (Reddit's bot that checks the validity of deltas). The six light-gray lines to the left of the delta giver Reddits_Worst_Night signifies this thread contains six comments in total.






# COLX_523_Group7

Qichao Jiang  
Andrew Stich  
Yuesheng Luo  
Toshiko Shibano  

## Repo organization

Milestone-specific written documents will be saved in `milestone{1, 2, 3, 4}`.

All the code will be saved in `src`.

```
COLX_523_Group7
├── README.md
├── milestone1
│   └── README.md
├── milestone2
│   └── README.md
├── milestone3
│   └── README.md
├── milestone4
│   └── README.md
└── src
    └── README.md
```


